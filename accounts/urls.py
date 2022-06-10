from django.urls import path, include
from .views import SignupPageView, UserProfile

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),

    path('user/', UserProfile.as_view(), name="user_profile"),
    path('car/', include('user_auto.urls')),
]