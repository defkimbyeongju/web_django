from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

# 1. 로그인 페이지를 보여줘야 한다. : HTTP GET method
# 2. 실제 로그인 로직 : HTTP POST method
# 구분 어떻게?
def login(request):
    # POST: 실제 로그인 로직
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 == 세션ID 생성
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        # GET: 로그인 페이지
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, "accounts/login.html", context)

# 로그아웃
# 세션ID 삭제, 클라이언트에게 전달 x
def logout(request):
    auth_logout(request)
    return redirect("accounts:index")