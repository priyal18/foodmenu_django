from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/',views.DetailClassView.as_view(),name='detail'),
    path('item/',views.items,name='item'),
    path('add/',views.CreateClassView.as_view(),name="create_item"),
    path('update/<int:id>/',views.update_item,name="update_item"),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),

]
