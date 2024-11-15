from django.urls import path
from .views import GetJokeView

urlpatterns = [
    path('get-jokes/',GetJokeView.as_view(),name = 'get-jokes')
]