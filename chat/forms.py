from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        label='Ваш вопрос',
        max_length=4000,
        strip=True,
        error_messages={
            'required': 'Введите вопрос.',
            'max_length': 'Вопрос слишком длинный: не больше %(limit_value)d символов.',
        },
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Спросите что-нибудь…'}),
    )