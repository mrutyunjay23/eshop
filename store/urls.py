from django.urls import path
from .views import Index, signup, Login


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup', signup, name='signup'),
    path('login', Login.as_view(), name='login'),
]