from django.urls import path
from .views import get_student_details, get_single_student
from .views import MovieListAV, SingleMovieAV
from .views import AddressListAV
urlpatterns = [
    path('list/', get_student_details, name='student_list'),
    path('<int:pk>/', get_single_student, name='single-student'),
    path('list1/', MovieListAV.as_view(), name='student_list_av'),
    path('av/<int:id>/', SingleMovieAV.as_view(), name='single-student-av'),

    path('address/', AddressListAV.as_view(), name='address-list'),
]
