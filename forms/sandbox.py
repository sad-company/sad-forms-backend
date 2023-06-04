import json

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def loader_jsonschema():
    with open('json_schema.json', 'r') as text:
        schema = json.load(text)
    return schema


data = '[{"question": "Какой ваш любимый цвет?"},{"question": "Какое ваше любимое животное?"}]'
parsed_data = json.loads(data)
schema = loader_jsonschema()

try:
    validate(instance=parsed_data, schema=schema)
    print("Данные прошли валидацию по схеме.")
except ValidationError as e:
    print("Данные не соответствуют схеме:", e)
