"""
This file (test_models.py) contains the unit tests for the models.py file.
"""

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, email and hashed_password are defined correctly
    """
    assert new_user.username == 'mikeosa'
    assert new_user.email == 'mike@yahoo.com'
    assert new_user.password_hash != 'Password1'