from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SounddesignOrderForm(forms.Form):
    """ renders a form for user to order a soundtrack """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-soundtrack-order-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    deliver_by = forms.DateField(
        label='Type of sounddesign needed:',
        widget=forms.DateInput,
        required=True,
    )
    
    reference_links = forms.CharField(
        label='...insert reference links here',
        max_length='1024',
        required=False,
    )

    notes = forms.CharField(
        label='explain the project here.',
        max_length='1024',
        required=True
    )
