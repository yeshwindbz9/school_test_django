from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django import forms
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import *
from .models import *

# Create your views here.
# function based view
def home_view(request):
    return render(request, "classroom/home.html")


# class based view
class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankView(TemplateView):
    template_name = "classroom/thankyou.html"


# I've used this only for styling the create view form
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("f_name", "l_name", "sub_name")
        widgets = {
            "f_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "exampleFormControlInput1",
                    "placeholder": "name: first name",
                }
            ),
            "l_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "exampleFormControlInput2",
                    "placeholder": "name: last name",
                }
            ),
            "sub_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "exampleFormControlInput3",
                    "placeholder": "name: subject name",
                }
            ),
        }


class TeacherCreateView(CreateView):
    # default template -> model_form.html else override it!
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy("classroom:thankyou")
    # fields = [
    #     "f_name",
    #     "l_name",
    #     "sub_name",
    # ]
    # you cannot add css to create view and model, you gotta use modelform and use the form class


class TeacherListView(ListView):
    # default template -> model_list.html else override it!
    model = Teacher
    # queryset = Teacher.objects.all() #default
    template_name = "classroom/teacher_list.html"
    context_object_name = "teachers"  # instead of object_list


class TeacherDetailView(DetailView):
    # default template -> model_detail.html else override it!
    model = Teacher
    context_object_name = "teacher"
    # for a pk --> teacher object
    # the work is done at the template side, to pass the pk


class TeacherUpdateView(UpdateView):
    # this shares the model_form.html, teacher_form.html in this case
    # this needs a pk!
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy("classroom:thankyou")


class TeacherDeleteView(DeleteView):
    # needs a form for confirm delete
    # default template -> model_confirm_delete.html else override it!
    model = Teacher
    success_url = reverse_lazy("classroom:list_teacher")


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"  # html not url
    # success_url = "/classroom/thank_you/"  # url not html
    success_url = reverse_lazy("classroom:thankyou")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
