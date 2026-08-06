from django.urls import path
from .views import UserView, TierView


urlpatterns = [
  path("users/", UserView.as_view(), name= "user-list" ),
  path("users/<int:id>/", UserView.as_view(), name="user-details"),
  path("tiers/", TierView.as_view(), name= "tier-list" ), 

]