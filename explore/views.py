from django.shortcuts import render
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import PostModel
# Create your views here.

class ExploreListView(ListView):
    def get(self, request, *args, **kwargs):

        try:
            #posts_qs =  PostModel.object.order_by('-upload_date')
            return render(request, 'index.html')
            
        except ObjectDoesNotExist:
            messages.warning(self.request, "No posts yet!")