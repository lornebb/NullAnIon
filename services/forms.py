from django import forms
# from django.forms.widgets import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ExampleForm(forms.Form):
    """renders example form from crispy website"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

# class Mix_order_form(forms.Form):

#     TYPE_CHOICES = [('single', 'singe'),
#                     ('EP', 'EP'),
#                     ('Album / LP', 'Album / LP')]
    
#     DATE_CHOICES = [('2 working days', '2 working days'),
#                     ('5 working days', '5 working days'),
#                     ('10 working days', '10 working days')]
    
#     REFERENCE_TYPE_CHOICES = [('General', 'General'),
#                                 ('Energy', 'Energy'),
#                                 ('Tone', 'Tone'),
#                                 ('Instruments', 'Instruments')]
    
#     STEMS_CHOICES = [('6 grouped', '6 grouped'),
#                     ('40 individual stems', '40 individual stems'),
#                     ('40+ individual stems', '40+ individual stems')]
    
#     REVISIONS = [('upto 3 revisions', ' upto 3 revisions'),
#                 ('upto 6 revisions', 'upto 6 revisions')]

#     MIX_EXTRAS = [('Auto-Tune Lead Vocal', 'Auto-Tune Lead Vocal'),
#                 ('Auto-Tune Backing Vocals', 'Auto-Tune Backing Vocals'),
#                 ('Drum Replacement', 'Drum Replacement'),
#                 ('Instrumental Version', 'Instruemntal Version'),
#                 ('Show Ready Version', 'Show Ready Version'),
#                 ('A Capella Version', 'A Capella Version'),
#                 ('Group Mixed Stem Return', 'Group Mix Stem Return'),
#                 ('Individual Mixed Stem Return', 'Individual Mixed Stem Return')]

#     type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect, label='Type:')
#     deliver_by = forms.ChoiceField(choices=DATE_CHOICES, widget=forms.RadioSelect, label='Deliver by:')
#     reference_type = forms.ChoiceField(choices=REFERENCE_TYPE_CHOICES, widget=forms.RadioSelect, label='References:', required=False)
#     reference_links = forms.CharField(max_length='1024', label="...insert link here", required=False)
#     stems = forms.ChoiceField(choices=STEMS_CHOICES, widget=forms.RadioSelect, label='Stems:')
#     revisions = forms.ChoiceField(choices=REVISIONS, widget=RadioSelect, label="Revisions (per track):")
#     mix_extras = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=MIX_EXTRAS)


