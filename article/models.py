from django.db import models
# Create your models here.
TYPE_OPTIONS=(
    ('LST','lost'),
    ('FND','found'),
    ('SLL','sell'),
    ('GIV','give_away'),
    ('REQ','request'),
)
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    article_image = models.FileField(blank = True,null = True,verbose_name="Image")
    article_type = models.CharField(max_length=3,choices=TYPE_OPTIONS,default='REQ')
    resolved = models.BooleanField(default = False)
    deadline = models.DateTimeField(default=None,null=True)
    def get_likes(self):
        return self.like_set.count()
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
class Like(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)

class Bid(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    article =  models.ForeignKey(Article,on_delete=models.CASCADE)
    value = models.IntegerField(default=None, null=True)