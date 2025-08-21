from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback, Teacher
# Create your views here.


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/thank_you.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})


@login_required
def teacher_feedback(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
        feedbacks = Feedback.objects.filter(teacher=teacher)
    except Teacher.DoesNotExist:
        feedbacks = Feedback.objects.none()
    return render(request, 'feedback/teacher_feedback.html', {'feedbacks': feedbacks})


@login_required
def director_feedback(request):
    if request.user.is_superuser:
        feedbacks = Feedback.objects.all()
    else:
        feedbacks = Feedback.objects.none()
    return render(request, 'feedback/director_feedback.html', {'feedbacks': feedbacks})
