from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(blank=False, max_length=80)

    @classmethod
    def create(cls, name):
        category = cls(title=name)
        # do something with the book
        return category

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=80, blank=False, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, default='')
    question_text = models.TextField(blank=False)
    choices = models.ManyToManyField('Choice', blank=True, related_name='questions')
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=False)
    closed_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.TextField(blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote(self):
        self.votes = self.votes + 1
        self.save()

    def votes_in_percent(self, question_id):
        total_votes = 0
        choices = Question.objects.get(id=question_id).choices.all()
        for choice in choices:
            total_votes = total_votes + choice.votes
        if total_votes == 0:
            total = 0
        else:
            total = (100.0*self.votes)/total_votes
        return total


