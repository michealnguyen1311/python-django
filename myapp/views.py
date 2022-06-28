import django
from django.forms.models import ModelForm
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse
from django.db.models import Q 
import time
import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
# from . import models
from .models import Place, Restaurant, Waiter, Article, CafefArticle
from .forms import PlaceForm, RestaurantForm,WaiterForm
# Function-base views: tất cả hàm đều có tham số là requerequest: HttpRequestst
# Phía back-end/server/máy chủ
# Create your views here.
def welcome(request):
    # Tham số của hàm tên là request: HttpRequest
    # Client/browser gõ URL vào thanh địa chỉ: HTTP REQUEST
    # Server nhận HTTP REQUEST
    #        trả về Client/Browser HTTP RESPONSE
    response = HttpResponse()
    response.write("<h1>Welcome to my first django web</h1>")
    response.write("<a href='https://www.djangoproject.com/'> Trang chủ django</a>")
    response.write("<h2>Danh sach cac Places</h2>")
    places = Place.objects.all()
    response.write("<ul>")
    for place in places:
        if Restaurant.objects.filter(place=place).exists():
            restaurant_place = place.restaurant
            response.write(f"<li>{place}, Restaurant:{restaurant_place}")
            response.write("<ol>")
            for waiter in restaurant_place.waiter_set.all():
                response.write(f"<li>{waiter.name}</li>")
            response.write("</ol></li>")
        else:
            response.write(f"<li>{place}</li>")
    return response

def index(request):
    # Mình truyền xữ liệu từ python cho HTML hiển thị
    # print("Logger user:", request.session['logged_user'])
    # lst = ["Python", "HTML", "CSS", "Javascript"]
    # now = datetime.datetime.now()
    
    places = Place.objects.all()

    return render(
        request=request,
        template_name='index.html', 
        context={ 
            # context: giá trị truyền qua cho temaplate html hiển thị
            # keys của context là các biến bên HTML sẽ gọi
            # 'logged_user': request.session['logged_user'],
            'places': places,
            # 'now': now
            }
        )

# Thứ tự 1 mới 1 functions view
# Bước 1: Viết cái hàm, render template cùng tên với tên hàm :))

def login(request):
    if request.method == "POST":
        print("Data client gửi lên")
        print("Tên đăng nhập", request.POST['username'])
        print("Mật khẩu", request.POST['password'])
        request.session['logged_user'] = request.POST['username']
        time.sleep(1)
        return redirect('index')
        # if request.POST['username'] == "python2108" and request.POST['password'] == "python2108":
        #     request.session['logged_user'] = request.POST['username']
        # else:
        #     del request.session['logged_user']
    # else: 
    #     print("Data request trên URL")
    #     print("Tên đăng nhập", request.GET['username'])
    #     print("Mật khẩu", request.GET['password'])
    return render(request, 'login.html')
@permission_required("myapp.list_places", login_url='/login', raise_exception=True)
def list_places(request):    
    places = Place.objects.all()
    keyword = request.GET.get('keyword', None)
    if keyword:
        places = Place.objects.filter(Q(name__contains= keyword) | Q(address__contains=keyword))
    
    paginator = Paginator(object_list = places,per_page= settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request=request,
        template_name='place/list.html',
        context={
            'page_obj': page_obj
            # 'places': places
                }
            )
#C Create
@login_required(login_url='/login')
def add_place(request):
    form = PlaceForm()
    if request.method == "POST":
        print(request.POST)
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect chuyển về Urls
            return redirect('list_places')
            # return HttpResponseRedirect('/place/list')
        else:
            print(form.errors)

    return render(
        request=request,
        template_name='place/add.html',
        context={
            'form': form
        }
    )
#R ( READ)
@login_required(login_url='/login')
def view_detail_place(request, place_id):
    place = get_object_or_404(Place,id=place_id) #Place.objects.get(id=place_id)
    return render(
        request=request,
        template_name='place/detail.html',
        context={
            'place': place
        }
    )
