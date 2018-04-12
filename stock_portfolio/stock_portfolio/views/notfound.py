from pyramid.view import notfound_view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPFound


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return {}

# can also render the 404 template above for below error so that we don't
# giave anything away
@forbidden_view_config(renderer='../templates/404.jinja2')
def forbidden_view(request):
    request.response.status = 404
    return {}