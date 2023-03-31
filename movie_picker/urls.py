from django.urls import path
from . import views

urlpatterns = [
    path('moviepicker', views.MovieList.as_view(),name='movie_list'),
    path('moviepicker/<int:pk>',views.MovieDetail.as_view(),name='movie_detail')
]