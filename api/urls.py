from django.urls import path
from .views import *

urlpatterns = [
    path("quiz",QuizView.as_view()),
    path("category",CategoryView.as_view())
]
