from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    followers = models.PositiveIntegerField(default=0)
    followed_by =models.ManyToManyField(User, related_name='current_followers', blank=True)




    def __str__(self):
        return self.user.username # used for the djnago template can use it and makes it readable for us

class Tweets(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) #conncts to the profile calss so i can acces porifle user and pfp
    tweet = models.CharField(max_length=100) # wt the user is tweeting
    posted_at = models.DateTimeField(auto_now_add=True) #date when posted(using servertime)
    user_name= models.CharField(max_length=29)
    likes = models.PositiveIntegerField(default=0) #store how many likes
    liked_by = models.ManyToManyField(User, related_name='liked_tweets', blank=True) # this is jsut used to store data of users that liked the tweet




    def __str__(self):
        return self.user_name # used for  the djnago template can use it and makes it readable for us


    def get_profile_image(self):
        return self.profile.profile_image.url if self.profile.profile_image else None # used for the djnago template can use it and makes it readable for us

