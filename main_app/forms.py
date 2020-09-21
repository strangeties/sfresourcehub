from .models import OpeningHours
from .models import Resource
from .models import WeeklyOpeningHours
from django import forms

class USPhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three  boxes.
    """
    class Media:
        js = ('js/us_phone_number_multiwidget.js',)

    def __init__(self,attrs=None):
        widgets = (
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone'}),
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone'}),
            forms.TextInput(attrs={'size':'4','maxlength':'4', 'class':'phone'}),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None,None,None]

    def value_from_datadict(self, data, files, name):
        values = super(USPhoneNumberMultiWidget, self).value_from_datadict(data, files, name)
        return u'+1 (%s)-%s-%s' % (values[0], values[1], values[2])

class WeeklyOpeningHoursMultiWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.TextInput(),
                   forms.TextInput())
        super(WeeklyOpeningHoursMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None,None]

    def value_from_datadict(self, data, files, name):
        values = super(WeeklyOpeningHoursMultiWidget, self).value_from_datadict(data, files, name)
        arr = [OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00'),
               OpeningHours(False, '00:00', '00:00')]
        return WeeklyOpeningHours(arr)

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class AddResourceForm(forms.Form):
    resource_name = forms.CharField(max_length=100, required=True)
    org_name = forms.CharField(max_length=100, required=True)
    category = forms.ChoiceField(choices=Resource.CATEGORIES)
    opening_hours = forms.CharField(max_length=512, widget=WeeklyOpeningHoursMultiWidget())
    phone = forms.CharField(widget=USPhoneNumberMultiWidget())
  
    foo = USPhoneNumberMultiWidget()
    print (foo.media)
    
    address = forms.CharField(max_length=100, required=True)
    street_number = forms.CharField(widget=forms.HiddenInput(),
                                    max_length=100, required=False, disabled=False)
    street_name = forms.CharField(widget=forms.HiddenInput(),
                                  max_length=100, required=False, disabled=False)
    city = forms.CharField(widget=forms.HiddenInput(),
                           max_length=100, required=False, disabled=False)
    state = forms.CharField(widget=forms.HiddenInput(),
                            max_length=100, required=False, disabled=False)
    country = forms.CharField(widget=forms.HiddenInput(),
                              max_length=100, required=False, disabled=False)
    postal_code = forms.CharField(widget=forms.HiddenInput(),
                                  max_length=100, required=False, disabled=False)
    long = forms.DecimalField(widget=forms.HiddenInput(),
                              required=False, disabled=False)
    lat = forms.DecimalField(widget=forms.HiddenInput(),
                             required=False, disabled=False)

    url = forms.URLField(max_length=100, required=False)
    notes = forms.CharField(max_length=250, required=False)
