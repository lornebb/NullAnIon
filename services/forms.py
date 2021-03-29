from django.forms import ModelForm, Textarea, RadioSelect
from django.forms.widgets import CheckboxSelectMultiple
from services.models import Mix, Master, Production


class MixForm(ModelForm):
    class Meta:
        model = Mix
        fields = ('package_type',
                  'deliver_by', 'stem_choices',
                  'revisions', 'reference_link_type',
                  'reference_link', 'mix_extras',
                  'contact',)

        widgets = {
            'package_type': RadioSelect(),
            'stem_choices': RadioSelect(),
            'revisions': RadioSelect(),
            'mix_extras': CheckboxSelectMultiple(),
        }


class MasterForm(ModelForm):
    class Meta:
        model = Master
        fields = ('order_type', 'package_type',
                  'deliver_by', 'stem_choices',
                  'revisions', 'reference_link_type',
                  'reference_link', 'mix_extras',
                  'contact',)

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
            'notes': Textarea(attrs={'cols': 1, 'rows': 3})
                }
