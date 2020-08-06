from django.shortcuts import render, redirect
from profiles import services, models


# Create your views here.


def view_profile(request):

    token = services.get_token_from_request(request)
    if token == "unauthorized":
        # user not logged in , redirect user to login page
        return redirect('login_view')

    if request.method == "GET":

        profile = services.get_profile_api(token)

        return render(request, 'profile.html', {'profile': profile})

    elif request.method == "POST":
        data = {"first_name": request.POST['first_name'],
                "last_name": request.POST['last_name'],
                "phone_number": request.POST['phone_number'],
                "age": request.POST['age'],
                "gender": request.POST['gender'],

                }
        print(data)
        # change gender data format to make it api compatible
        data['gender'] = data['gender'][0]
        response = services.update_profile_api(json_data=data, token=token)

        return redirect('view_profile')
