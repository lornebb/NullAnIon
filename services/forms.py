from django import forms
# from django.forms.widgets import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

TYPE_CHOICES = [('single', 'single'),
                ('EP', 'EP'),
                ('Album / LP', 'Album / LP')]
    
DATE_CHOICES = [('2 working days', '2 working days'),
                ('5 working days', '5 working days'),
                ('10 working days', '10 working days')]

REFERENCE_TYPE_CHOICES = [('General', 'General'),
                            ('Energy', 'Energy'),
                            ('Tone', 'Tone'),
                            ('Instruments', 'Instruments')]

STEMS_CHOICE = [('6 grouped', '6 grouped'),
                ('40 individual stems', '40 individual stems'),
                ('40+ individual stems', '40+ individual stems')]

MASTER_STEMS_CHOICE = [('1 stereo pre-mix', '1 stereo pre-mix'),
                        ('5 grouped stems', '5 grouped stems')]

REVISIONS = [('upto 3 revisions', ' upto 3 revisions'),
            ('upto 6 revisions', 'upto 6 revisions')]

MIX_EXTRAS = [('Auto-Tune Lead Vocal', 'Auto-Tune Lead Vocal'),
            ('Auto-Tune Backing Vocals', 'Auto-Tune Backing Vocals'),
            ('Drum Replacement', 'Drum Replacement'),
            ('Instrumental Version', 'Instruemntal Version'),
            ('Show Ready Version', 'Show Ready Version'),
            ('A Capella Version', 'A Capella Version'),
            ('Group Mixed Stem Return', 'Group Mix Stem Return'),
            ('Individual Mixed Stem Return', 'Individual Mixed Stem Return')]

MASTER_EXTRAS = [('Instrumental Version', 'Instrumental Version (only for grouped stems)'),
                ('Show ready version', 'Show Ready Version (only for grouped stems)'),
                ('A Capella Version', 'A Capella Version (only for grouped stems)')]


class MixOrderForm(forms.Form):
    """ renders a form for user to order a mix """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-mix-order-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    type = forms.TypedChoiceField(
        label='Type of mix:',
        choices=TYPE_CHOICES,
        widget=forms.RadioSelect,
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required = True,)
    
    deliver_by = forms.TypedChoiceField(
        label='Deliver by:',
        choices=DATE_CHOICES, 
        widget=forms.RadioSelect, 
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required = True,)

    reference_type = forms.TypedChoiceField(
        label='References:',
        choices=REFERENCE_TYPE_CHOICES,
        widget=forms.RadioSelect,
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required=False)
    
    reference_links = forms.CharField(
        label="...insert link here",
        max_length='1024',
        required=False)

    stems = forms.ChoiceField(
        label='Stems:',
        choices=STEMS_CHOICE,
        widget=forms.RadioSelect)
    
    revisions = forms.TypedChoiceField(
        label="Revisions (per track):",
        choices=REVISIONS,
        widget=forms.RadioSelect)
    
    mix_extras = forms.MultipleChoiceField(
        label="Mix Extras",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MIX_EXTRAS)


class MasterOrderForm(forms.Form):
    """ renders a form for user to order a master """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-master-order-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    REVISIONS = [('upto 3 revisions', ' upto 3 revisions'),
                ('upto 6 revisions', 'upto 6 revisions')]
    
    type = forms.TypedChoiceField(
        label='Type of mix:',
        choices=TYPE_CHOICES,
        widget=forms.RadioSelect,
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required = True,)
    
    deliver_by = forms.TypedChoiceField(
        label='Deliver by:',
        choices=DATE_CHOICES, 
        widget=forms.RadioSelect, 
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required = True,)

    reference_type = forms.TypedChoiceField(
        label='References:',
        choices=REFERENCE_TYPE_CHOICES,
        widget=forms.RadioSelect,
        coerce = lambda x: bool(int(x)),
        initial = '1',
        required=False)
    
    reference_links = forms.CharField(
        label="...insert link here",
        max_length='1024',
        required=False)

    stems = forms.ChoiceField(
        label='Stems:',
        choices=MASTER_STEMS_CHOICE,
        widget=forms.RadioSelect)
    
    revisions = forms.TypedChoiceField(
        label="Revisions (per track):",
        choices=REVISIONS,
        widget=forms.RadioSelect)
    
    master_extras = forms.MultipleChoiceField(
        label="Mix Extras",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MASTER_EXTRAS)
