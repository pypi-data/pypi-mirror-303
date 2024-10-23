"""Entrypoint for the OpenDAPI CLI `opendapi generate` command."""

# pylint: disable=duplicate-code

from typing import List, Type

import click

from opendapi.adapters.git import (
    add_named_stash,
    check_if_uncomitted_or_untracked_changes_exist,
    get_checked_out_branch_or_commit,
    pop_named_stash,
    run_git_command,
)
from opendapi.cli.common import (
    Schemas,
    get_opendapi_config_from_root,
    pretty_print_errors,
    print_cli_output,
)
from opendapi.cli.options import (
    BASE_COMMIT_SHA_PARAM_NAME_WITH_OPTION,
    CATEGORIES_PARAM_NAME_WITH_OPTION,
    DAPI_PARAM_NAME_WITH_OPTION,
    DATASTORES_PARAM_NAME_WITH_OPTION,
    PURPOSES_PARAM_NAME_WITH_OPTION,
    SUBJECTS_PARAM_NAME_WITH_OPTION,
    TEAMS_PARAM_NAME_WITH_OPTION,
    dev_options,
    git_options,
    minimal_schema_options,
)
from opendapi.logging import LogDistKey, Timer
from opendapi.validators.base import BaseValidator, MultiValidationError
from opendapi.validators.categories import CategoriesValidator
from opendapi.validators.dapi import DAPI_INTEGRATIONS_VALIDATORS
from opendapi.validators.datastores import DatastoresValidator
from opendapi.validators.subjects import SubjectsValidator
from opendapi.validators.teams import TeamsValidator


@click.command()
@minimal_schema_options
@dev_options
@git_options
def cli(**kwargs):
    """
    Generate DAPI files for integrations specified in the OpenDAPI configuration file.

    For certain integrations such as DBT and PynamoDB, this command will also run
    additional commands in the respective integration directories to generate DAPI files.
    """
    print_cli_output(
        "Generating DAPI files for your integrations per `opendapi.config.yaml` configuration",
        color="green",
    )
    opendapi_config = get_opendapi_config_from_root(
        local_spec_path=kwargs.get("local_spec_path"), validate_config=True
    )

    minimal_schemas = Schemas(
        teams=TEAMS_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
        datastores=DATASTORES_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
        purposes=PURPOSES_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
        dapi=DAPI_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
        subjects=SUBJECTS_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
        categories=CATEGORIES_PARAM_NAME_WITH_OPTION.extract_from_kwargs(kwargs),
    )

    # determine all of the required validators
    validators: List[Type[BaseValidator]] = [
        TeamsValidator,
        DatastoresValidator,
        CategoriesValidator,
        SubjectsValidator,
    ]

    print_cli_output(
        "Identifying your integrations...",
        color="yellow",
    )
    for intg, validator in DAPI_INTEGRATIONS_VALIDATORS.items():
        if opendapi_config.has_integration(intg):
            if validator:
                validators.append(validator)
            print_cli_output(f"  Found {intg}...", color="green")

    # if the base commit is known, determine the file state at that commit
    base_commit_sha = kwargs.get(BASE_COMMIT_SHA_PARAM_NAME_WITH_OPTION.name)
    base_commit_files = {}
    if base_commit_sha:
        print_cli_output(
            "Identifying DAPIs at base commit...",
            color="yellow",
        )
        # need to stash since runners may have generated dapis
        stash_created = add_named_stash(opendapi_config.root_dir, "opendapi-generate")

        # sanity check
        if check_if_uncomitted_or_untracked_changes_exist(opendapi_config.root_dir):
            raise RuntimeError(
                "You have uncommitted or untracked changes. "
                "Please commit or stash them before running this command."
            )

        current_commit_sha = get_checked_out_branch_or_commit(opendapi_config.root_dir)
        run_git_command(opendapi_config.root_dir, ["git", "checkout", base_commit_sha])

        for validator in validators:
            inst_validator = validator(
                root_dir=opendapi_config.root_dir,
                # passing this in manually in case it doesnt exist at the base commit
                override_config=opendapi_config,
                enforce_existence=False,
                should_autoupdate=False,
            )
            base_commit_files.update(inst_validator.parsed_files)

        # ensure that nothing was generated at this stage
        if check_if_uncomitted_or_untracked_changes_exist(opendapi_config.root_dir):
            raise RuntimeError(
                "File changes were detected while reading base_commit_files."
            )

        run_git_command(
            opendapi_config.root_dir, ["git", "checkout", current_commit_sha]
        )
        if stash_created:
            pop_named_stash(opendapi_config.root_dir, "opendapi-generate")

    print_cli_output(
        "Generating DAPI files for your integrations...",
        color="yellow",
    )
    errors = []
    metrics_tags = {"org_name": opendapi_config.org_name_snakecase}
    with Timer(dist_key=LogDistKey.CLI_GENERATE, tags=metrics_tags):

        # In a multi-integration repo, team activation PRs may fail if they are generated for
        # integration A, but validated by integration B, as the fields array will be empty
        # at the time of validation in integration B if it runs before integration A.
        # Therefore, instead of combining the generate and validate steps by invoking `run`,
        # we instead do them as a two step process

        # NOTE: keeping all instances at one time for speed. if we notice memory issues,
        #       do not keep references to instances
        inst_validators = [
            validator(
                root_dir=opendapi_config.root_dir,
                enforce_existence=True,
                should_autoupdate=True,
                schema_to_prune_base_template_for_autoupdate=minimal_schemas.minimal_schema_for(
                    validator
                ),
                base_commit_files=base_commit_files,
            )
            for validator in validators
        ]

        # generate every integration before validating
        for inst_validator in inst_validators:
            inst_validator.maybe_autoupdate()

        # validate every integration
        # NOTE: if there are multiple Dapi integrations, this may do repeat work,
        #       but it is safer to do this than assume all pre-validation logic "sets up"
        #       validation the same in each integration. Currently this is true - validation
        #       is self-encompassed - but this may not always be the case
        for inst_validator in inst_validators:
            try:
                inst_validator.validate()
            except MultiValidationError as exc:
                errors.append(exc)

    if errors:
        pretty_print_errors(errors)
        # fails with exit code 1 - meaning it blocks merging - but as a ClickException
        # it does not go to sentry, which is appropriate, as this is not an error condition
        raise click.ClickException("Encountered one or more validation errors")

    print_cli_output(
        "Successfully generated DAPI files for your integrations",
        color="green",
    )
