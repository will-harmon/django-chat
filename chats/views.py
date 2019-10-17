from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Chat, Comment

class ChatListView(generic.ListView):
    model = Chat
    template_name = 'chats/chat_list.html'

class ChatDetailView(generic.DetailView):
    model = Chat

class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)

class ChatCreateView(generic.CreateView):
    model = Chat
    fields = ('title','users','created_by')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
