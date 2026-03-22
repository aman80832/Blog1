from django.db import models

# Profile Model
class Profile(models.Model):
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"Comment on {self.post.title}"