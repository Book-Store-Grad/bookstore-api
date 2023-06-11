from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html

def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.29.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.29.0/swagger-ui.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch


app = FastAPI()

oauth_schema = OAuth2PasswordBearer(tokenUrl='auth')
