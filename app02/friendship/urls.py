from django.urls import path
from . import views
#from .views import ProfileListView, ProfileDetailView

friendship_patterns = ([
    #path('', ProfileListView.as_view(), name='list'),
    #path('<username>/', ProfileDetailView.as_view(), name='detail'),
    path('friend_request/',views.friendrequest_list, name='friendrequest_list'),
    path('friend_list/',views.friend_list, name='friend_list'),
    path('accept_request/<int:id>/',views.accept_request, name='accept_request'),
    path('decline_request/<int:id>/',views.decline_request, name='decline_request'),
    path('delete_friend/<int:id>/',views.delete_friend, name='delete_friend'),
], "friendship")
