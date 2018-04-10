import pytest
from pyramid import testing

@pytest.fixture
def dummy_request():
    return testing.DummyRequest()

# @pytest.fixture
# def test_entry():


# def configuration(request):