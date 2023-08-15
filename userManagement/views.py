from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signupfunc(request):
    user2 = User.objects.all()
    print(user2)
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('signup')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'login.html')