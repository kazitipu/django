from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from .forms import BlogPostModelForm
from .models import BlogPost



def blog_post_list_view(request):
    qs = BlogPost.objects.all() 
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/bloglist.html'
    context = {'blog_list': qs}
    return render(request, template_name, context) 



@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
        messages.info(request, "Your blog was created succesfully")
        return redirect ('/blog-new/')

    template_name = 'blog/create.html'
    context = {'form': form}
    return render(request, template_name, context)  


def blog_post_detail_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"blog": blog}
    return render(request, template_name, context)   

@staff_member_required
def blog_post_update_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        messages.success(request, "Your blog was updated succesfully")
        return redirect ('/blog/')
    template_name = 'blog/update.html'
    context = {"blog": blog, "form": form}
    return render(request, template_name, context)  


@staff_member_required
def blog_post_delete_view(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Your blog was deleted succesfully")
        return redirect("/blog")
    context = {"blog": blog}
    return render(request, template_name, context)  









