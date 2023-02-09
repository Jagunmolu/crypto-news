from django.db import models


class Exclusive(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}\n\n{self.content[:50]}'
