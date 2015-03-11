from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models


class PersonDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        vip = kwargs.pop("vip", False)
        super().__init__(*args, **kwargs)

        # Are you a VIP?
        if vip:
            self.fields["first_class"] = forms.BooleanField(
                label="Fly First Class?",
                required=False,
                initial=True,
                help_text="First-class only offered to VIPs")

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Submit'))


class SubscribeForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('subscribe_butn', 'Subscribe'))


class UnSubscribeForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('unsubscribe_butn', 'UnSubscribe'))


class ImportantDateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = models.ImportantDate
        fields = ["date", "desc"]
