from django.shortcuts import render, redirect
from .forms import ExtendForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post
# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def home2(request):
    request_counter_signal.send(sender=Post, timestamp='2019-1-10')
    return HttpResponse("hello")


@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("requestfinshed! ")


request_counter_signal = Signal(providing_args=['timestamp'])


@receiver(request_counter_signal)
def post_counter_signal_receiver(sender, **kwargs):
    print(kwargs)


def register(request):
    if request.method == 'POST':
        form = ExtendForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('home')
    else:
        form = ExtendForm()
    return render(request, 'accounts/register.html', {'form': form})
