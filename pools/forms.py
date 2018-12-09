from django import forms
from pools.models import Question
from pools.models import Category
from pools.models import Choice
from django.utils.safestring import mark_safe


class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.Input(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None,
                                      widget=forms.widgets.Select(attrs={'class': 'form-control'}))
    choices = forms.ModelMultipleChoiceField(queryset=Choice.objects.all(),
                                             widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}),
                                             required=False)
    question_text = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Question
        exclude = ['closed', 'pub_date', 'closed_at', ]

    def clean_question_text(self):
        question_text = self.cleaned_data['question_text']
        if not question_text.endswith('?'):
            raise forms.ValidationError(
                mark_safe('The question text must ends with ' + '<strong>' + '?' + '</strong>'))

        return question_text

    def clean_choices(self):
        choices = self.cleaned_data['choices']
        print(choices.__len__())
        if choices.__len__() > 4:
            raise forms.ValidationError(
                mark_safe("You can only add up to 4 choices."))

        return choices
