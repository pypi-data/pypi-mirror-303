"""PynamoDB DAPI validator module"""

import inspect
import os
from typing import TYPE_CHECKING, Dict, List

from opendapi.defs import OPENDAPI_SPEC_URL
from opendapi.validators.dapi.base import DapiValidator

if TYPE_CHECKING:
    from pynamodb.models import Model  # pragma: no cover


class PynamodbDapiValidator(DapiValidator):
    """
    Validator class for DAPI files created for Pynamo datasets

    Example usage:

    from opendapi.validators.dapi import DapiValidator, PynamodbDapiValidator
    from opendapi.validators.datastores import DatastoresValidator
    from opendapi.validators.purposes import PurposesValidator
    from opendapi.validators.teams import TeamsValidator
    from my_service.db.pynamo import Post, User

    class MyPynamodbDapiValidator(PynamodbDapiValidator):

        def get_pynamo_tables(self):
            return [User, Post]

        def build_datastores_for_table(self, table) -> dict:
            return {
                "sources": [
                    {
                        "urn": "my_company.datastore.dynamodb",
                        "data": {
                            "identifier": table.Meta.table_name,
                            "namespace": "sample_db.sample_schema",
                        },
                    },
                ],
                "sinks": [
                    {
                        "urn": "my_company.datastore.snowflake",
                        "data": {
                            "identifier": table.Meta.table_name,
                            "namespace": "sample_db.sample_schema",
                        },
                    },
                ],
            }

        def build_owner_team_urn_for_table(self, table):
            return f"my_company.sample.team.{table.Meta.table_name}"

        def build_urn_for_table(self, table):
            return f"my_company.sample.dataset.{table.Meta.table_name}"

        # Optional to override if you want to keep all DAPIs together,
        # instead of keeping them next to schema
        def build_dapi_location_for_table(self, table):
            return f"{self.base_dir_for_autoupdate()}/pynamodb/{table.Meta.table_name}.dapi.yaml"
    """

    def get_pynamo_tables(self) -> List["Model"]:
        """Get the Pynamo tables"""
        raise NotImplementedError

    def build_datastores_for_table(self, table: "Model") -> Dict:
        """Build the datastores for the table"""
        raise NotImplementedError

    def build_owner_team_urn_for_table(self, table: "Model") -> str:
        """Build the owner for the table"""
        raise NotImplementedError

    def build_urn_for_table(self, table: "Model") -> str:
        """Build the urn for the table"""
        raise NotImplementedError

    def _dynamo_type_to_dapi_datatype(self, dynamo_type: str) -> str:
        """Convert the DynamoDB type to DAPI data type"""
        dynamo_to_dapi = {
            "S": "string",
            "N": "number",
            "B": "binary",
            "BOOL": "boolean",
            "SS": "string_set",
            "NS": "number_set",
            "BS": "binary_set",
            "L": "array",
            "M": "object",
            "NULL": "null",
        }
        return dynamo_to_dapi.get(dynamo_type) or dynamo_type

    def build_fields_for_table(self, table: "Model") -> List[Dict]:
        """Build the fields for the table"""
        attrs = table.get_attributes()
        fields = []
        for _, attribute in attrs.items():
            fields.append(
                {
                    "name": attribute.attr_name,
                    "data_type": self._dynamo_type_to_dapi_datatype(
                        attribute.attr_type
                    ),
                    "description": None,
                    "is_nullable": attribute.null,
                    "is_pii": None,
                    "access": "private",
                    "data_subjects_and_categories": [],
                    "sensitivity_level": None,
                    "is_personal_data": None,
                    "is_direct_identifier": None,
                }
            )
        fields.sort(key=lambda x: x["name"])
        return fields

    def build_primary_key_for_table(self, table: "Model") -> List[str]:
        """Build the primary key for the table"""
        attrs = table.get_attributes()
        hash_key, range_key = None, None
        for _, attribute in attrs.items():
            if attribute.is_hash_key:
                hash_key = attribute.attr_name
            if attribute.is_range_key:
                range_key = attribute.attr_name
        primary_key = [hash_key] if hash_key else []
        if range_key:
            primary_key.append(range_key)
        return primary_key

    def build_dapi_location_for_table(self, table: "Model") -> str:
        """Build the relative path for the DAPI file"""
        module_name_split = inspect.getfile(table).split("/")
        module_dir = "/".join(module_name_split[:-1])
        location = f"{module_dir}/{table.Meta.table_name.lower()}.dapi.yaml"
        return location

    def _reconcile_polymorphism(
        self, dapi_for_model: Dict[str, Dict]
    ) -> Dict[str, Dict]:
        """Reconcile polymorphism in the DAPIs"""
        dapi_by_location = {}
        # Sort the dapi_for_model by table to have a consistent ordering of models
        # This prevents unnecessary diffs in the DAPI files on each run
        dapi_for_model = dict(
            sorted(dapi_for_model.items(), key=lambda x: inspect.getfile(x[0]))
        )

        for _, value in dapi_for_model.items():
            location = value["location"]
            if location in dapi_by_location:
                # Union the fields across all polymorphic models
                # since they all correspond to the same underlying table
                existing_fields = dapi_by_location[location]["fields"]
                new_fields = value["dapi"]["fields"]
                for field in new_fields:
                    for existing_field in existing_fields:
                        if field["name"] == existing_field["name"]:
                            break
                    else:
                        existing_fields.append(field)
            else:
                dapi_by_location[location] = value["dapi"]

        for _, value in dapi_for_model.items():
            value["dapi"] = dapi_by_location[value["location"]]

        return dapi_for_model

    def base_template_for_autoupdate(self) -> Dict[str, Dict]:
        dapi_for_model = {}
        for table in self.get_pynamo_tables():
            dapi_for_model[table] = {
                "location": self.build_dapi_location_for_table(table),
                "dapi": {
                    "schema": OPENDAPI_SPEC_URL.format(
                        version=self.SPEC_VERSION, entity="dapi"
                    ),
                    "urn": self.build_urn_for_table(table),
                    "owner_team_urn": self.build_owner_team_urn_for_table(table),
                    "description": None,
                    "type": "entity",
                    "datastores": self.build_datastores_for_table(table),
                    "primary_key": self.build_primary_key_for_table(table),
                    "fields": self.build_fields_for_table(table),
                    "context": {
                        "service": table.__module__,
                        "integration": "pynamodb",
                        "rel_model_path": os.path.relpath(
                            inspect.getfile(table),
                            os.path.dirname(self.build_dapi_location_for_table(table)),
                        ),
                    },
                },
            }
        result = {}
        for table, value in self._reconcile_polymorphism(dapi_for_model).items():
            result[value["location"]] = value["dapi"]

        return result
