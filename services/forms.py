from django import forms
from services.models import Mix, Master, Production
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class MixForm(forms.ModelForm):
    class Meta:
        model = Mix
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['order_type'].widget.attrs['disabled'] = True
        self.fields['order_type'].widget.attrs['required'] = True
        self.fields['reference_link'].widget.attrs['required'] = False


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['order_type'].widget.attrs['disabled'] = True
        self.fields['order_type'].widget.attrs['required'] = True
        self.fields['reference_link'].widget.attrs['required'] = False


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['order_type'].widget.attrs['disabled'] = True
        self.fields['order_type'].widget.attrs['required'] = True
        self.fields['reference_link'].widget.attrs['required'] = False
