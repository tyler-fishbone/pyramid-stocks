from pyramid.response import Response
from pyramid.view import view_config
from ..sample_data import MOCK_DATA
from sqlalchemy.exc import DBAPIError, IntegrityError
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED
from ..models import Stock
from . import DB_ERR_MSG
import requests
import json

from ..models import Stock
from ..models import Account

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
            query = request.dbsession.query(Account)
            instance = query.filter(Account.username == request.authenticated_userid).first()
            # query = request.dbsession.query(Stock)
            # user_stocks = query.filter(Stock.account_id == request.authenticated_userid)
        except DBAPIError:
            return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)
        if instance:
            print(instance)
            return {'stocks': instance.stock_id}
        else:
            return HTTPNotFound()


    # Get info from API
    if request.method == 'POST':
        if not all([field in request.POST for field in ['companyName', 'symbol', 'exchange', 'website', 'CEO', 'industry', 'sector', 'issueType', 'description']]):
            raise HTTPBadRequest

        query = request.dbsession.query(Account)
        instance = query.filter(Account.username == request.authenticated_userid).first()

        query = request.dbsession.query(Stock)
        second_instance = query.filter(Stock.symbol == request.POST['symbol']).first()

        if second_instance:
            second_instance.account_id.append(instance)
        else:
            new = Stock()
            new.account_id.append(instance)
            # new.account_id = request.authenticated_userid,
            new.companyName = request.POST['companyName']
            new.symbol = request.POST['symbol']
            new.exchange = request.POST['exchange']
            new.website = request.POST['website']
            new.CEO = request.POST['CEO']
            new.industry = request.POST['industry']
            new.sector = request.POST['sector']
            new.issueType = request.POST['issueType']
            new.description = request.POST['description']

            try:
                request.dbsession.add(new)
                request.dbsession.flush()
            except IntegrityError:
                pass
        return HTTPFound(location=request.route_url('portfolio'))

    return HTTPNotFound()


@view_config(route_name='stock-detail', renderer='../templates/stock-detail.jinja2', request_method='GET')
def get_portfolio_symbol_view(request):
    
    try:
        stock = request.matchdict['symbol']
    except (IndexError, KeyError):
        raise HTTPNotFound()

    try:
        query = request.dbsession.query(Stock)
        stock_detail = query.filter(Stock.account_id == request.authenticated_userid).filter(Stock.symbol == stock).one_or_none()
    
        if stock_detail is None:
            raise HTTPNotFound()

    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)


    return {'stock' : stock_detail}