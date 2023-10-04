import unittest

from jsonschema.exceptions import ValidationError

from sad_forms.common.env_validator import EnvValidator


class TestsEnvValidator(unittest.TestCase):
    def test_when_everything_is_wrong(self):
        environment = {'DB_HOST': 1, 'DB_PORT': 0, 'DB_NAME': '3',
                       'DB_USER': '4', 'DB_PASSWORD': '5'}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        self.assertEqual("1 is not of type 'string'", cm.exception.message)

    def test_when_host_is_int(self):
        environment = {'DB_HOST': 123, 'DB_PORT': 'asdsa', 'DB_NAME': 'cxzczx',
                       'DB_USER': 'adsad', 'DB_PASSWORD': 'AAAAAA'}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        self.assertEqual("123 is not of type 'string'", cm.exception.message)

    def test_when_db_name_is_long(self):
        environment = {'DB_HOST': '123', 'DB_PORT': 1, 'DB_NAME': '1' * 64,
                       'DB_USER': 'adsad', 'DB_PASSWORD': 'AAAAAA'}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        self.assertEqual("'1111111111111111111111111111111111111111111111111111111111111111' is too long",
                         cm.exception.message)

    def test_when_user_name_is_long(self):
        environment = {'DB_HOST': '123', 'DB_PORT': 1, 'DB_NAME': 'sadsad',
                       'DB_USER': 'a' * 64, 'DB_PASSWORD': 'AAAAAA'}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        self.assertEqual("'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' is too long",
                         cm.exception.message)

    def test_when_password_is_long(self):
        environment = {'DB_HOST': '123', 'DB_PORT': 1, 'DB_NAME': 'sadsad',
                       'DB_USER': 'a', 'DB_PASSWORD': 'A' * 257}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        self.assertEqual(
            "'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' is too long",
            cm.exception.message)

    def test_when_commas_in_host(self):
        environment = {'DB_HOST': '128,0,0,1', 'DB_PORT': 5238, 'DB_NAME': 'postgres',
                       'DB_USER': 'root', 'DB_PASSWORD': 'root'}
        with self.assertRaises(ValidationError) as cm:
            EnvValidator.validate(environment)
        actual_error_message = str(cm.exception.message)
        expected_error_message = "'128,0,0,1' does not match '^(?!-)[A-Za-z0-9-]{1,255}(?<!-)(\\\\.[A-Za-z0-9-]{1,63})*$'"
        self.assertEqual(expected_error_message, actual_error_message)

    def test_when_everything_is_correct(self):
        environment = {'DB_HOST': '127.0.0.1', 'DB_PORT': 5238, 'DB_NAME': 'postgres',
                       'DB_USER': 'root', 'DB_PASSWORD': 'root'}
        self.assertIsNone(EnvValidator.validate(environment))
