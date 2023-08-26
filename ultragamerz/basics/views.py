from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import RegisterForm,UserLoginForm,messageForm
from .serializers import productSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import product

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            customer = Group.objects.get(name="Customers")
            user.groups.add(customer)

            return redirect('home')
       
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
                login(request, user)  # Correct usage of login function
                return redirect('Products')  # Redirect to the home page
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