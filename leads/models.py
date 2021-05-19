from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Lead(models.Model):
    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('NewsLetter', 'NewsLetter'),
        ('Others', 'Others'),
    )
    first_name = models.CharField(
        max_length=25,
        verbose_name='first name',
        null=True
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name='last name',
        null=True
    )
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES,
        default="Youtube"
    )
    # profile_pic = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    def get_absolute_url(self):
        return reverse('leads:lead-detail', kwargs={'pk': self.id})


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return f"{self.user.username}"
