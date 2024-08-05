from django.http import JsonResponse
from .models import Tweets, Profile
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ProfilePictureForm
from django.contrib.auth.models import User
@api_view(['GET', 'POST', 'DELETE'])
@login_required(login_url='/')
def tweet_list(request, format=None):
    if request.method == 'GET':  # print all current tweets
        all_tweets = Tweets.objects.all() #gets all tweets
        serializer = TweetSerializer(all_tweets, many=True) #seralizes them with the serealizeer file
        profile = get_object_or_404(Profile, user=request.user) #gets current user
        return render(request, 'tweets.html', {'tweets': serializer.data, 'profile':profile}) #passes the seralized and proifle data so htmlfile can use it
    
    elif request.method == 'POST': #prints new tweet
        user = request.user #gets current user
        tweet_text = request.POST.get('tweet') #gets tweet
        profile = get_object_or_404(Profile, user=request.user) #gets current proifle
        new_tweet = { # the data has to be passes as a dict so this si it
            'profile': profile.id,
            'tweet': tweet_text,
            'user_name': user.username #user is a n object to acces the string veriosn of the user u use user.username
        }
        serializer = TweetSerializer(data=new_tweet) #the dict is apssed to be orgainzed by serialzer file
        if serializer.is_valid():
            serializer.save() #saves it to data basae
            return redirect('tweets')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #else an error happened 
       
    
@api_view(['GET', 'PUT', 'DELETE'])
def tweet_detail(request, id, format=None):
    try:
        tweet = Tweets.objects.get(pk=id)
    except Tweets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TweetSerializer(tweet)
        return render(request, 'tweets.html', {'tweets': [serializer.data]})

    elif request.method == 'PUT':
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST']) # this repsents delete cuz html only takes post and put
def tweet_delete(request, id, format=None):
    try:
        tweet = Tweets.objects.get(pk=id) # gets current id of tweet
    except Tweets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    tweet.delete() 
    return redirect('tweets')#delete tweet and redirect to tweets page (to find tweet page url go tourls file and look for "name= "tweets")

def user_logout(request):
    logout(request) 
    return redirect('/') #logs out current suer and sends abck to login screen

def profile_page(request):
    if request.method == 'GET':
        return render(request, 'profile.html') #this is to render the proifle update page

def update_profile(request): # this is to update pfp of curret user
    if request.method == 'POST': # these "post" r a key word apssed from djano n r important kinda like a tracer
        new_img = request.FILES.get("profile_img") #takes the input fiel from html file 
        profile = Profile.objects.get(user=request.user) #gets current insatnce of the profile calss ex les say sahil is the profile and user and profile:img are under its variabels
        profile.profile_image = new_img #sets new pfp as the curret users pfp
        profile.save() #saves file and redriects to tweets page
        return redirect('tweets')
    return render(request, 'profile.html') # this is there so i dont get error doesnt rlly do anything

def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweets, pk=tweet_id) ##gets tweet id if it dont exsit gives eror code 404
    user = request.user

    # Check if the user has already liked the tweet
    if tweet.liked_by.filter(pk=user.pk).exists(): #checks the tweet.liked_whic stores users that arldy liked thw tweet. if user there it unlike else it likes
        # Unlike the tweet
        tweet.likes -= 1 #removes a like form the tweet
        tweet.liked_by.remove(user) #removes user from liked accounts from the tweet
    else:
        # Like the tweet
        tweet.likes += 1 #adds a like tot weet
        tweet.liked_by.add(user)# adds user to liked account for the tweet

    tweet.save() #saves tweet
    return redirect('tweets') #redirects to tweets page


def to_account_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    tweets = Tweets.objects.filter(profile=profile)
    followed_users = profile.followed_by.all()  # Query followed users directly from the profile
    all_users = User.objects.all()
    all_usernames = list(all_users.values_list('username', flat=True))
    
    return render(request, 'account _profile.html', {
        'tweets': tweets,
        'profile': profile,
        'profile_id': profile_id,
        'followed_users': followed_users,  # Pass followed users to the template
        'all_users' : all_users,
        'all_usernames': all_usernames,
    })


     
   


def follow(request, account_id):
    
    
    account_profile = get_object_or_404(Profile, id=account_id)
    user = request.user  

   
    if account_profile.followed_by.filter(pk=user.pk).exists(): 
       
        account_profile.followers-= 1 
        account_profile.followed_by.remove(user) 
    else:
        
        account_profile.followers += 1 
        account_profile.followed_by.add(user)

   
    account_profile.save()

    return redirect('to_account_profile', profile_id=account_id) 
    


    