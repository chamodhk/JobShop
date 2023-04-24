from django.urls import path
from .views import HomeJobView,SearchResultsListView,JobView

urlpatterns = [
    path("",HomeJobView.as_view(),name="home_jobs"),
    path("search/",SearchResultsListView.as_view(),name="search_results"),
    path("job/<int:pk>/",JobView,name="job_view"),
]