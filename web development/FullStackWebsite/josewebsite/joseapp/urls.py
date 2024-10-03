# import view
from .views import home,index,umairurl,fruits,students
# import path

from django.urls import path
# import models

urlpatterns = [
    path('', home, name='home'),
    path('jose', index, name='jose'),
    path('umair', umairurl, name='umair'),
    path('fruits', fruits, name='fruits'),
    path('students',students, name='students'),
]