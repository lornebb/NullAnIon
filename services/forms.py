import datetime
from django.forms import ModelForm, Textarea, RadioSelect, DateField
from django.forms.fields import CharField
# from typing_extensions import Required
from services.models import Mix, Master, Production
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class MixForm(ModelForm):
    class Meta:
        model = Mix
        fields = ('package_type', 
                'deliver_by', 'stem_choices',
                'revisions', 'reference_link_type',
                'reference_link', 'mix_extras', 
                'total_price',)
        
        widgets = {
            'package_type': RadioSelect(),
            'stem_choices': RadioSelect(),
            'revisions': RadioSelect(),
            # 'deliver_by': DateField(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(MixForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.layout.append(Submit('save', 'save'))

    #     self.helper.form_id = 'id-MixOrderform'
    #     # self.helper.form_class = 'HELPER ACTIVATE' css class
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'checkout_order'

    #     self.helper.add_input(Submit('submit', 'Submit'))

    #     self.fields['order_type'].widget.attrs['disabled'] = True
    #     self.fields['order_type'].widget.attrs['required'] = True
    #     self.fields['reference_link'].widget.attrs['required'] = False
    #     # self.fields['total_price'].widget.attrs['default'] = "22.33"
    #     # self.fields['total_price'].widget.attrs['disabled'] = True
    #     self.fields['total_price'].widget.attrs['required'] = True
    #     # self.fields['package_type'].widget.forms.RadioSelect


class MasterForm(ModelForm):
    class Meta:
        model = Master
        fields = ('order_type', 'package_type', 
                    'deliver_by', 'stem_choices',
                    'revisions', 'reference_link_type',
                    'reference_link', 'mix_extras', 
                    'total_price',)
        
        widgets = {
            'package_type': RadioSelect(),
            'stem_choices': RadioSelect(),
            'revisions': RadioSelect(),
        }



class ProductionForm(ModelForm):
    class Meta:
        model = Production
        
        
        fields = ('production_type',
                'reference_link_type',
                'reference_link',
                'deliver_by',
                'notes',
        )
        widgets = {
            'notes': Textarea(attrs={'cols': 1, 'rows': 1})
        }
