from django.urls import path

from transfers.views import redirect_views


urlpatterns = [
     path('login-redirect/', redirect_views.login_redirect_view),
]
