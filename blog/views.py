from django.shortcuts import render
from django.utils import timezone
from .models import Post
import logging

logger = logging.getLogger(__name__)

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	logger.info(posts)
	return render(request, 'blog/post_list.html', {'posts': posts})


