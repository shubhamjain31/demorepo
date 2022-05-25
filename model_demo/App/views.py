from django.shortcuts import render, redirect

from .models import *
import datetime, json

# Create your views here.

def index(request):
    if request.method == "POST":
        title                    = request.POST.get('title')
        
        MyModel.objects.create(title=title, start_time=datetime.datetime.now())
    return render(request, 'index.html')


def information(request):
    if request.method == "POST":
        information_name                = request.POST.get('information_name')
        skills                          = request.POST.getlist('skills')
        images                          = request.FILES.getlist('images')
        print(images)

        information_obj = Informations.objects.create(information_name=information_name)

        count = 1
        skills_list = []

        for skill in skills:
            skills_list.append({str(count): skill})
            count += 1

        information_obj.json_text_field = json.dumps(skills_list)
        information_obj.save()

        for image in images:
            Images.objects.create(information=information_obj, image=image)

        
        return redirect('/information/')
    return render(request, 'information.html')


def show_info(request, id):
    context = {}
    try:
        information_obj = Informations.objects.get(id = id)
        images = Images.objects.filter(information=information_obj)
        context['information_obj'] = information_obj
        context['images'] = images

    except Exception as e:
        print(e)

    return render(request, 'show_information.html', context)


# ================================================================================ @Practice@ =============================================================================
from django.http import HttpResponse
from django.db.models import Sum, Avg, Min, Max
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.db import connection
from django.db.models import Prefetch
from django.db import reset_queries


def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results
    return inner_func

def quiz_(request):

    # fee_count           = Quiz.objects.aggregate(Sum('fee'))
    # discount_count      = Quiz.objects.annotate(discount_int=Cast('discount', IntegerField())).aggregate(Sum('discount_int'))
    # discount_avg        = Quiz.objects.annotate(discount_int=Cast('discount', IntegerField())).aggregate(Avg('discount_int'))
    # obj                 = Quiz.objects.values()

    # quiz_by_language    = Question.objects.values('quiz__name').annotate(Sum('id'))
    # aa                  = Question.objects.select_related('quiz').get(pk=1).quiz.name

    # all_questions         = Question.objects.select_related('quiz')

    # for ques in all_questions:
    #     print(ques.quiz.name)
    # all_questions         = Question.objects.all().prefetch_related('options')
    with_prefetch_related_advanced()
    return HttpResponse('<h1>Success</h1>')

@database_debug
def without_prefetching():
    # questions = Question.objects.all()
    # questions = Question.objects.select_related('quiz').all()

    questions = Question.objects.prefetch_related('quiz').all()
    return [question.quiz.name for question in questions]

@database_debug
def with_prefetch_related_advanced():
    # not optimize
    quizzes = Quiz.objects.prefetch_related('questions')
    objective_questions_count = {}
    for quiz in quizzes:
        objective_questions_count[quiz.name] = quiz.questions.filter(question_type=Question.OBJECTIVE).count()
    

    # optimize
    quizzes = Quiz.objects.prefetch_related(Prefetch('questions', queryset=Question.objects.filter(question_type=Question.OBJECTIVE)))
    objective_questions_count = {}
    for quiz in quizzes:
        objective_questions_count[quiz.name] = quiz.questions.count()
    return objective_questions_count