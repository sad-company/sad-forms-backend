import json
import logging
from pathlib import Path

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class EnvValidator:
    @staticmethod
    def __load_json_schema():
        current_dir = Path(__file__).parent.absolute()

        with open(current_dir / '..' / 'json_schemas/environment_variables.json', 'r') as raw_json_schema:
            return json.load(raw_json_schema)

    @staticmethod
    def validate(environment_variables: dict[str, str]) -> None:
        json_schema = EnvValidator.__load_json_schema()
        try:
            validate(instance=environment_variables, schema=json_schema)
        except ValidationError as e:
            logging.error(f"Environment variable validation error:\n{e}")
            raise e
