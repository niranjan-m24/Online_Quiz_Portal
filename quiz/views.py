
from django.shortcuts import render
from .models import Question, Result
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'quiz/home.html')

@login_required
def quiz_view(request):
    questions = Question.objects.all()
    score = 0
    if request.method == "POST":
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_option:
                score += 1
        Result.objects.create(user=request.user, score=score)
        return render(request, 'quiz/result.html', {'score': score})
    return render(request, 'quiz/quiz.html', {'questions': questions})
