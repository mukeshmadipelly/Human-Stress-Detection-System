from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, AuthenticationForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def supportpage(request):
    return render(request, 'support.html')

def signuppage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Adjust this if your form field is 'email' or 'username'
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dataentry')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, AuthenticationForm
from .models import HealthData, predict_stress

@login_required
def dataentrypage(request):
    if request.method == 'POST':
        heart_rate = float(request.POST['heart_rate'])
        snoring_rate = float(request.POST['snoring_rate'])
        respiratory_rate = float(request.POST['respiratory_rate'])
        body_temperature = float(request.POST['body_temperature'])
        limb_movements = float(request.POST['limb_movements'])
        blood_oxygen = float(request.POST['blood_oxygen'])
        eye_movement = float(request.POST['eye_movement'])
        sleep_hours = float(request.POST['sleep_hours'])
        
        # Parameters in the required order
        parameters = [heart_rate, snoring_rate, respiratory_rate, body_temperature, limb_movements, blood_oxygen, eye_movement, sleep_hours]
        
        # Use the model to predict stress
        stress_result = predict_stress(parameters)
        
        # Save the data to the database
        HealthData.objects.create(
            user=request.user,
            heart_rate=heart_rate,
            snoring_rate=snoring_rate,
            respiratory_rate=respiratory_rate,
            body_temperature=body_temperature,
            limb_movements=limb_movements,
            blood_oxygen=blood_oxygen,
            eye_movement=eye_movement,
            sleep_hours=sleep_hours,
            result=stress_result
        )
        
        return render(request, 'result.html', {'stress_result': stress_result})
    return render(request, 'dataentry.html')


def analyze_parameters(heart_rate, snoring_rate, respiratory_rate, body_temperature, limb_movements, blood_oxygen, eye_movement, sleep_hours):
    # Normal ranges
    normal_ranges = {
        'heart_rate': (60, 100),
        'snoring_rate': (10, 15),
        'respiratory_rate': (12, 15),
        'body_temperature': (15, 32),
        'limb_movements': (90, 110),
        'blood_oxygen': (95, 100),
        'eye_movement': (90, 120),
        'sleep_hours': (7, 8),
    }

    # Check if parameters are within normal ranges
    params = {
        'heart_rate': heart_rate,
        'snoring_rate': snoring_rate,
        'respiratory_rate': respiratory_rate,
        'body_temperature': body_temperature,
        'limb_movements': limb_movements,
        'blood_oxygen': blood_oxygen,
        'eye_movement': eye_movement,
        'sleep_hours': sleep_hours,
    }

    for param, value in params.items():
        min_range, max_range = normal_ranges[param]
        if not (min_range <= value <= max_range):
            return "Stressed"

    return "Not Stressed"


def resultpage(request):
    return render(request, 'result.html')

def profilepage(request):
    return render(request, 'profile.html')


