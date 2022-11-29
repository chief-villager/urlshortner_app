from django.urls import path
from . import views

app_name = 'shortner'



urlpatterns = [

    path('',views.index_view,name = 'index'),
    path('create',views.create_view,name='create'),
    path('<str:pk>',views.go_view,name='go')

]