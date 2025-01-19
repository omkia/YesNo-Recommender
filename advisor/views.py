from .models import Activity
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from .models import UserActivity
import random


def questionnaire(request):
    if request.method == 'POST':
        # Get answers from the form
        joint_pain = request.POST.get('joint_pain') == 'yes'
        sedentary = request.POST.get('sedentary') == 'yes'
        back_pain = request.POST.get('back_pain') == 'yes'
        stress = request.POST.get('stress') == 'yes'
        cardio = request.POST.get('cardio') == 'yes'
        answers = {
            "joint_pain" : request.POST.get('joint_pain'),
        "sedentary" : request.POST.get('sedentary') ,
        "back_pain" : request.POST.get('back_pain'),
        "stress" : request.POST.get('stress') ,
        "cardio": request.POST.get('cardio'),
        }
        # Simple recommendation logic
        activities = []

        if joint_pain:
            activities.extend(['Swimming', 'Water Aerobics', 'Stationary Cycling'])

        if sedentary:
            activities.extend(['Walking', 'Standing Desk Exercises', 'Office Stretching'])

        if back_pain:
            activities.extend(['Core Strengthening', 'Yoga', 'Pilates'])

        if stress:
            activities.extend(['Yoga', 'Tai Chi', 'Walking Meditation'])

        if cardio:
            activities.extend(['Brisk Walking', 'Swimming', 'Cycling'])

        if not activities:
            activities = ['Walking', 'Basic Stretching', 'Light Yoga']

        # Remove duplicates and select random activity
        activities = list(set(activities))
        recommended = random.choice(activities)
        save_activity(request, "health", answers, recommended)
        return render(request, 'advisor/result.html', {'activity': recommended})

    return render(request, 'advisor/questionnaire.html')


def gift_advisor(request):
    if request.method == 'POST':
        answers = {
            'mobility': request.POST.get('mobility'),
            'content_creation': request.POST.get('content_creation'),
            'audio': request.POST.get('audio'),
            'environment': request.POST.get('environment'),
            'social_music': request.POST.get('social_music'),
            'health_tracking': request.POST.get('health_tracking'),
            'smart_watch': request.POST.get('smart_watch'),
        }

        # Enhanced gift recommendation logic
        if answers['mobility'] == 'yes':
            recommendation = {
                'item': 'High-Capacity Power Bank',
                'description': 'A premium 20000mAh power bank with fast charging capability, multiple ports, and compact design.',
                'features': ['Fast charging technology', 'Multiple device charging', 'LED power indicator',
                             'Compact and portable'],
                'suggestions': ['Anker PowerCore 20000', 'Mophie Powerstation XXL', 'RavPower Portable Charger'],
                'price_range': '$40-$80'
            }
        elif answers['content_creation'] == 'yes':
            recommendation = {
                'item': 'Portable Mini Projector',
                'description': 'A compact HD projector perfect for sharing photos, videos, and creating immersive viewing experiences.',
                'features': ['1080p resolution', 'Built-in speakers', 'Wireless connectivity', 'Long battery life'],
                'suggestions': ['Anker Nebula Capsule', 'Kodak Luma 350', 'ViewSonic M1+'],
                'price_range': '$200-$400'
            }
        elif answers['audio'] == 'yes' and answers['environment'] == 'yes':
            recommendation = {
                'item': 'Noise-Cancelling Headphones',
                'description': 'Premium over-ear headphones with active noise cancellation for immersive listening experience.',
                'features': ['Active noise cancellation', 'Long battery life', 'Comfortable fit', 'High-quality sound'],
                'suggestions': ['Sony WH-1000XM4', 'Bose QuietComfort 35 II', 'Sennheiser Momentum 4'],
                'price_range': '$250-$400'
            }
        elif answers['audio'] == 'yes':
            recommendation = {
                'item': 'Premium Wireless Earbuds',
                'description': 'Compact wireless earbuds with excellent sound quality and convenient features.',
                'features': ['Touch controls', 'Wireless charging case', 'Water resistance', 'Voice assistant support'],
                'suggestions': ['Apple AirPods Pro', 'Sony WF-1000XM4', 'Samsung Galaxy Buds Pro'],
                'price_range': '$150-$250'
            }
        elif answers['social_music'] == 'yes':
            recommendation = {
                'item': 'Portable Bluetooth Speaker',
                'description': 'Powerful portable speaker with rich sound and party-ready features.',
                'features': ['Water resistance', 'Long battery life', 'Party lights', 'Multi-speaker pairing'],
                'suggestions': ['JBL Charge 5', 'Ultimate Ears BOOM 3', 'Sony SRS-XB43'],
                'price_range': '$120-$200'
            }
        elif answers['health_tracking'] == 'yes':
            recommendation = {
                'item': 'Advanced Fitness Tracker',
                'description': 'Comprehensive health and fitness tracking device with advanced metrics.',
                'features': ['Heart rate monitoring', 'Sleep tracking', 'GPS', 'Water resistance'],
                'suggestions': ['Fitbit Charge 5', 'Garmin Vivosmart 4', 'Samsung Galaxy Fit2'],
                'price_range': '$100-$180'
            }
        elif answers['smart_watch'] == 'yes':
            recommendation = {
                'item': 'Hybrid Smartwatch',
                'description': 'Elegant timepiece combining traditional design with smart features.',
                'features': ['Classic design', 'Activity tracking', 'Notification display', 'Long battery life'],
                'suggestions': ['Withings ScanWatch', 'Garmin Vivomove', 'Fossil Hybrid HR'],
                'price_range': '$200-$350'
            }
        else:
            recommendation = {
                'item': 'Designer Power Bank',
                'description': 'Stylish portable charger with unique designs and reliable charging capabilities.',
                'features': ['Custom designs', 'Compact size', 'Fast charging', 'Multiple ports'],
                'suggestions': ['Native Union Jump+', 'iDeal of Sweden Power Bank', 'Ted Baker Power Bank'],
                'price_range': '$50-$100'
            }
        save_activity(request, "gift", answers, recommendation)
        return render(request, 'advisor/gift_result.html', {'recommendation': recommendation})

    return render(request, 'advisor/gift_advisor.html')




def home(request):
    return render(request, 'advisor/home.html')

def about(request):
    return render(request, 'advisor/about.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('advisor:home')
        messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'advisor/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('advisor:home')
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'advisor/login.html', {'form': form})

@login_required
def recommendations(request):
    user_activities = UserActivity.objects.filter(user=request.user)
    return render(request, 'advisor/recommendations.html', {'activities': user_activities})

# Update your existing views to save activities when logged in
def save_activity(request, activity_type, answers, recommendation):
    if request.user.is_authenticated:
        UserActivity.objects.create(
            user=request.user,
            activity_type=activity_type,
            answers=answers,
            recommendation=recommendation
        )