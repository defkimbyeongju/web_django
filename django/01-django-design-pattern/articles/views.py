from django.shortcuts import render

# Create your views here.
def index(request): # request 인자는 약속임. 이게 안넘어오면 실행할 수가 없음. 프레임워크이기 때문에 이런 약속들이 많이 있음.
    return render(request, 'articles/index.html') # render 함수에서도 request는 약속임. 그 다음에 템플릿 경로를 설정. 
    