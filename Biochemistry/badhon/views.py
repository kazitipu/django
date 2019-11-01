from django.shortcuts import render,get_object_or_404,redirect
from .models import Donor
from .forms import DonorModelForm
from django.views.generic import DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

class DonorListView(ListView):
    queryset = Donor.objects.all()
    paginate_by=12
    template_name= 'badhon/service.html'

def donor_detail_view(request,slug):
     donor=Donor.objects.get(slug=slug)
     context={'donor':donor}
     return render(request, 'badhon/detail.html', context)


@login_required
def donor_create_view(request):
    form =DonorModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = DonorModelForm()
        messages.success(request, "Your have been registered as a donor here")
        return redirect("/blood")
    template_name = 'badhon/create.html'
    context = {'form': form}
    return render(request, template_name, context)  


@login_required
def donor_update_view(request, slug):
    donor = get_object_or_404(Donor, slug=slug)
    form = DonorModelForm(request.POST or None, instance=donor)
    if form.is_valid():
        form.save()
        messages.success(request, "Your profile has been updated")
        return redirect("/blood")
    template_name = 'badhon/update.html'
    context = {"donor": donor, "form": form}
    return render(request, template_name, context)  


@staff_member_required
def donor_delete_view(request, slug):
    donor = get_object_or_404(Donor, slug=slug)
    template_name = 'badhon/delete.html'
    if request.method == "POST":
        donor.delete()
        messages.success(request, "your profile has been deleted")
        return redirect("/blood")
    context = {"donor": donor}
    return render(request, template_name, context)  

