from rest_framework import serializers
from .models import Tweets, Profile

class TweetSerializer(serializers.ModelSerializer):
    posted_at = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField() 
    class Meta:
        model = Tweets
        fields = ['id', 'profile', 'tweet', 'posted_at', 'profile_image', 'user_name','likes','profile_id'] # this organizes the data bfr posting it

    def get_posted_at(self, obj):
        return obj.posted_at.strftime('%B %d, %Y at %I:%M %p')

    def get_profile_image(self, obj):
        return obj.get_profile_image()
    def get_username(self, obj):
        return obj.profile.user.username
    
    def get_profile_id(self, obj):  # Method to get the profile id
        return obj.profile_id


