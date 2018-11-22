from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(blank=False)
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.question_text

    def choices(self):
        return Choice.objects.filter(question=self)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.TextField(blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote(self):
        self.votes = self.votes + 1
        self.save()

    def votes_in_percent(self):
        total_votes = 0
        choices = Choice.objects.filter(question=self.question)
        for choice in choices:
            total_votes = total_votes + choice.votes
        if total_votes == 0:
            total = 0
        else:
            total = (100.0*self.votes)/total_votes
        return total

