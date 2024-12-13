from django.template.defaulttags import url
from django.urls import path

from accounts.views import register_view, login_view, email_verification_view

urlpatterns = [
    path('accounts/register/', register_view, name='signup'),
    path('accounts/login/', login_view, name='signin'),
    path('accounts/verify_email/', email_verification_view, name='e_verify'),
    url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ActivateAccountView.as_view(), name='activate_account'),
]
