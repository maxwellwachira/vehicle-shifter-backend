import json
from starlette.config import Config
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter



config = Config('.env')
oauth = OAuth(config)

oauth.register(
    name='twitter',
    api_base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

router = APIRouter(
    prefix="/twitter", 
    tags=["Twitter Auth"]
)

@router.get('/')
async def homepage(request: Request):
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        html = (
            f'<pre>{data}</pre>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="login">login</a>')


@router.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.twitter.authorize_redirect(request, redirect_uri)


@router.get('/auth')
async def auth(request: Request):
    token = await oauth.twitter.authorize_access_token(request)
    url = 'account/verify_credentials.json'
    resp = await oauth.twitter.get(
        url, params={'skip_status': True}, token=token)
    user = resp.json()
    request.session['user'] = dict(user)
    return RedirectResponse(url='/')


@router.get('/logout')
async def logout(request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')
