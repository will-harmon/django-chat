# from django.db import models
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
