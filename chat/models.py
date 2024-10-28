from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.TextField()
    # time_stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"(str{self.room} - {str(self.sender)})"
    
# class ChatRoomOneVsOne(models.Model):
#     user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user1')
#     user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user2')
    
#     # Đảm bảo không có 2 phòng chat trùng lặp giữa 2 người dùng
#     class Meta:
#         unique_together = ('user1', 'user2')

#     def __str__(self):
#         return f"Chat between {self.user1.username} and {self.user2.username}"