from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Chat, Comment, Thread

class ChatListView(LoginRequiredMixin, generic.ListView):
    model = Chat
    # form.instance.created_by = self.request.user
    # form.instance.chat_id = self.kwargs['pk']
    # return super().form_valid(form)

class ChatDetailView(LoginRequiredMixin, generic.DetailView):
    model = Chat

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)

class NewThreadView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    fields = ('text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)
