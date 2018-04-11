# Default view properties


def test_default_response_entries_view(dummy_request):
    from ..views.stock import get_portfolio_view

    response = get_portfolio_view(dummy_request)
    assert isinstance(response, dict)
    assert response['stocks'] == []


def test_default_detail_view(dummy_request, db_session, test_stock):
    from ..views.stock import get_portfolio_symbol_view

    db_session.add(test_stock)

    dummy_request.matchdict = {'symbol': 'SMPL'}
    response = get_portfolio_symbol_view(dummy_request)
    assert response['stock'].symbol == 'SMPL'


def test_detail_not_found(dummy_request):
    from ..views.stock import get_portfolio_symbol_view
    from pyramid.httpexceptions import HTTPNotFound

    response = get_portfolio_symbol_view(dummy_request)
    assert isinstance(response, HTTPNotFound)


def test_default_response_get_portfolio_view(dummy_request):
    from ..views.stock import get_portfolio_view

    response = get_portfolio_view(dummy_request)
    assert len(response['stocks']) == 0
    assert type(response) == dict


# def test_valid_post_to_new_view(dummy_request):
#     from ..views.stock import get_portfolio_view
#     from pyramid.httpexceptions import HTTPFound

#     dummy_request.method = 'POST'
#     dummy_request.POST = {
#         'symbol': 'fake symbol',
#         'company': 'some fake company of information',
#         'date': '01-01-2018',
#         'CEO': 'Fakey McFaker',
#     }

#     response = get_portfolio_view(dummy_request)
#     assert response.status_code == 302
#     assert isinstance(response, HTTPFound)


# def test_valid_post_to_new_view_adds_record_to_db(dummy_request, db_session):
#     from ..views.stock import get_portfolio_view
#     from ..models import Stock

#     dummy_request.method = 'POST'
#     dummy_request.POST = {
#         'symbol': 'fake symbol',
#         'company': 'some fake company of information',
#         'date': '01-01-2018',
#         'CEO': 'Fakey McFaker',
#     }

#     # assert right here that there's nothing in the DB

#     get_portfolio_view(dummy_request)
#     query = db_session.query(Stock)
#     one = query.first()
#     assert one.symbol == 'fake symbol'
#     assert one.company == 'some fake company of information'
#     assert type(one.id) == int


# def test_invalid_post_to_new_view(dummy_request):
#     import pytest
#     from ..views.stock import get_portfolio_view
#     from pyramid.httpexceptions import HTTPBadRequest

#     dummy_request.method = 'POST'
#     dummy_request.POST = {}

#     with pytest.raises(HTTPBadRequest):
#         response = get_portfolio_view(dummy_request)
#         assert isinstance(response, HTTPBadRequest)

