
from django.urls import path
from . import views
app_name='seriesapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('series/<int:series_id>/',views.detail,name='detail'),
    path('add/', views.add_series, name='add_series'),
    path('update/<int:id>/', views.update_series, name='update_series'),
    path('delete/<int:id>/', views.delete, name='delete')

]