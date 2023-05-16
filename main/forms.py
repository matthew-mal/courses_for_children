from .models import Reviews
from django.forms import ModelForm, HiddenInput, Textarea, DateTimeInput


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['login', 'feedback', 'date']

        widgets = {
            "login": HiddenInput(),
            "feedback": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }
