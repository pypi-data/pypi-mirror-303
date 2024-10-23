"""Teams validator module"""

import os
from collections import Counter
from typing import Dict, List, Tuple

from opendapi.defs import (
    DEFAULT_DAPIS_DIR,
    OPENDAPI_SPEC_URL,
    TEAMS_SUFFIX,
    OpenDAPIEntity,
)
from opendapi.validators.base import BaseValidator, ValidationError


class TeamsValidator(BaseValidator):
    """
    Validator class for Teams files
    """

    SUFFIX = TEAMS_SUFFIX
    SPEC_VERSION = "0-0-1"
    ENTITY = OpenDAPIEntity.TEAMS

    # Paths & keys to use for uniqueness check within a list of dicts when autoupdating
    AUTOUPDATE_UNIQUE_LOOKUP_KEYS: List[Tuple[List[str], str]] = [(["teams"], "urn")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._team_urn_counts = self._collect_team_urn_counts()

    @property
    def team_urns(self) -> List[str]:
        """Return the team urns"""
        return list(self._team_urn_counts.keys())

    def _collect_team_urn_counts(self) -> Dict[str, int]:
        """Collect all the team urns and their counts"""
        return Counter(
            (
                team["urn"]
                for teams_file in self.parsed_files.values()
                for team in teams_file.get("teams", [])
            )
        )

    def _validate_parent_team_urn(self, file: str, content: dict):
        """Validate if the parent team urn is valid"""
        teams = content.get("teams") or []
        for team in teams:
            if (
                team.get("parent_team_urn")
                and team["parent_team_urn"] not in self.team_urns
            ):
                raise ValidationError(
                    f"Parent team urn '{team['parent_team_urn']}'"
                    f" not found in '{team['urn']}' in '{file}'"
                )

    def _validate_team_urns_globally_unique(self, file: str, content: dict):
        """Validate if the team urns are globally unique"""
        non_unique_team_urns = {
            team["urn"]
            for team in content.get("teams", [])
            if self._team_urn_counts[team["urn"]] > 1
        }
        if non_unique_team_urns:
            raise ValidationError(
                f"Non-globally-unique team urns in file '{file}': {non_unique_team_urns}"
            )

    def validate_content(self, file: str, content: Dict):
        """Validate the content of the files"""
        self._validate_parent_team_urn(file, content)
        self._validate_team_urns_globally_unique(file, content)
        super().validate_content(file, content)

    def base_dir_for_autoupdate(self) -> str:
        return os.path.join(self.root_dir, DEFAULT_DAPIS_DIR)

    def base_template_for_autoupdate(self) -> Dict[str, Dict]:
        """Set Autoupdate templates in {file_path: content} format"""
        return {
            f"{self.base_dir_for_autoupdate()}/{self.config.org_name_snakecase}.teams.yaml": {
                "schema": OPENDAPI_SPEC_URL.format(
                    version=self.SPEC_VERSION, entity="teams"
                ),
                "organization": {"name": self.config.org_name},
                "teams": [],
            }
        }
