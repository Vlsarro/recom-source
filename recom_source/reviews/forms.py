from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    """
    Specifies the model object it's going to use as a base (i.e. Review),
    a selection of fields to use, and also what widget to use for one of them
    """
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
