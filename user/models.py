from django.db import models

# Create your models here.
class Profile(models.Model):
    roll_number = models.CharField(max_length=20,null=True)
    image = models.ImageField(null=True)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
class Notif(models.Model):
    user_reciever = models.ForeignKey("auth.User",  on_delete=models.PROTECT)
    user_sender = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True, related_name="sender")
    statement = models.CharField(max_length=100, default="notified")

