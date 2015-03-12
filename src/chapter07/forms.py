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


class NewsLetterForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        submit_btn_name = kwargs.pop('submit_btn_name', 'subscribe_butn')
        submit_btn_value = kwargs.pop('submit_btn_value', 'Subscribe')

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit(name=submit_btn_name,
                                         value=submit_btn_value))


class SubscribeForm(NewsLetterForm):

    def __init__(self, *args, **kwargs):
        kwargs['submit_btn_name'] = 'subscribe_butn'
        kwargs['submit_btn_value'] = 'Subscribe'
        super().__init__(*args, **kwargs)


class UnSubscribeForm(NewsLetterForm):

    def __init__(self, *args, **kwargs):
        kwargs['submit_btn_name'] = 'unsubscribe_butn'
        kwargs['submit_btn_value'] = 'UnSubscribe'
        super().__init__(*args, **kwargs)


class ImportantDateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = models.ImportantDate
        fields = ["date", "desc"]
