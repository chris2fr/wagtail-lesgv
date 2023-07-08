from django.views.generic import ListView, DetailView

from .models import Tutorial

class FeedMeListView(ListView):
    model = Tutorial
    context_object_name = 'tutorial_list'
    template_name = 'tutorials/tutorial_list.html'


class FeedMeDetailView(DetailView): 
    model = Tutorial
    context_object_name = 'tutorial'
    template_name = 'tutorials/tutorial_detail.html'