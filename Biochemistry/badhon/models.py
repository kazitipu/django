from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class DonorQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
                    Q(name__iexact=query) |
                    Q(blood_group__iexact=query) |
                    Q(department__iexact=query) 
                )

        return self.filter(lookup)


class DonorManager(models.Manager):
    def get_queryset(self):
        return DonorQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Donor(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    name=models.CharField(max_length=20)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='image/', blank=True, null=True)
    blood_group=models.CharField(max_length=10)
    department=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=15)

    objects = DonorManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blood/{self.slug}'

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"