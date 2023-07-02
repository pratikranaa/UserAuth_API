from django.urls import path, include, re_path
from login_api.views import *


urlpatterns = [
    path('request-reset-email/', request_reset_email, name = 'request-reset-email'),
    re_path(r"^reset-password/(?P<uid>[-\w]+)_(?P<token>[-\w]+)/", resetPassword, name="reset-password")
]