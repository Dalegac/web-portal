from django.urls import path
from . import views


urlpatterns = [
    path('competitions/', views.CompetitionsAPIView.as_view(), name="competitions-api-overview"),
    path('homecarousel/', views.HomeCarouselAPIView.as_view(), name="carousel-api-overview"),
    path('news/', views.NewsAPIView.as_view(), name="news-api-overview"),
    path('upcomingevents/', views.UpEventsAPIView.as_view(), name="upcomingevents-api-overview"),
    path('profile-selectlist/', views.ProfileSelectListAPIView.as_view(), name="profile-selectlist")
]
