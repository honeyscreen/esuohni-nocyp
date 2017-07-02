from django.db import models

class User(models.Model):
    # id, integer, primary
    nickname = models.CharField(max_length=20)

    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=6) # 'male', 'female'
    device_ifa = models.CharField(max_length=200, db_index=True)
    device_anroid_id = models.CharField(max_length=200, db_index=True)

    join_date = models.DateTimeField(auto_now_add=True)

class Campaign(models.Model):
    cid = models.CharField(max_length=200, db_index=True)
    platform = models.CharField(max_length=7, db_index=True)
    price = models.FloatField()
    appstore = models.CharField(max_length=200)
    redirect_url = models.TextField()
    country = models.CharField(max_length=50)

    title = models.CharField(max_length=100)
    description = models.TextField()
    app_icon = models.TextField()
    app_image = models.TextField()

class Click(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Conversion(models.Model):
    click = models.ForeignKey(Click, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)