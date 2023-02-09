from django.db import models
# from django.utils import timesince
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight


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
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title} || {self.content[:50]}'

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                             full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super().save(*args, **kwargs)


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
