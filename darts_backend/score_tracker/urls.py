from django.urls import path
from score_tracker.views import scores, score_detail

# define the urls
urlpatterns = [
    path('scores/', scores),
    path('scores/<int:pk>/', score_detail),
]