from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from django.urls import reverse
from django.views import View

from ultragamerz.settings import EMAIL_HOST_USER
from .forms import RegisterForm,UserLoginForm,messageForm
from .serializers import productSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import product
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['email']
            user = form.save()
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            email_subject = 'Ultragamerz Account Activation'
            activate_url = 'http://'+ domain + link
            email_body = "Please click the link to activate your account" + activate_url
            
            try:
                email = EmailMessage(
                    email_subject,
                    email_body,
                    EMAIL_HOST_USER,
                    [mail],
                )
                email.send()
                print('Email sent successfully')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as Ex:
                print(f"Error sending email: {Ex}")
                return HttpResponse('An error occurred while sending the email.')
            customer = Group.objects.get(name="Customers")
            user.groups.add(customer)
            return render(request,'authentication/verification.html')
        else:
            form.add_error(None, "Invalid email or password.")
            return render(request,'authentication/registration.html',{'form':form})
       
    form = RegisterForm()
    return render(request,'authentication/registration.html',{'form':form})
    
def home(request):
    return render(request,'shop/home.html')

def Contact_Us(request):
    form = messageForm()
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'contact.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  
                return redirect('products')  
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'authentication/login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('home')
class Products(ListView):
    model = product
    template_name = 'shop/goods.html'
    context_object_name = 'products'
    # ordering = ['-date']
    # paginate_by = 6

    def get_queryset(self):
        queryset = product.objects.all()
        return queryset
    
class verification_View(View):
    def get(self,request,uidb64,token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            if not token_generator.check_token(user,token):
                return redirect('login'+'?message='+'User already activated')
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            return redirect('login')
        except Exception as ex:
            pass

        return redirect('login')
