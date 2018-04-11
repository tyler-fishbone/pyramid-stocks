from pyramid.response import Response
from pyramid.view import view_config
from ..sample_data import MOCK_DATA
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import NO_PERMISSION_REQUIRED
from ..models import Stock
from . import DB_ERR_MSG
import requests
import json

# API_URL = 'https://api.iextrading.com/1.0'

@view_config(route_name='base', renderer='../templates/base.jinja2', request_method='GET')
def get_base_view(request):
    return Response('base view is functional')

@view_config(route_name='home', renderer='../templates/index.jinja2', request_method='GET', permission=NO_PERMISSION_REQUIRED)
def get_home_view(request):
    # need to add permision here somehow
    return {}


# @view_config(route_name='auth', renderer='../templates/auth.jinja2')
# def get_auth_view(request):
#     if request.method == 'GET':
#         try:
#             username = request.GET['username']
#             password = request.GET['password']
#             print('User: {}, Pass: {}'.format(username, password))

#             return HTTPFound(location=request.route_url('portfolio'))

#         except KeyError:
#             return {}
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

#         return HTTPFound(location=request.route_url('portfolio'))

#     return HTTPNotFound()


# @view_config(route_name='stock', renderer='../templates/stock-add.jinja2')
# def get_stock_add_view(request):
    
#     if request.method == 'GET':
#         try:
#             symbol = request.GET['symbol']

#         except KeyError:
#             return {}

#         try:
#             response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
#             data = response.json()
#             return {'company': data}
#         except ValueError:
#             print('That stock does not exist')
#             return HTTPFound(location=request.route_url('stock'))
        

# @view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2')
# def get_portfolio_view(request):
    
#     if request.method == 'GET':
#         try:
#             query = request.dbsession.query(Stock)
#             all_stocks = query.all()
#         except DBAPIError:
#             return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)
        
#         return {'stocks': all_stocks}

#     # Get info from API
#     if request.method == 'POST':
#         symbol = request.POST['symbol']
#         response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
#         data = response.json()

#         # Check if info already DB
#         my_object = request.dbsession.query(Stock).filter(Stock.symbol == data['symbol']).first()
#         if not my_object:
#             e = Stock(**data)
#             request.dbsession.add(e)
#             query = request.dbsession.query(Stock)
#             all_stocks = query.all()
#             return {'stocks': all_stocks}
#         else:
#             print('We you already have that in your database')
#             return HTTPFound(location=request.route_url('stock'))



# @view_config(route_name='stock-detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
# def get_portfolio_symbol_view(request):
    
#     try:
#         stock = request.matchdict['symbol']
#     except IndexError:
#         return HTTPNotFound()

#     try:
#         query = request.dbsession.query(Stock)
#         stock_detail = query.filter(Stock.symbol == stock)[0] # can also use .first() for first item
#     except DBAPIError:
#         return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

#     return {'stock' : stock_detail}

    # # Cool method querying another API
    #     res = requests.get('https://pixabay.com/api?key={}&q={}'.format(
    #         API_KEY, entry_detail.title.split(' ')[0]))

    # for stock_item in MOCK_DATA:
    #     if stock_item['symbol'] == stock:
    #         return {'stock' : stock_item}
    # return {}

