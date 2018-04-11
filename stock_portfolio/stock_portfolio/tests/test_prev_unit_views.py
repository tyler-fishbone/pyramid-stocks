def test_default_behavior_of_base_view(dummy_request):
    """ tests for base connectivity """
    from ..views.default import get_base_view
    from pyramid.response import Response

    request = dummy_request
    response = get_base_view(request)
    # import pdb ; pdb.set_trace()
    assert isinstance(response, Response)
    assert response.text == 'base view is functional'


def test_default_behavior_of_home_view(dummy_request):
    """ tests for home connectivity """
    from ..views.default import get_home_view
    from pyramid.response import Response

    request = dummy_request
    response = get_home_view(request)
    # import pdb ; pdb.set_trace()
    assert isinstance(response, dict)


# def test_default_behavior_of_portfolio_view(dummy_request):
#     """ test MOCK data to see if it is callable"""
#     from ..views.default import get_portfolio_view

#     response = get_portfolio_view(dummy_request)
#     print(response)
#     assert type(response) == dict
#     assert response['stocks'][0]['symbol'] == 'GE'

## can't test user input
# def test_default_behavior_of_auth_view(dummy_request):
#     """ tests for auth view """
#     from ..views.default import get_auth_view
#     from pyramid.response import Response

#     request = dummy_request
#     response = get_auth_view(request)
#     # import pdb ; pdb.set_trace()
#     assert isinstance(response, dict)

# def test_signin_to_auth_view(dummy_auth_request):
#     from ..views.default import my_auth_view(dummy_auth_request):
#     from pyramid.httpexceptions import HTTPFound

#     response = my_auth_view(dummy_auth_request)

    
#     assert isinstance(my_auth_view.dummy_auth_request())
#     request = dummy_auth_request

#     request.method = 'GET'


# def test_default_behavior_of_stock_add_view(dummy_request):
#     """ tests for stock_add connectivity """
#     from ..views.default import get_stock_add_view
#     from pyramid.response import Response

#     request = dummy_request
#     response = get_stock_add_view(request)
#     # import pdb ; pdb.set_trace()
#     assert isinstance(response, dict)

# def test_default_behavior_of_stock_add_view(dummy_request):
#     """ tests for stock_add connectivity """
#     from ..views.default import get_stock_add_view
#     from pyramid.response import Response

#     request = dummy_request
#     response = get_stock_add_view(request)
#     # import pdb ; pdb.set_trace()
#     assert isinstance(response, dict)
