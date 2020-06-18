from django.urls import path

from accounts.views import signup, list_member

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('members/list/', list_member, name="list-member"),
]