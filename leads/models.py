from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"

    def __str__(self) -> str:
        return self.user.username


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

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        "Agent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

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
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse("agents:agent-detail", kwargs={'pk': self.id})


class Category(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
