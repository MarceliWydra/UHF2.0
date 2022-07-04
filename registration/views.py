from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ParticipantForm

class RegistrationView(FormView):
    template_name = 'registrations/registrations.html'
    form_class = ParticipantForm
    success_url = '/registration/success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class SuccessView(FormView):
    template_name = 'registrations/success.html'
    form_class = ParticipantForm
    success_url = '/registration/success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ParticipantForm()
        return context
