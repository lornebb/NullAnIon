from django.forms import ModelForm, Textarea, RadioSelect, DateInput
from django.forms.widgets import CheckboxSelectMultiple
from services.models import Mix, Master, Production

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div


class MixForm(ModelForm):
    class Meta:
        model = Mix
        fields = ('package_type', 
                'deliver_by', 'stem_choices',
                'revisions', 'reference_link_type',
                'reference_link', 'mix_extras',
                'contact', 'order_total',)
        
        widgets = {
            'package_type': RadioSelect(),
            'stem_choices': RadioSelect(),
            'revisions': RadioSelect(),
            'mix_extras': CheckboxSelectMultiple(),
            'deliver_by': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div('package_type', style="background: white;", title="Explication title", css_class="control")
            # Row(
            #     Column('package_type', css_class='icon-single HELLO WORLD'),
            #     Column('stem_choices', css_class='coioioioioi'),
            #     css_class='form-row'
            # ),
            # 'address_1',
            # 'address_2',
            # Row(
                # Column('city', css_class='form-group col-md-6 mb-0'),
                # Column('state', css_class='form-group col-md-4 mb-0'),
                # Column('zip_code', css_class='form-group col-md-2 mb-0'),
                # css_class='form-row'
            # ),
            # 'check_me_out',
            # Submit('submit', 'Sign in')
        )


class MasterForm(ModelForm):
    class Meta:
        model = Master
        fields = ('order_type', 'package_type', 
                    'deliver_by', 'stem_choices',
                    'revisions', 'reference_link_type',
                    'reference_link', 'mix_extras', 
                    'contact', 'order_total',)
        
        widgets = {
            'package_type': RadioSelect(),
            'stem_choices': RadioSelect(),
            'revisions': RadioSelect(),
            'mix_extras': CheckboxSelectMultiple(),
        }


class ProductionForm(ModelForm):
    class Meta:
        model = Production
        
        
        fields = ('production_type',
                'reference_link_type',
                'reference_link',
                'deliver_by',
                'contact',
                'notes',
        )
        widgets = {
            'production_type': CheckboxSelectMultiple(),
            'notes': Textarea(attrs={'cols': 1, 'rows': 1})
        }
