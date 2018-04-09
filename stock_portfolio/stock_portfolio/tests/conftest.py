import pytest
from pyramid import testing

@pytest.fixture
def dummy_request():
    return testing.DummyRequest()


# @pytest.fixture
# def dummy_auth_request():
#     request = testing.DummyRequest(method="POST", params={'username': 'dummy', 'email': 't@g.co', 'password': '1234'})

#     return

