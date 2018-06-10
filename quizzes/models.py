from django.db import models

# Create your models here.

import uuid
from django.urls import reverse  # Used to generate urls by reversing the URL patterns


class Theme(models.Model):
  """
  Model representing a quiz theme
  """
  name = models.CharField(max_length=80, help_text="Enter a theme name.")

  def __str__(self):
    """
    String for representing the Model object (in Admin site etc.)
    """
    return self.name

class Answer(models.Model):
  """
  Model representing an answer.
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                        help_text="Unique ID for this particular answer across whole library")
  name = models.CharField(max_length=80)

  def __str__(self):
    """
    String for representing the Model object.
    """
    return self.name

class Question(models.Model):
  """
  Model representing a question.
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                        help_text="Unique ID for this particular answer across whole library")
  name = models.CharField(max_length=200)
  answers = models.ManyToManyField(Answer, help_text="Select possible answers for questions.")

  def __str__(self):
    """
    String for representing the Model object.
    """
    return self.name

class Quiz(models.Model):
  """
  Model representing a quiz.
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                        help_text="Unique ID for this particular quiz across whole library")
  name = models.CharField(max_length=80)
  summary = models.TextField(max_length=1000, help_text="Enter a brief description of the quiz.")
  theme = models.ManyToManyField(Theme, help_text="Select quiz theme")
  questions = models.ManyToManyField(Question, help_text="Select questions for the quiz")

  def display_theme(self):
    """
    Creates a string for the Theme. This is required to display theme in Admin.
    """
    return ', '.join([theme.name for theme in self.theme.all()[:3]])

  def get_absolute_url(self):
    """
    Returns the url to access a particular quiz instance.
    """
    return reverse('quiz-detail', args=[str(self.id)])

  def __str__(self):
    """
    String for representing the Model object.
    """
    return self.name
