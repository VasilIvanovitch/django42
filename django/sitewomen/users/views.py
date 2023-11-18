from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm, ProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import inlineformset_factory

from .models import Profile


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


    # def get_success_url(self):
    #     return reverse_lazy('women:home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['profile_form'] = ProfileForm(self.request.POST)
    #     else:
    #         context['profile_form'] = ProfileForm()
    #     return context
    #
    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        if profile_form.is_valid():
            self.object = form.save()
            profile_form.instance.user = self.object
            profile_form.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем объект пользователя
        user = self.get_object()

        # Создаем ProfileUserFormSet для пользователя
        ProfileUserFormSet = inlineformset_factory(
            get_user_model(),  # Родительская модель (User)
            Profile,  # Дочерняя модель (Profile)
            fields=['photo', 'date_birth'],  # Поля для включения в форму
            can_delete=False,  # Не разрешать удаление объекта Profile из формы
            extra=1  # Количество дополнительных форм, которые будут отображаться по умолчанию
        )
        formset = ProfileUserFormSet(instance=user)
        for form in formset.forms:
            form.fields['photo'].widget.attrs['class'] = 'form-input'
            form.fields['date_birth'].widget.attrs['class'] = 'form-input'
        # Передаем форму ProfileUserFormSet в контекст
        context['profile_form'] = formset
        # context['formset'] = ProfileUserFormSet(instance=user)
        return context


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}



# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             return render(request, 'users/register_done.html')
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})

