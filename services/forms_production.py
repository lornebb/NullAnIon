from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProductionOrderForm(forms.Form):
    """ renders a form for user to order a production """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-production-order-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    PRODUCTION_TYPE = [('Guitar', 'Guitar'),
                        ('Bass', 'Bass'),
                        ('Synths', 'Synths'),
                        ('Keys', 'Keys'),
                        ('Drums', 'Drums')]
    
    type = forms.TypedChoiceField(
        label='Type of mix:',
        choices=PRODUCTION_TYPE,
        widget=forms.RadioSelect,
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required = True,
    )
    
    deliver_by = forms.DateField(
        label='Type of production needed:',
        widget=forms.DateInput,
        required=True,
    )
    
    reference_links = forms.CharField(
        label='...insert link here',
        max_length='1024',
        required=False,
    )

    notes = forms.CharField(
        label='explain a bit about what you need.',
        max_length='1024'
    )
