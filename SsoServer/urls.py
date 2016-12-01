from django.conf.urls import url, include
from .views import SsoLoginView,SsoLogoutView

urlpatterns = [
    url(r'login/$', SsoLoginView.as_view(), name='login'),
    url(r'logout/$',SsoLogoutView.as_view(), name='logout'),
]

