import os
import pytest
from pyramid import testing
from ..models.meta import Base
from ..models import Stock


@pytest.fixture
def test_stock():
    return Stock(
        symbol = 'SMPL',
        companyName = 'Sample Inc',
        exchange = 'New York Stock Exchange',
        industry = 'Samples',
        website = 'http://www.sample.com',
        description = 'sample description',
        CEO = 'Ida Sampel',
        issueType = 'cs',
        sector = 'Electronics',
    )


@pytest.fixture
def configuration(request):
    """Setup a database for testing purposes."""
    config = testing.setUp(settings={
        # 'sqlalchecmy.url': 'postgres://localhost:5432/stock_portfolio_testing'
        'sqlalchemy.url': os.environ['stock_portfolio_testing']
    })
    config.include('stock_portfolio.models')
    config.include('stock_portfolio.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a database session for interacting with the test database."""
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Create a dummy GET request with a dbsession."""
    return testing.DummyRequest(dbsession=db_session)



# import pytest
# from pyramid import testing

# @pytest.fixture
# def dummy_request():
#     return testing.DummyRequest()
