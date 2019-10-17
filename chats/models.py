from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Chat(models.Model):
    title = models.CharField(max_length=120)
    users = models.ManyToManyField(User, related_name='chats')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('chats:chat_detail', args=(self.chat_id,))



#
# # Create your models here.
# class ChatDetailView(generic.DetailView):
#     model = Chat
#
#     def add_comment(request, pk):
#         comment = Comment()
#         # you need to make this line dynamic
#         comment.text = 'hello'
#         comment.chat_id = pk
#         comment.save()
#         return HttpResponseRedirect(reverse('chats:chat_detail', args=(pk,)))
