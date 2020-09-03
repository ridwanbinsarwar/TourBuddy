from django.shortcuts import render, redirect
from .forms import RegistrationForm
from accounts import services


# Create your views here.


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        # creating json representation to call api method
        data = {"email": form.data['email'],
                "password": form.data['password'],
                "password2": form.data['password2'],
                }
        # api call method
        response = services.register_user_api(data)

        # add fields errors
        # No need to add email field errors manually
        # because ModelForm is used
        if response.status_code == 400:
            try:
                # get error message from response
                error = response.json()["password"]
                form.add_error('password', error)
            except KeyError:
                if form.has_error('email') is False:
                    # in case of unknown errors
                    form.add_error(None, "weird shit happened")
            return render(request, 'registration.html', {'form': form})
        return redirect('registration_view')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == 'POST':
        # form = Top_List_Form(request.POST)
        # creating json representation to call api method
        data = {"email": request.POST['email'],
                "password": request.POST['pass'],
                }
        # api call method
        response = services.login_user_api(data)
        print(response.json())
        if response.status_code != 400:
            # authentication success

            token = response.json()["token"]
            email = response.json()["email"]
            request.session['token'] = token
            request.session['user'] = email

            return redirect("view_profile")
    return redirect("login_view")
