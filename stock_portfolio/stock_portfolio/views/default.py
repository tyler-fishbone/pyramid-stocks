from pyramid.response import Response
from pyramid.view import view_config
from ..sample_data import MOCK_DATA
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
import requests

API_URL = 'https://api.iextrading.com/1.0'

# from sqlalchemy.exc import DBAPIError
# from ..models import MyModel

@view_config(route_name='base', renderer='../templates/base.jinja2', request_method='GET')
def get_base_view(request):
    return Response('base view is functional')

@view_config(route_name='home', renderer='../templates/index.jinja2', request_method='GET')
def get_home_view(request):
    return {}
    # return Response('get_home_view is functional')


@view_config(route_name='auth', renderer='../templates/auth.jinja2')
def get_auth_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('portfolio'))

        except KeyError:
            return {}
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('portfolio'))

    return HTTPNotFound()


@view_config(route_name='stock', renderer='../templates/stock-add.jinja2', request_method='GET')
def get_stock_add_view(request):
    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']

        except KeyError:
            return {}

        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        return {'company': data}

    else:
        raise HTTPNotFound()


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2', request_method='GET')
def get_portfolio_view(request):
    return {
        'stocks' : MOCK_DATA,
    }


@view_config(route_name='stock-detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def get_portfolio_symbol_view(request):
    stock = request.matchdict['symbol']
    print('             {}'.format(stock))
    for stock_item in MOCK_DATA:
        if stock_item['symbol'] == stock:
            return {'stock' : stock_item}
    return {}

