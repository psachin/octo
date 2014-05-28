from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from app.models import Blog

from app.forms import PostForm


def hello(request):
    output = _("Hello")
    return HttpResponse(output)


def say_hi(request):
    return render_to_response("say_hi.html")


def blog(request):
    context = RequestContext(request)
    blogs = Blog.objects.all()
    context_dict = {
        'blogs': blogs,
    }

    return render_to_response("app/blog.html", context_dict, context)


def submit_post(request):
    """Create a form to submit post.
    """
    context = RequestContext(request)

    if request.POST:
        postform = PostForm(data=request.POST)
        if postform.is_valid():
            postform.save(commit=True)
            return HttpResponseRedirect('/app/blog')
        else:
            print postform.errors
    else:
        postform = PostForm()
        print postform

    context_dict = {
        'postform': postform,
    }

    return render_to_response("app/submitpost.html", context_dict, context)
