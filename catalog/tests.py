from django.test import TestCase

# Create your tests here.
# Run the specified module
py manage.py test catalog.test

# Run the specified module
py manage.py test catalog.test.test_models

# Run the specified class
py manage.py test catalog.test.test_models.YourTestClass

# Run the specified method
py manage.py test catalog.test.test_models.YourTestClass.test_one_plus_one_equals_two