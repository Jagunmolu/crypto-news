from django.db import models
from django.utils import timesince


class Post(models.Model):

    POST_TAGS = [
        ('BLOCK', 'BlockChain News'),
        ('CRYPT', 'Crypto News'),
        ('PR', 'Press Release'),
    ]
    
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    post_category = models.CharField(
        max_length=5,
        choices=POST_TAGS,
        default='BLOCK',
    )
    content = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}\n\n{self.content[:50]}'


    # @property
    # def timesince(self):
    #     return timesince.timesince(self.timestamp)


class Comments(models.Model):
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.email)
