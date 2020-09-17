from django.forms import ModelForm
from address.forms import AddressField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit

from .models import locations

class LocationForm(ModelForm):
    address = AddressField()
    class Meta:
        model = locations
        fields = [
            'name', 
            'address', 
            'phone_number', 
            'website'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'LocationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_location'
        self.helper.add_input(Submit('submit', 'Create'))
        self.helper.layout = Layout (
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address',
            'website'
        )