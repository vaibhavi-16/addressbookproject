from django.contrib import admin
from django.urls import path
from.views import *

app_name = 'Library'


urlpatterns = [
    path('home/', addata,name='addata'),
    # path('show_squad/',show_squad, name='addshow'), 
    path('delete_data/<int:id>/',delete_data, name='delete_data'), 
    path('<int:id>/',update_data, name='update_data'),
]