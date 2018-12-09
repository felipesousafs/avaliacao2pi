from django import template
from pools.models import Choice, Question
register = template.Library()


@register.simple_tag(name='votes_in_percent')
def votes_in_percent(choice_id, question_id):
    choice = Choice.objects.get(id=choice_id)
    question = Question.objects.get(id=question_id)
    return choice.votes_in_percent(question_id)