#U( Update)
@login_required(login_url='/login')
def update_place(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return render(
            request=request,
            template_name='404.html',
        )
    
    form = PlaceForm(instance=place)
    
    if request.method == "POST":
    # Chưa làm được chức năng sửa nếu trùng thì không cho add  
        # place.name = request.POST.get('name') 
        place.address = request.POST.get('address')
        place.country = request.POST.get('country')
        # print(request.POST)      
        place.save()
        return redirect('list_places')
            # return HttpResponseRedirect('/place/list')

    return render(
        request=request,
        template_name='place/update.html',
        context={
            'form': form
        }
    )
#D( Delete)
@login_required(login_url='/login')
def confirm_delete(request, place_id):
    data = get_object_or_404(Place,id=place_id)
    return render(
        request=request,
        template_name='place/confirm_delete.html',
        context={
            'data': data
        }
    )
@login_required(login_url='/login')
def delete_place(request, place_id):
    place = get_object_or_404(Place,id=place_id)
    place.delete()
    return redirect('list_places')

@login_required(login_url='/login')
def add_restaurant(request):
    form = RestaurantForm()
    if request.method == "POST":
        print(request.POST)
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_restaurant')
            # return HttpResponseRedirect('/place/list')
        else:
            print(form.errors)

    return render(
        request=request,
        template_name='restaurant/add.html',
        context={
            'form': form
        }
    )
def list_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(
        request=request,
        template_name='restaurant/list.html',
        context={
            'restaurants': restaurants
        }       
    )
@login_required(login_url='/login')
def view_detail_restaurant(request, place_id): 
    place = Place.objects.get(id=place_id)
    restaurant= get_object_or_404(Restaurant,place_id=place.id)
    print(place_id)
    return render(
        request=request,
        template_name='restaurant/detail.html',
        context={
            'restaurant': restaurant
        }
    )
@login_required(login_url='/login')   
def update_restaurant(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        restaurant = Restaurant.objects.get(place_id=place)
    except Restaurant.DoesNotExist:
        return render(
            request=request,
            template_name='404.html',
        )
    form = RestaurantForm(instance=restaurant)
    
    if request.method == "POST":
        print(request.POST)
        restaurant.serves_hot_dogs = True if request.POST.get('serves_hot_dogs') =='on' else False
        restaurant.serves_pizza = True if request.POST.get('serves_pizza') =='on' else False
        restaurant.serves_pho =  True if request.POST.get('serves_pho') =='on' else False
        # print(request.POST)
              
        restaurant.save()
        place.save()
        return redirect('list_restaurant')
            # return HttpResponseRedirect('/place/list')

    return render(
        request=request,
        template_name='restaurant/update.html',
        context={
            'form': form
        }
    )
@login_required(login_url='/login')
def delete_restaurant(request, place_id):
    place = Place.objects.get(id=place_id)
    restaurant = get_object_or_404(Restaurant,place_id=place.id)
    restaurant.delete()
    return redirect('list_restaurant')
@login_required(login_url='/login')
def add_waiter(request):
    form = WaiterForm()
    if request.method == "POST":
        print(request.POST)
        form = WaiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_waiter')
            # return HttpResponseRedirect('/place/list')
        else:
            print(form.errors)

    return render(
        request=request,
        template_name='waiter/add.html',
        context={
            'form': form
        }
    )
def list_waiter(request):
    waiters = Waiter.objects.all()
    return render(
        request=request,
        template_name='waiter/list.html',
        context={
            'waiters': waiters
        }       
    )
@login_required(login_url='/login')
def view_detail_waiter(request, waiter_id):
   
    waiters= get_object_or_404(Waiter,id=waiter_id)
    return render(
        request=request,
        template_name='waiter/detail.html',
        context={
            'waiters': waiters
        }
    )
@login_required(login_url='/login')
def update_waiter(request, waiter_id):
    try:
        waiter = Waiter.objects.get(id=waiter_id)
    except Waiter.DoesNotExist:
        return render(
            request=request,
            template_name='404.html',
        )
    form = WaiterForm(instance=waiter)
    
    if request.method == "POST":
    # Chưa làm được chức năng sửa nếu trùng thì không cho add  
        # place.name = request.POST.get('name') 
        print(request.POST)
        waiter.name = request.POST.get('name')
        # waiter.restaurant_id = request.POST.get('restaurant_id')
        print(request.POST)      
        waiter.save()
        return redirect('list_waiter')
            # return HttpResponseRedirect('/place/list')

    return render(
        request=request,
        template_name='waiter/update.html',
        context={
            'form': form
        }
    )
@login_required(login_url='/login')
def delete_waiter(request, waiter_id):
    waiter = get_object_or_404(Waiter,id=waiter_id)
    waiter.delete()
    return redirect('list_waiter')


def list_articles(request):
    articles = Article.objects.all()
    return render(
        request=request,
        template_name='article.html',
        context={   
            'articles':articles

        }
    )
def list_cafef_articles(request):
    articles = CafefArticle.objects.all()
    return render(
        request=request,
        template_name='cafef_article.html',
        context={   
            'articles':articles

        }
    )
def list_money(request):
    return render(request, 'moneyclub.html')
