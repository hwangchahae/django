from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer

def index(request):
    questions = Question.objects.order_by('-created_at')  # 질문을 생성시간 기준으로 내림차순
    return render(request, 'board/index.html', {'questions' : questions})



def detail(request, question_id):
    # question = Question.objects.get(id=question_id)  # 질문 객체 가져오기  
    question = get_object_or_404(Question, id=question_id)  # 질문 객체 가져오기, 없으면 404 에러 반환
    return render(request, 'board/detail.html', {'question': question})
