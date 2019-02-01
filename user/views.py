from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def UserSignUp(request):

    if request.user.is_authenticated:
        """
            # If user is logged and if requested this url, write this event to log along with User's username and IP.
            
            # Redirect the user to homepage and send a message "Your are already registered and logged in."

        """
        return redirect('homepage:homepage-index')

    if request.method == 'POST':
        """
        Need to use django.form and cleaned_data
        """
        username = request.POST['phone']
        password = request.POST['password']
        email = request.POST['email']

        # first_name = request.POST['first_name']
        # if username not in database: create account

        try:
            user = User.objects.get(username=username)
            """
            # return a page with message you are already registered
            # provide two options 'Login' or 'Reset Password'
            """
            return HttpResponse('You are already registered, Please login.')
        except User.DoesNotExist:
            # Send OTP and Verify Phone Number
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage:homepage-index')

    else:
        return render(request, 'user/registration.html', {})


def LogOut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage:homepage-index')
    else:
        return HttpResponse('Invalid request!')


def Login(request):
    if request.method == 'POST':
        username = request.POST['phone']
        password = request.POST['password']
        current_url = request.POST['current_url']
        user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                # check if user have a redirect url
                x = reverse('login') + '?next='
                y = len(x)
                if x == current_url[:y]:
                    return redirect(current_url[y:])

                # if the user has logged in via pop-up.
                # Single page application need to be use in this case.
                # SPA will change the login button to profile dropdown without redirect.
                elif reverse('login') != current_url[:len(reverse('login'))]:
                    return redirect(current_url)

                # if the user has logged in via login page without a redirect url.
                else:
                    return redirect('homepage:homepage-index')
            else:
                # Show warning with base template
                return HttpResponse('Your account has been blocked, please contact help center')
        else:
            # Show warning Mobile No. or password is wrong
            return redirect('login')

    else:
        return render(request, 'user/login.html', )


def UserProfileView(request):
    return render(request, 'user/user_profile.html')




