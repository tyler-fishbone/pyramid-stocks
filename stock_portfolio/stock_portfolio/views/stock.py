from pyramid.response import Response
from pyramid.view import view_config
from ..sample_data import MOCK_DATA
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED
from ..models import Stock
from . import DB_ERR_MSG
import requests
import json

API_URL = 'https://api.iextrading.com/1.0'

@view_config(route_name='stock', renderer='../templates/stock-add.jinja2')
def get_stock_add_view(request):
    
    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']

        except KeyError:
            return {}

        try:
            response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
            data = response.json()
            return {'company': data}
        except ValueError:
            print('That stock does not exist')
            return HTTPFound(location=request.route_url('stock'))


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2')
def get_portfolio_view(request):
    

    if request.method == 'GET':
        try:
            query = request.dbsession.query(Stock)
            all_stocks = query.all()
        except DBAPIError:
            return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)
        
        return {'stocks': all_stocks}

    # Get info from API
    if request.method == 'POST':
        try:
            symbol = request.POST['symbol']
        except KeyError:
            return HTTPBadRequest()
        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        data = response.json()
        data['account_id'] = request.authenticated_userid
    
    # to grab userid
    # account_id = request.authenticated_userid

        # Check if info already DB
        my_object = request.dbsession.query(Stock).filter(Stock.symbol == data['symbol']).first()
        if not my_object:
            e = Stock(**data)
            request.dbsession.add(e)
            query = request.dbsession.query(Stock)
            #filter here for the correct userid ******
            all_stocks = query.all()
            return {'stocks': all_stocks}
        else:
            print('We you already have that in your database')
            return HTTPFound(location=request.route_url('stock'))



@view_config(route_name='stock-detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def get_portfolio_symbol_view(request):
    
    try:
        stock = request.matchdict['symbol']
    except (IndexError, KeyError):
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.symbol == stock)[0] # can also use .first() for first item
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'stock' : stock_detail}