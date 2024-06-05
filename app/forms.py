from django import forms

class PredictionForm(forms.Form):
    VEGETABLE_CHOICES = []
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('winter', 'Winter'),
    ]
    MONTH_CHOICES = [
        ('jan', 'January'),
        ('feb', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('aug', 'August'),
        ('sept', 'September'),
        ('oct', 'October'),
        ('nov', 'November'),
        ('dec', 'December'),
    ]
    DISASTER_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    vegetable = forms.CharField(max_length=100, required=True)
    season = forms.ChoiceField(choices=SEASON_CHOICES, required=True)
    month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    availability = forms.ChoiceField(choices=DISASTER_CHOICES, required=True)
    temperature = forms.FloatField(required=True)
