from  django.urls import path

from webapp.views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView, name='expression'),
]