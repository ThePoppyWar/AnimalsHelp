from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import LoginForm, UserCreationForm, UserPromissionForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('You not pass')
            return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class UserCreationView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        ret_val = super().form_valid(form)
        self.object.set_password(form.cleaned_data['pass_1'])
        self.object.save()
        return ret_val


class UserPermissionView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPromissionForm(instance=user)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPromissionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {"form": form})
