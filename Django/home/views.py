from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect
from .models import Product
from .forms import ProductForm , SimpleProductForm , CustomLoginForm , SearchForm

from django.contrib.auth import authenticate, login , logout
# from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages


def search(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(lesson_name__icontains=query) if query else []
    
    return render(request, 'index.html', {'query': query, 'results': results})



def login_view(request):
    if request.user.is_authenticated:
        return render(request , 'index.html' )
    else:
        if request.method == 'POST':
            form = CustomLoginForm(request, data=request.POST)
            if form.is_valid():
                print("Form is valid")  # Debugging
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    print("login keldi")  # Debugging
                    login(request, user)
                    messages.success(request, f'Hi {username.title()}, welcome back!')
                    return redirect('HomePage')
                else:
                    print("Authentication failed")  # Debugging
                    messages.error(request, 'Invalid username or password.')
            else:
                print("Form is not valid")  # Debugging
                messages.error(request, 'Invalid username or password.')
                return render(request,'login.html',{'form': form})
        else:
            form = CustomLoginForm()
            return render(request,'login.html',{'form': form})
            
            

def sign_out(request):

    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        


# Create your views here.
def homePage(request):
    if request.user.is_authenticated:
        Products = Product.objects.all()
        context = {
            "Products":Products
        }
        return render(request , "index.html" , context)
    else:
        return redirect("login")
# Front-end ---------------------------------------------------------------------------------------------------

def FrontEnd_view(request):
    Products = Product.objects.filter(category_name="Front-end")
    context = {
        "Products":Products
    }
    return render(request , "FrontEnd.html" ,context )

def createFrontEnd_view(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Front-end"
            form.save()
            return redirect('FronEnd_view')
        else:
            print("xatolik")
            print("Form is invalid. Errors:", form.errors)
    else:
        form = ProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Frontend(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("FronEnd_view")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Frontend(request, id):

    # dictionary for initial data with 
    # field names as keys
    # context = {}
    Products = Product.objects.all()
    context = {
        "Products":Products
    }
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    # if request.method == "POST":
        # delete object
    obj.delete()
    return redirect("FronEnd_view")
        # after deleting redirect to 
        # home page
    # return render(request , "Backend.html" , context)

# Back-end ---------------------------------------------------------------------------------------------------

def BackEnd_view(request):
    Products = Product.objects.filter(category_name="Back-end")
    context = {
        "Products":Products
    }
    return render(request , "BackEnd.html" ,context )

def createBackEnd_view(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Back-end"
            form.save()
            return redirect('BackEnd_view')
        else:

            print("Form is invalid. Errors:", form.errors)
    else:
        form = ProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Backend(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("BackEnd_view")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Backend(request, id):
    # return redirect("HomePage")
    # return render(request, "index.html", context)


    # dictionary for initial data with 
    # field names as keys
    # context = {}
    Products = Product.objects.all()
    context = {
        "Products":Products
    }
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    # if request.method == "POST":
        # delete object
    obj.delete()
    return redirect("BackEnd_view")
        # after deleting redirect to 
        # home page
    # return render(request , "Backend.html" , context)

# Adobe PS ---------------------------------------------------------------------------------------------------

def Photoshop_view(request):
    Products = Product.objects.filter(category_name="Grafik Dizayn" , subcategory_name="Photoshop")
    context = {
        "Products":Products
    }
    return render(request , "Photoshop.html" ,context )

def createPhotoshop_view(request):
    context = {}
    if request.method == 'POST':
        form = SimpleProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Grafik Dizayn"
            form.instance.subcategory_name = "Photoshop"
            form.save()
            return redirect('Photoshop_view')
        else:
            print("xatolik")
            print("Form is invalid. Errors:", form.errors)
    else:
        form = SimpleProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Photoshop(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = SimpleProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("Photoshop_view")
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Photoshop(request, id):
    # return redirect("HomePage")
    # return render(request, "index.html", context)


    # dictionary for initial data with 
    # field names as keys
    # context = {}
    Products = Product.objects.all()
    context = {
        "Products":Products
    }
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    # if request.method == "POST":
        # delete object
    obj.delete()
    return redirect("Photoshop_view")


# Adobe Illustrator ---------------------------------------------------------------------------------------------------

def Illustrator_view(request):
    Products = Product.objects.filter(category_name="Grafik Dizayn" , subcategory_name="Illustrator")
    context = {
        "Products":Products
    }
    return render(request , "illustrator.html" ,context )

def createIllustrator_view(request):
    context = {}
    if request.method == 'POST':
        form = SimpleProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Grafik Dizayn"
            form.instance.subcategory_name = "Illustrator"
            form.save()
            return redirect('Illustrator')
        else:
            print("xatolik")
            print("Form is invalid. Errors:", form.errors)
    else:
        form = SimpleProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Illustrator(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = SimpleProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("Illustrator")
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Illustrator(request, id):
    Products = Product.objects.all()

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)

    obj.delete()
    return redirect("Illustrator")


# Adobe Coreldraw ---------------------------------------------------------------------------------------------------

def Coraldraw_view(request):
    Products = Product.objects.filter(category_name="Grafik Dizayn" , subcategory_name="Coreldraw")
    context = {
        "Products":Products
    }
    return render(request , "Coraldraw.html" ,context )

def createCoraldraw_view(request):
    context = {}
    if request.method == 'POST':
        form = SimpleProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Grafik Dizayn"
            form.instance.subcategory_name = "Coreldraw"
            form.save()
            return redirect('Coraldraw')
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = SimpleProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Coraldraw(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = SimpleProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("Coraldraw")
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Coraldraw(request, id):
    Products = Product.objects.all()

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)

    obj.delete()
    return redirect("Coraldraw")


# Kompyuter savodxonligi ---------------------------------------------------------------------------------------------------   

def Kompyuter_view(request):
    Products = Product.objects.filter(category_name="Kompyuter savodxonligi" , subcategory_name="Kompyuter savodxonligi")
    context = {
        "Products":Products
    }
    return render(request , "kompyuter.html" ,context )

def createKompyuter_view(request):
    context = {}
    if request.method == 'POST':
        form = SimpleProductForm(request.POST)
        
        if form.is_valid():
            # Inspect form data
            form.instance.category_name = "Kompyuter savodxonligi"
            form.instance.subcategory_name = "Kompyuter savodxonligi"
            form.save()
            return redirect('Kompyuter')
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = SimpleProductForm()
    context['form'] = form
    return render(request, "addLesson.html", context)

def update_Kompyuter(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = SimpleProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("Kompyuter")
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_Kompyuter(request, id):
    Products = Product.objects.all()

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)

    obj.delete()
    return redirect("Kompyuter")





def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("HomePage")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "updateLesson.html", context)

def delete_view(request, id):

    # dictionary for initial data with 
    # field names as keys
    # context = {}
    Products = Product.objects.all()
    context = {
        "Products":Products
    }
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    # if request.method == "POST":
        # delete object
    obj.delete()
        # after deleting redirect to 
        # home page
    return render(request , "index.html" , context)

 
