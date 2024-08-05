from django.contrib import admin
from django.urls import path
from logic import views
from rest_framework. urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #url for admin stie
    path('tweets/',views.tweet_list,name ='tweets'),#url for tweets page
    #path('tweets/<int:id>',views.tweet_detail),
    path('tweets/delete/<int:id>/', views.tweet_delete, name='tweet_delete'),#url for delete individual tweet in all of these the name patters tahts wt html uses to connect to the url page whon conencts to the view through the views.(wtv ur funciton name is) 
    path('logout/', views.user_logout, name='log_out'), #logout url
    path('new_profile/', views.profile_page, name='profile-page'), #this for the page where u upolad file for new pfp
    path('update_profile/', views.update_profile, name='update_profile'), # just there to connect html to view function this is where the pfp is changed
    path('tweets/like/<int:tweet_id>/', views.like_tweet, name='like_tweet'), # used to connect the likes to the view function
    path('tweets/accounts/profile/<int:profile_id>/', views.to_account_profile, name='to_account_profile'), #url formaccount url page
    path('tweets/accounts/profile/account/<int:account_id>/', views.follow, name='follow'),

]

