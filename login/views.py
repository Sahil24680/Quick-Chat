from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect  # Import HttpResponseRedirect
from django.contrib.auth.models import User
from logic.models import  Profile

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username") #gets user frok front end hml file
        password = request.POST.get("password")#gets pass frok front end hml file
        user = authenticate(request, username=username, password=password) # cheks  database for if he user and pass matches any in the accounts regestry
        if user is not None:
            login(request, user)
            return redirect("tweets") # if it is valid it log u in and redircts u to twees page (name if the url)
        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponseRedirect(request.path_info)  # Redirect to the same page
    else:
        return render(request, 'registration/login.html', {}) #this is so if he user does nothign it just stays in that page by deuqalft djanogo also
    #epxects the tmepalte for login to be within registration folder in the tempalet so tmepalte/registraion/login.html

def lol(request):
    return redirect("tweets") # this is cuz of danjo defuatl setting when the login is false first and correct after it auto looks for accounts/profile
#so is used this to jsut redirect that back to the tweets urls
def new_user(request):
    return render (request,'create_user.html') # this is to render the create page



def make_newuser(request):
        if request.method == 'POST':
            username = request.POST.get('new_username')
            email = request.POST.get('new_gmail')
            password = request.POST.get('new_password') #this is to create a new user
            default_profile_pic_path = 'defaults/male.jpg'  # Adjust the path as per your directory structure
            
        # Create the user
        try:
            user = User.objects.create_user(username, email, password) # this creates the new user and adds to database
            
            # Create profile with default profile image
            profile = Profile.objects.create(user=user, profile_image=default_profile_pic_path)
            
            messages.success(request, 'User created successfully!')
            return redirect('login')  # Redirect to the login page after successful registration
        except Exception as e:
            messages.error(request, f'Error creating user: {e}')

        return render(request, 'registration/register.html') # ignore this, this is just there so I don't get an error