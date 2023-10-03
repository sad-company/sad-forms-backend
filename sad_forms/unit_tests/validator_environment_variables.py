import unittest

from jsonschema.exceptions import ValidationError

from sad_forms.common.env_validator import EnvValidator


class TestEnvironmentVariableValidation(unittest.TestCase):
    def test_when_everything_is_wrong(self):
        environment = {'DB_HOST': '1', 'DB_PORT': '2', 'DB_NAME': '3',
                       'DB_USER': '4', 'DB_PASSWORD': '5'}
        try:
            EnvValidator.validate(environment)
        except ValidationError as e:
            self.assertRaises(ValidationError)

    def test_when_all_letters(self):
        environment = {'DB_HOST': 'sadsadsa', 'DB_PORT': 'asdsad', 'DB_NAME': 'cxzczx',
                       'DB_USER': 'adsad', 'DB_PASSWORD': 'AAAAAA'}
        try:
            EnvValidator.validate(environment)
        except ValidationError as e:
            self.assertRaises(ValidationError)

    def test_when_everything_is_empty(self):
        environment = {'DB_HOST': '', 'DB_PORT': '', 'DB_NAME': '',
                       'DB_USER': '', 'DB_PASSWORD': ''}
        try:
            EnvValidator.validate(environment)
        except ValidationError as e:
            self.assertRaises(ValidationError)

    def test_when_commas(self):
        environment = {'DB_HOST': '128,0,0,1', 'DB_PORT': '5238', 'DB_NAME': 'postgres',
                       'DB_USER': 'root', 'DB_PASSWORD': 'root'}
        try:
            EnvValidator.validate(environment)
        except ValidationError as e:
            self.assertRaises(ValidationError)

    def test_when_everything_is_correct(self):
        environment = {'DB_HOST': '128.0.0.1', 'DB_PORT': '5238', 'DB_NAME': 'postgres',
                       'DB_USER': 'root', 'DB_PASSWORD': 'root'}
        self.assertIsNone(EnvValidator.validate(environment))
