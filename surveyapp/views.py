from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Question, Result
import json
from django.http import JsonResponse
from django.utils.safestring import mark_safe

# Create your views here.varshini

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def submit_survey(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            survey_data = data.get('survey_data', [])
            for entry in survey_data:
                question_id = entry['question_id']
                answer = entry['answer']
                question = Question.objects.get(id=question_id)
                result, created = Result.objects.get_or_create(question=question)
                if answer == 'yes':
                    result.yes_count += 1
                elif answer == 'no':
                    result.no_count += 1
                elif answer == 'not_interested':
                    result.not_interested_count += 1
                result.save()
            return JsonResponse({'message': 'Survey submitted successfully!'})
        except Exception as e:
            return JsonResponse({'Error!': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request!'}, status=400)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def result(request):
    results = Result.objects.select_related('question').all()
    results_data = json.dumps([
        {
            'question_id': result.question.id,
            'question_text': result.question.text,
            'yes_count': result.yes_count,
            'no_count': result.no_count,
            'not_interested_count': result.not_interested_count
        }
        for result in results
    ])
    results_data_safe = mark_safe(results_data)
    return render(request, 'result.html', {'results': results, 'results_data': results_data_safe})