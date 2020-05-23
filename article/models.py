from django.db import models
# Create your models here.

CHOICES = (
    ('lost','LOST'),
    ('found', 'FOUND'),
    ('request','REQUEST'),
    ('sell','SELL'),
    ('giveaway','GIVEAWAY'),
)
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = models.TextField()
    article_type = models.CharField(max_length=15, choices=CHOICES, default= "LOST", verbose_name="Type")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    article_image = models.FileField(blank = True,null = True,verbose_name="Image")
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class LostArticle(Article):
    found = models.BooleanField(default=False, verbose_name="Found")

class FoundArticle(Article):
    claimed = models.BooleanField(default=False, verbose_name="Claimed")

class RequestArticle(Article):
    approvals = models.ManyToManyField("auth.User",verbose_name="appprovals")

class SellArticle(Article):
    base_price = models.IntegerField(verbose_name="Baseprice")
    claimed = models.BooleanField(default=False)
    highest_claimed_price=models.IntegerField(default=None)
    highest_claimant  = models.ForeignKey("auth.User",on_delete=models.PROTECT,verbose_name="Hclaim")
    deadline =models.DateTimeField(verbose_name = "deadline")
class GiveAwayArticle(Article):
    approvals = models.ManyToManyField("auth.User",verbose_name="appprovals")
    deadline =models.DateTimeField()
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
