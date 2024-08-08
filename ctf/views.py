import logging
import random
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .models import Challenge, Submission, UserProfile
from django.db import IntegrityError

def home(request):
    if request.user.is_authenticated:
        messages.info(request, f"Welcome back, {request.user.username}!")
        
        other_challenges = Challenge.objects.exclude(title__startswith='Vinegar')
        vinegar_challenges = Challenge.objects.filter(title__startswith='Vinegar')
        selected_vinegar_challenge = random.choice(vinegar_challenges) if vinegar_challenges.exists() else None

        challenges = list(other_challenges)
        if selected_vinegar_challenge:
            challenges.append(selected_vinegar_challenge)

        # Get the list of solved challenges for the logged-in user
        solved_challenges = Submission.objects.filter(user=request.user, is_correct=True).values_list('challenge', flat=True)

        leaderboard = UserProfile.objects.order_by('-total_points')
        user_profile = request.user.userprofile  # Fetch the user's profile to get their points

        return render(request, 'ctf/home.html', {
            'challenges': challenges,
            'solved_challenges': solved_challenges,  # Pass the solved challenges to the template
            'leaderboard': leaderboard,
            'user_profile': user_profile,  # Pass the user's profile to the template
        })
    else:
        messages.info(request, "Welcome to the RVU Santhe's MINICTF!")
        return render(request, 'ctf/home.html')


@login_required
def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)

    # Check if the challenge has already been solved by the user
    previous_submission = Submission.objects.filter(user=request.user, challenge=challenge, is_correct=True).exists()
    
    if previous_submission:
        messages.info(request, "You've already solved this challenge.")
        return redirect('submission_result', pk=challenge.pk)

    if request.method == 'POST':
        flag_submitted = request.POST.get('flag')
        messages.info(request, f"Flag submitted: {flag_submitted}")

        correct_flag = challenge.flag
        is_correct = flag_submitted == correct_flag

        if is_correct:
            user_profile = request.user.userprofile
            user_profile.total_points += challenge.points
            user_profile.save()
            messages.success(request, f"Correct flag! You earned {challenge.points} points.")
        else:
            messages.error(request, "Incorrect flag. Please try again.")

        # Create a submission entry only if the flag is correct
        if is_correct:
            Submission.objects.create(
                user=request.user,
                challenge=challenge,
                flag_submitted=flag_submitted,
                is_correct=is_correct,
                submission_time=timezone.now()
            )
        return redirect('submission_result', pk=challenge.pk)

    return render(request, 'ctf/challenge_detail.html', {'challenge': challenge})


@login_required
def submission_result(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    submissions = Submission.objects.filter(user=request.user, challenge=challenge)
    return render(request, 'ctf/submission_result.html', {'submissions': submissions})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request, f"Sign up successful! Welcome, {username}")
                return redirect('home')
            except IntegrityError as e:
                messages.error(request, "Sign up failed. This username or email may already be in use.")
        else:
            messages.error(request, "Sign up failed. Please correct the errors below.")
            for field in form.errors:
                messages.error(request, f"{field.capitalize()} error: {form.errors[field].as_text()}")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login successful! Welcome, {username}.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def leaderboard(request):
    # Order users by total points in descending order
    leaderboard = UserProfile.objects.order_by('-total_points')
    return render(request, 'ctf/leaderboard.html', {'leaderboard': leaderboard})

@login_required
def leaderboard_data(request):
    leaderboard = UserProfile.objects.order_by('-total_points').values('user__username', 'total_points')
    return JsonResponse(list(leaderboard), safe=False)

def logout_view(request):
    messages.info(request, f"Goodbye, {request.user.username}! You've been logged out.")
    auth_logout(request)
    return redirect('home')
