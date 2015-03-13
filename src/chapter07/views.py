from django.views import generic
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from braces.views import StaticContextMixin
from .forms import PersonDetailsForm
from .forms import SubscribeForm, UnSubscribeForm
from .forms import ImportantDateForm
from . import models


class FormView(StaticContextMixin, generic.TemplateView):
    template_name = "forms.html"
    static_context = {"form": PersonDetailsForm()}


class ClassBasedFormView(generic.View):
    template_name = 'cbv-form.html'

    def get(self, request):
        form = PersonDetailsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            # Success! We can use form.cleaned_data now
            return redirect('home')
        else:
            # Invalid form! Reshow the form with error highlighted
            return render(request, self.template_name,
                          {'form': form})


class GenericFormView(generic.FormView):
    template_name = 'cbv-form.html'
    form_class = PersonDetailsForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Check if the logged-in user is a memeber of "VIP" group
        kwargs["vip"] = self.request.user.groups.filter(name="VIP").exists()
        return kwargs


class NewsletterView(generic.TemplateView):
    subcribe_form_class = SubscribeForm
    unsubcribe_form_class = UnSubscribeForm
    template_name = "newsletter.html"

    def get(self, request, *args, **kwargs):
        kwargs.setdefault("subscribe_form", self.subcribe_form_class())
        kwargs.setdefault("unsubscribe_form", self.unsubcribe_form_class())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
            'files': self.request.FILES,
        }
        if "subscribe_butn" in request.POST:
            form = self.subcribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                subscribe_form=form)
            # Use the form.cleaned_data["email"]
            print("Subscribed to {}".format(form.cleaned_data["email"]))
            return redirect("home")
        elif "unsubscribe_butn" in request.POST:
            form = self.unsubcribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                unsubscribe_form=form)
            # Use the form.cleaned_data["email"]
            print("Unsubscribed from {}".format(form.cleaned_data["email"]))
            return redirect("home")
        return super().get(request)


# Pattern: CRUD Views

class ImpDateDetail(generic.DetailView):
    model = models.ImportantDate


class ImpDateCreate(generic.CreateView):
    model = models.ImportantDate
    form_class = ImportantDateForm


class ImpDateUpdate(generic.UpdateView):
    model = models.ImportantDate
    form_class = ImportantDateForm


class ImpDateDelete(generic.DeleteView):
    model = models.ImportantDate
    success_url = reverse_lazy("impdate_list")


# Non-CRUD
class ImpDateList(generic.ListView):
    model = models.ImportantDate
