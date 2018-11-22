from django import forms
from pools.models import Question
from pools.models import Choice


class NewQuestionForm(forms.ModelForm):
    question_text = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Question
        exclude = ('closed', 'pub_date', 'closed_at',)
