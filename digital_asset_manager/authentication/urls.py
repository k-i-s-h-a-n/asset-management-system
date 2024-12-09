from django.urls import path
from .views import signup, signin
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
   
]



urlpatterns += [
    path('categories/', category_list_create, name='categories'),
    path('assets/', asset_list_create, name='assets'),
    path('assets/<int:id>/', asset_update_delete, name='asset_detail'),
]


