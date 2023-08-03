from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView

from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from .models import ContactUs


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context
