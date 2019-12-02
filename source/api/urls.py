from  django.urls import path

from api.views import json_add_view, json_substract_view, json_multiply_view, json_divide_view

app_name = 'api_v1'

urlpatterns = [
    path('add/', json_add_view, name = 'add'),
    path('substract/', json_substract_view, name='substract'),
    path('multiply/', json_multiply_view, name='multiply'),
    path('divide/', json_divide_view, name='divide'),
]