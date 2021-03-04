from django import forms

class Mix_order_form(forms.Form):

    TYPE_CHOICES = [('single', 'singe'),
                    ('EP', 'EP'),
                    ('Album / LP', 'Album / LP')]
    
    DATE_CHOICES = [('2 working days', '2 working days'),
                    ('5 working days', '5 working days'),
                    ('10 working days', '10 working days')]

    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect, label='Type:')
    deliver_by = forms.ChoiceField(choices=DATE_CHOICES, widget=forms.RadioSelect, label='Deliver by:')
    reference_links = forms.CharField(max_length='1024', label="...insert link here")
