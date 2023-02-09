from django.db import models


class Guide(models.Model):

    POST_TAGS = [
        ('BTC', 'Bitcoin'),
        ('BLOCK', 'BlockChain News'),
    ]
    
    title = models.CharField(max_length=100)
    post_category = models.CharField(
        max_length=5,
        choices=POST_TAGS,
        default='BLOCK',
    )
    content = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title}\n\n{self.content[:50]}'
