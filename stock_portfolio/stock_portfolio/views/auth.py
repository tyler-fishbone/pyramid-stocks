from pyramid.response import Response
from pyramid.view import view_config
# from ..sample_data import MOCK_DATA
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPUnauthorized, HTTPBadRequest
from pyramid.security import NO_PERMISSION_REQUIRED, remember, forget
from pyramid.response import Response
from ..models import Account
from . import DB_ERR_MSG
import requests



@view_config(route_name='auth', renderer='../templates/auth.jinja2', permission=NO_PERMISSION_REQUIRED)
def get_auth_view(request):
    
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HTTPBadRequest()

        try:
            instance = Account(
                username=username,
                email=email,
                password=password,
            )
            headers = remember(request, userid=instance.username)
            request.dbsession.add(instance)
            return HTTPFound(location=request.route_url('portfolio'), headers=headers)
        
        except DBAPIError:
            return Response(DB_ERR_MSG, content_type='text/plain', status=500)
        # print('User: {}, Pass: {}, Email: {}'.format(username, password, email))
    return HTTPNotFound()


    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            # print('User: {}, Pass: {}'.format(username, password))

        except KeyError:
            return {}
        
        is_authenticated = Account.check_credentials(request, username, password)
        if is_authenticated[0] == True:
            headers = remember(request, userid=username)
            return HTTPFound(location=request.route_url('portfolio'), headers=headers)
        else:
            return HTTPUnauthorized()
        
    return HTTPFound(location=request.route_url('home'))


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)