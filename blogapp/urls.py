from django.urls import path
from .import views



urlpatterns=[
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('addct/',views.addct,name='addct'),
    path('sign',views.sign,name='sign'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
