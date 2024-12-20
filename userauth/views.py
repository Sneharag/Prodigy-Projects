from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views import View

from .forms import UserRegistrationForm


class UserRegistrationView(View):

    template_name='register.html'

    def get(self, request,*args,**kwargs):

        form_instance = UserRegistrationForm()

        return render(request,self.template_name, {'form': form_instance})

    def post(self, request,*args,**kwargs):

        form_data=request.POST

        form_instance = UserRegistrationForm(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect('login')
        
        return render(request, self.template_name, {'form': form_instance})


class UserLoginView(View):

    template_name='login.html'

    def get(self, request,*args,**kwargs):

        return render(request, self.template_name)

    def post(self, request,*args,**kwargs):

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:

            login(request, user)

            return redirect('protected')
        
        return render(request,self.template_name, {'error': 'Invalid credentials'})


class UserLogoutView(View):

    def get(self, request,*args,**kwargs):

        logout(request)

        return redirect('login')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ProtectedView(View):

    template_name='protected.html'

    def get(self, request):

        return render(request,self.template_name, {'user': request.user})
