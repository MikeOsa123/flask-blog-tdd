import pytest

from app import create_app, db
from app.config import config
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username="mikeosa", email="mike@yahoo.com")
    user.set_password("Password1")
    return user


@pytest.fixture(scope='module')
def test_client():

    flask_app = create_app(config['testing'])
    print(flask_app)
    print(type(flask_app))
    
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database tables
    db.create_all()

    # Insert user data
    user1 = User(username="mikeosa", email="mike@yahoo.com")
    user1.set_password("Password1")
    user2 = User(username="davido", email="davido@gmail.com")
    user2.set_password("sorosoke1")
    db.session.add(user1)
    db.session.add(user2)

    # commit the changes for the users
    db.session.commit()

    yield db 

    db.drop_all()    