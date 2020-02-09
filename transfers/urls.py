from django.urls import path

from transfers.views import redirect_views, form_view


urlpatterns = [
     path('login-redirect/', redirect_views.login_redirect_view),
     path('PS2TS/',  form_view.PS2TSFormView.as_view()),
     path('TS2PS/',  form_view.TS2PSFormView.as_view()),
]
