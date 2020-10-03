from .models import OpeningHours
from .models import Resource
from .models import WEEKDAYS
from .models import WeeklyOpeningHours
from django import forms

class USPhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three  boxes.
    """
    def __init__(self,attrs=None):
        self.template_name = 'widgets/phone_number.html'
        widgets = (
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone', 'prefix':'+1 ( '}),
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone', 'prefix':') '}),
            forms.TextInput(attrs={'size':'4','maxlength':'4', 'class':'phone', 'prefix':' - '}),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None,None,None]

    def value_from_datadict(self, data, files, name):
        values = super(USPhoneNumberMultiWidget, self).value_from_datadict(data, files, name)
        return u'+1 (%s)-%s-%s' % (values[0], values[1], values[2])

class TimeWidget(forms.TimeInput):
    def __init__(self, attrs=None):
        if attrs == None:
            attrs = {}
        attrs['type'] = 'time'
        forms.TimeInput.__init__(self, attrs)

class OpeningHoursMultiWidget(forms.MultiWidget):
    class Media:
        js = ('js/weekly_opening_hours.js',)
    def __init__(self, attrs=None):
        self.template_name = 'widgets/opening_hours.html'
        widgets = (forms.CheckboxInput(attrs={'class': 'time_enabled', 'style': 'visibility: hidden'}),
                   TimeWidget(attrs={'class': 'time', 'value': '09:00'}),
                   TimeWidget(attrs={'class': 'time', 'value': '17:00', 'prefix': ' to '}))
        super(OpeningHoursMultiWidget, self).__init__(widgets, attrs)
    
    def decompress(self, value):
        if value:
          return value.split('-')
        return [None,None,None]

    def value_from_datadict(self, data, files, name):
        values = super(OpeningHoursMultiWidget, self).value_from_datadict(data, files, name)
        if values[0]:
          return '%s %s'%(values[1], values[2])
        else:
          return None

class WeeklyOpeningHoursMultiWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        self.template_name = 'widgets/weekly_opening_hours.html'
        widgets = (OpeningHoursMultiWidget(attrs={'weekday': 'Monday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_0', 'hours_id': 'opening_hours_times_0', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Tuesday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_1', 'hours_id': 'opening_hours_times_1', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Wednesday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_2', 'hours_id': 'opening_hours_times_2', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Thursday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_3', 'hours_id': 'opening_hours_times_3', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Friday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_4', 'hours_id': 'opening_hours_times_4', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Saturday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_5', 'hours_id': 'opening_hours_times_5', 'style': 'visibility: hidden'}),
                   OpeningHoursMultiWidget(attrs={'weekday': 'Sunday', 'closed_text': 'closed', 'weekday_id': 'opening_hours_weekday_6', 'hours_id': 'opening_hours_times_6', 'style': 'visibility: hidden'}))
        super(WeeklyOpeningHoursMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None,None,None,None,None,None,None]

    def value_from_datadict(self, data, files, name):
        values = super(WeeklyOpeningHoursMultiWidget, self).value_from_datadict(data, files, name)
        str = ''
        for i in range(7):
            str += '(%s %s)'%(WEEKDAYS[i], values[i])
        return str

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class AddResourceForm(forms.Form):
    resource_name = forms.CharField(max_length=100, required=True)
    org_name = forms.CharField(max_length=100, required=True)
    category = forms.ChoiceField(choices=Resource.CATEGORIES)
    opening_hours = forms.CharField(max_length=512, widget=WeeklyOpeningHoursMultiWidget(), required=False)
    phone = forms.CharField(widget=USPhoneNumberMultiWidget())
  
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
