from django.contrib.auth import login
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django import forms
# from robokassa.forms import RobokassaForm


def main(request):
    films = Film.objects.all()
    return render(request, 'kino/index.html', {'films': films})


def news(request):
    news = News.objects.all()
    return render(request, 'kino/news.html', {'news': news})


def feedback(request):
    return render(request, 'kino/feedback.html', {})


def contacts(request):    
    return render(request, 'kino/contacts.html', {})

    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'kino/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, error)
    else:
        form = AuthenticationForm()
    return render(request, 'kino/login.html', {'form': form})


def film(request, pk):
    film = Film.objects.get(pk=pk)
    reviews = Review.objects.filter(film=film)
    return render(request, 'kino/spiderman.html', {'film': film, 'reviews': reviews})


def session(request, pk):
    film = Film.objects.get(pk=pk)
    sessions = Session.objects.filter(film=film).order_by('start_time')
    return render(request, 'kino/sessions.html', {'sessions': sessions, 'film': film})


def sort(request, pk):
    film = Film.objects.get(pk=pk)
    sessions = Session.objects.filter(film=film).order_by('kino_teatre')
    
    return render(request, 'kino/sessions.html', {'sessions': sessions, 'film': film})


def history(request):
    his = History.objects.filter(owner=request.user)
    time = timezone.now()
    return render(request, 'kino/history.html', {'his': his, 'time': time})


def deleteticket(request, pk):
    History.objects.get(pk=pk).delete()
    his = History.objects.filter(owner=request.user)
    
    return render(request, 'kino/history.html', {'his': his})


def review(request, pk):
    author = request.user
    film = Film.objects.get(pk=pk)
    Review.objects.create(film=film, author=author, text=request.GET.get('text'))
    reviews = Review.objects.filter(film=film)
    return render(request, 'kino/spiderman.html', {'film': film, 'reviews': reviews})


def user_logout(request):
    logout(request)
    return redirect('main')


def seats(request, pk):

    return render(request, 'kino/cinema.html', {'pk': pk})


def pay_with_robokassa(request, pk):
    order = get_object_or_404(Session, pk=pk)
    History.objects.create(date=timezone.now(), owner=request.user, ticket=order)
    # form = forms(initial={
    #            'OutSum': order.tic_price,
    #            'InvId': order.pk,
    #            'Desc': order.film.name,
    #            'Email': request.user.email,
    #            # 'IncCurrLabel': '',
    #            # 'Culture': 'ru'
    #        })

    return render(request, 'kino/pay.html', {'order': order})


 # iutr23frc2uiwv2167g
 # пустышка мест