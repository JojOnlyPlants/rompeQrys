from django.db import models
from registration.models import Profile

class Friendship(models.Model):
    user1 = models.ForeignKey(Profile, related_name='friendship_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name='friendship_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def delete_friend(self):
        friendship1 = Friendship.objects.get(user1=self.user2, user2=self.user1)
        friendship1.delete()
        self.delete()

    def __str__(self):
        return f"Amistad entre {self.user1.user} y {self.user2.user}"

class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profile, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='friend_requests_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def accept(self):
        Friendship.objects.create(user1=self.from_user, user2=self.to_user)
        Friendship.objects.create(user1=self.to_user, user2=self.from_user)
        self.accepted = True
        self.save()

    def decline(self):
        self.delete()

    def __str__(self):
        return f"Solicitud de amistad de {self.from_user.user} para {self.to_user.user}"
