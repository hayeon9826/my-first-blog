from django.db import models
from django.utils import timezone
# Create your models here.

#models은 Post가 장고 모델임을 의미
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #models.ForeignKey - 다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

        # string representation of object.
    def __str__(self):
        return self.title
        #__str__를 호출하면 Post 모델의 제목 텍스트(string)를 얻게 될 거에요.