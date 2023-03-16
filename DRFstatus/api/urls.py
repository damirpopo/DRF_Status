from django.urls import path
from api.views import *

urlpatterns = [
    path('order/', order_list),
    path('order/<int:pk>',order_detail),
    path('status/', Status_list),
    path('status/<int:pk>', Status_detail),
    path('workers/', Workers_list),
    path('workers/<int:pk>', Workers_detail),
    path('titleJob/', titleJob_list),
    path('titleJob/<int:pk>', TitleJob_detail),
]