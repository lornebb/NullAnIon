from django.db import models

# global scope variables for choices
general = 'general'
energy = 'energy'
tone = 'tone'
instrument = 'instrument'
single = 'single (< 5mins)'
ep = 'ep (< 35mins)'
album = 'album / LP (> 35mins)'

reference_link_type = [(general, 'general'),
                    (energy, 'energy'),
                    (tone, 'tone'),
                    (instrument, 'instrument')]

package_type = [(single, 'single (< 5mins)'),
                (ep, 'ep (< 35mins)'),
                (album, 'album / LP (> 35mins)')]


class Mix(models.Model):
    """ model for MIX service database """

    class Meta:
        verbose_name_plural = 'Mixes'

    # local choices veriables

    SIX = '6'
    FOURTY_STEMS = '40'
    FOURTY_PLUS_STEMS = '40+'

    STEM_CHOICES = [(SIX, '6'),
                    (FOURTY_STEMS, '40'),
                    (FOURTY_PLUS_STEMS, '40+')]

    THREE = '3'

    REVISIONS = [(THREE, '3'),
                    (SIX, '6')]

    MIX_EXTRAS = [('Auto-Tune Lead Vocal', 'Auto-Tune Lead Vocal'),
                    ('Auto-Tune Backing Vocals', 'Auto-Tune Backing Vocals'),
                    ('Drum Replacement', 'Drum Replacement'),
                    ('Instrumental Version', 'Instruemntal Version'),
                    ('Show Ready Version', 'Show Ready Version'),
                    ('A Capella Version', 'A Capella Version'),
                    ('Group Mixed Stem Return', 'Group Mix Stem Return'),
                    ('Individual Mixed Stem Return',
                        'Individual Mixed Stem Return')]

    order_type = models.CharField(
        max_length=15, null=False, blank=False, default="Mix")
    package_type = models.CharField(
        max_length=1026, choices=package_type, blank=False,
        null=False, default=single)
    deliver_by = models.DateField(blank=False, null=False)
    stem_choices = models.CharField(
        max_length=1026, choices=STEM_CHOICES, blank=False,
        null=False, default=6)
    revisions = models.CharField(
        max_length=1026, choices=REVISIONS, blank=False,
        null=False, default=3)
    reference_link_type = models.CharField(
        max_length=1026, choices=reference_link_type, blank=True,
        null=True, default=general)
    reference_link = models.URLField(
        blank=True, null=True)
    mix_extras = models.CharField(
        max_length=1026, choices=MIX_EXTRAS, blank=False,
        null=False, default='')
    contact = models.EmailField(
        blank=False, null=False, default='')
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False,
        blank=False, default=22.23)

    def __str__(self):
        return self.contact


class Master(models.Model):
    """ model for MASTER service database """

    GROUP_STEMS = 'max 5 grouped stems'
    IND_STEMS = 'Individual track stems'

    STEM_CHOICES = [(GROUP_STEMS, 'max 5 grouped stems'),
                        (IND_STEMS, 'individual track stems')]

    SIX = '6'
    THREE = '3'

    REVISIONS = [(THREE, '3'),
                (SIX, '6')]

    MASTER_EXTRAS = [
                ('Drum Replacement', 'Drum Replacement'),
                ('Instrumental Version', 'Instruemntal Version'),
                ('Show Ready Version', 'Show Ready Version'),
                ('A Capella Version', 'A Capella Version'),]

    order_type = models.CharField(max_length=15, null=False, blank=False, default="Master")
    package_type = models.CharField(max_length=1026, choices=package_type, blank=False, null=False, default=single)
    deliver_by = models.DateField(blank=False, null=False)
    stem_choices = models.CharField(max_length=1026, choices=STEM_CHOICES, blank=False, null=False, default=[GROUP_STEMS])
    revisions = models.CharField(max_length=1026, choices=REVISIONS, blank=False, null=False, default=3)
    reference_link_type = models.CharField(max_length=1026, choices=reference_link_type, blank=True, null=False, default=general)
    reference_link = models.URLField(blank=True, null=False)
    mix_extras = models.CharField(max_length=1026, choices=MASTER_EXTRAS, blank=True, null=False, default='')
    contact = models.EmailField(blank=False, null=False, default='')
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return self.contact


class Production(models.Model):
    """ model for PRODUCTION service database """

    PRODUCTION_TYPE = [
        ('guitar', 'Guitar'),
        ('bass', 'Bass'),
        ('synths', 'Synths'),
        ('piano', 'Piano'),
        ('drums', 'Drums'),
        ('track_production', 'Track Production')
    ]

    order_type = models.CharField(max_length=15, null=False, blank=False, default="Production")
    production_type = models.CharField(max_length=1026, choices=PRODUCTION_TYPE, blank=False, null=False)
    reference_link_type = models.CharField(max_length=1026, choices=reference_link_type, blank=False, null=False, default=general)
    reference_link = models.URLField(blank=True, null=False)
    deliver_by = models.DateField(blank=False, null=False)
    contact = models.EmailField(blank=False, null=False, default='')
    notes = models.CharField(max_length=320)

    def __str__(self):
        return self.contact
