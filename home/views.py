
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm,NewQuestionForm,NewResponseForm,NewReplyForm
from .models import Question,Response

def index(request):
    context={"variable":"this is sent"}
    return render(request,'index.html')
    #return HttpResponse("this is home page")
def about(request):
    context={}
    return render(request,'about.html',context) 
def weather(request):
    context={}
    return render(request,'weather.html',context) 
def disease(request):
    context={}
    return render(request,'disease.html',context) 

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = { 
        'questions': questions
    }
    return render(request, 'homePage.html', context)     

def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()
    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    return render(request, 'question.html', context)

def newQuestionPage(request):
    response_form = NewResponseForm()
    form=NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
        except Exception as e:
            print(e)
            raise
    context = {
            'form': form,
            'response_form': response_form
              }
    return render(request, 'new-question.html', context)    


def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')






def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        problem=request.POST.get("problem")
        contact=Contact(name=name,phone=phone,email=email,problem=problem,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    context={}
    return render(request,'contact.html',context)

def mainpage(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'mainpage.html')
         
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/mainpage")

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
 
def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')

				return redirect('/index')
			

		context = {'form':form}
		return render(request, 'register.html', context)
