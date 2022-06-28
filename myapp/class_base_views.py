from django.conf import settings
from django.db.models import query
from django.db import models
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place, Restaurant, Waiter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import PlaceForm, RestaurantForm, WaiterForm
@method_decorator(login_required(login_url='/login'),name='dispatch')
class PlaceListView(ListView):
    # model = Place
    # queryset = Place.objects.all()
    template_name = 'class_base/list_view.html'
    context_object_name = 'all_places'
    paginate_by = settings.PAGINATE_BY
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in ListView'
        return context
    def get_queryset(self):
        return Place.objects.all()
        
@method_decorator(login_required(login_url='/login'),name='dispatch')
class PlaceDetailView(DetailView):
    model = Place
    template_name = 'class_base/detail_view.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in DetailView'
        return context
@method_decorator(login_required(login_url='/login'),name='dispatch')
class PlaceCreatView(CreateView):
    model = Place
    # fields = ('name','address','country')
    form_class = PlaceForm
    template_name = 'class_base/create_view.html'
    success_url = reverse_lazy('class_list_places')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class PlaceUpdateView(UpdateView):
    model = Place
    # fields = ('name','address','country')
    form_class = PlaceForm
    template_name = 'class_base/update_view.html'
    success_url = reverse_lazy('class_list_places')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class PlaceDeleteView(DeleteView):
    model = Place
    # fields = ('name','address','country')
    template_name = 'class_base/confirm_delete_view.html'
    success_url = reverse_lazy('class_list_places')

class RestaurantListView(ListView):
    # model = Place
    # queryset = Place.objects.all()
    template_name = 'class_base/restaurant_list_view.html'
    context_object_name = 'all_restaurants'
    paginate_by = settings.PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in RestaurantListView'
        return context
    def get_queryset(self):
        return Restaurant.objects.all()
@method_decorator(login_required(login_url='/login'),name='dispatch')
class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'class_base/restaurant_detail_view.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in RestaurantDetailView'
        return context
@method_decorator(login_required(login_url='/login'),name='dispatch')
class RestaurantCreatView(CreateView):
    model = Restaurant
    # fields = ('name','address','country')
    form_class = RestaurantForm
    template_name = 'class_base/restaurant_create_view.html'
    success_url = reverse_lazy('class_list_restaurant')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class RestaurantUpdateView(UpdateView):
    model = Restaurant
    # fields = ('name','address','country')
    form_class = RestaurantForm
    template_name = 'class_base/restaurant_update_view.html'
    success_url = reverse_lazy('class_list_restaurant')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class RestaurantDeleteView(DeleteView):
    model = Restaurant
    # fields = ('name','address','country')
    template_name = 'class_base/restaurant_confirm_delete_view.html'
    success_url = reverse_lazy('class_list_restaurant')


class WaiterListView(ListView):
    # model = Place
    # queryset = Place.objects.all()
    template_name = 'class_base/waiter_list_view.html'
    context_object_name = 'all_waiters'
    paginate_by = settings.PAGINATE_BY
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in ListView'
        return context
    def get_queryset(self):
        return Waiter.objects.all()        
@method_decorator(login_required(login_url='/login'),name='dispatch')
class WaiterDetailView(DetailView):
    model = Waiter
    template_name = 'class_base/waiter_detail_view.html'
    context_object_name = 'waiter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_name'] = 'PYTHON2108E-ONLINE: addition context in DetailView'
        return context
@method_decorator(login_required(login_url='/login'),name='dispatch')
class WaiterCreatView(CreateView):
    model = Waiter
    # fields = ('name','address','country')
    form_class = WaiterForm
    template_name = 'class_base/waiter_create_view.html'
    success_url = reverse_lazy('class_list_waiter')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class WaiterUpdateView(UpdateView):
    model = Waiter
    # fields = ('name','address','country')
    form_class = WaiterForm
    template_name = 'class_base/waiter_update_view.html'
    success_url = reverse_lazy('class_list_waiter')
@method_decorator(login_required(login_url='/login'),name='dispatch')
class WaiterDeleteView(DeleteView):
    model = Waiter
    # fields = ('name','address','country')
    template_name = 'class_base/waiter_confirm_delete_view.html'
    success_url = reverse_lazy('class_list_waiter')

