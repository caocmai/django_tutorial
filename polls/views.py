from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # return HttpResponse("Hello, world. You're at the polls index.")

# This has to be question_id inorder for function to work
def detail(request, question_id):
    thing = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": thing})
   
    # return HttpResponse(f"You're looking at question {question_id}")


def results(requset, question_id):
    response = (f"You're looking at the results of question {question_id}")
    # Note sure if below is correct syntax
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")