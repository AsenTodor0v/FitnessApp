from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from NutriPage.meals.forms import MealsCreateForm
from NutriPage.meals.models import MealPlan


# Create your views here.

class CreateMealsView(CreateView):
    template_name = 'meals/create_meals.html'
    model = MealPlan
    form_class = MealsCreateForm
    success_url = reverse_lazy('homepage')


    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


