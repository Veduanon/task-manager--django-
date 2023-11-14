from django.urls import path

from kinotower.views import index

app_name = 'kinotower'

urlpatterns = [

path('', index, name='index')

]