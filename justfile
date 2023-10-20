default:
    just --list

test:
    python -m unittest sad_forms.unit_tests.validator_environment_variables

dev:
    python manage.py runserver
