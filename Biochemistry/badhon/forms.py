from django import forms

from .models import Donor 


class DonorModelForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name','blood_group', 'image', 'slug', 'department','address', 'contact_no', ]

    # def clean_name(self, *args, **kwargs):
    #     instance = self.instance
    #     name = self.cleaned_data.get('name')
    #     qs = BlogPost.objects.filter(name__iexact=name)
    #     if instance is not None:
    #         qs = qs.exclude(pk=instance.pk) # id=instance.id
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used. Please try again.")
    #     return title