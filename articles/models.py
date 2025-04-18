from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    autor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class likes(models.Model):
    liker = models.ForeignKey('users.CustomUser', related_name="likering", on_delete=models.CASCADE)
    liked = models.ForeignKey('Articles', related_name="likes", on_delete=models.CASCADE)
    liked_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('liker', 'liked')

    def __str__(self):
        return f"{self.liker.username} likes {self.liked.title}"

class comentarios(models.Model):
    comentario = models.TextField()
    comment = models.ForeignKey('users.CustomUser', related_name="Comentor", on_delete=models.CASCADE)
    commented = models.ForeignKey('Articles', related_name="Comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment.username} comento en {self.commented.title}"