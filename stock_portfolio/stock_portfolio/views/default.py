from pyramid.response import Response
from pyramid.view import view_config
from ..sample_data import MOCK_DATA
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models import Stock
from . import DB_ERR_MSG
import requests
import json

API_URL = 'https://api.iextrading.com/1.0'

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


@view_config(route_name='stock', renderer='../templates/stock-add.jinja2')
def get_stock_add_view(request):
    # This code below is not run until form is submitted
    
    if request.method == 'GET':
        try:
            # print(request)
            symbol = request.GET['symbol']

        except KeyError:
            return {}

        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        # print()
        # print(data)
        return {'company': data}
        
    # else:
    #     raise HTTPNotFound()
        

@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2')
def get_portfolio_view(request):
    
    if request.method == 'GET':
        try:
            query = request.dbsession.query(Stock)
            all_stocks = query.all()
        except DBAPIError:
            return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)
        
        return {stocks: all_stocks}
        # return {
        #     'stocks': MOCK_DATA
        # }

    # need to change below method so it utlizes DB
    if request.method == 'POST':
        symbol = request.POST['symbol']
        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        MOCK_DATA.append(data)
        return {'stocks': MOCK_DATA}



@view_config(route_name='stock-detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def get_portfolio_symbol_view(request):

    stock = request.matchdict['symbol']
    # print('             {}'.format(stock))

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.symbol == stock)[0] # can also use .first() for first item
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stock' : stock_detail}


    # for stock_item in MOCK_DATA:
    #     if stock_item['symbol'] == stock:
    #         return {'stock' : stock_item}
    # return {}

