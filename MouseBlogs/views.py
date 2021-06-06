from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import BlogPostForm,CommentForm
from .models import BlogPost,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'MouseBlogs/index.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'MouseBlogs/blogs.html', context)

def bad_404():
    raise Http404

def blog(request,blog_id):
    blog = get_object_or_404(BlogPost,id=blog_id)
    comments = blog.comment_set.order_by('-date_added')
    context = {'blog': blog, 'comments': comments}
    return render(request, 'MouseBlogs/blog.html', context)


@login_required
def new_blog(request):
    """Create new topics"""
    if request.method != 'POST':
        """Create a form"""
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('MouseBlogs:blogs'))
    context = {'form':form}
    return render(request,'MouseBlogs/new_blog.html',context)

@login_required
def new_comment(request,blog_id):
    """Add new entries"""
    blog = get_object_or_404(BlogPost,id=blog_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.blog = blog
            new_comment.save()
            return HttpResponseRedirect(reverse('MouseBlogs:blog',
                                                args=[blog_id]))
    context = {'blog': blog, 'form': form}
    return render(request, 'MouseBlogs/new_comment.html', context)

@login_required
def edit_blog(request,blog_id):
    """Edit the entry"""
    blog = get_object_or_404(BlogPost, id=blog_id)
    if blog.owner != request.user:
        bad_404()

    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('MouseBlogs:blog',
                                        args=[blog.id]))
    context = {'blog':blog,'form':form}
    return render(request, 'MouseBlogs/edit_blog.html', context)

@login_required
def edit_comment(request,comment_id):
    """Edit the entry"""
    comment = get_object_or_404(Comment,id=comment_id)
    blog = comment.blog
    if comment.owner != request.user:
        bad_404()

    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('MouseBlogs:blog',
                                        args=[blog.id]))
    context = {'comment': comment,'blog': blog,'form':form}
    return render(request, 'MouseBlogs/edit_comment.html', context)

def help(request):
    return render(request,'MouseBlogs/help.html')