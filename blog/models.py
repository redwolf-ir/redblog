from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

#my managers
#models.manager yani az on ers bari kon va 
#yeseri chiza behesh ezafe kon
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')

class Category(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'عنوان دسته‌بندی')
    slug = models.SlugField(max_length = 100, unique = True, verbose_name = 'آدرس دسته‌بنده')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = [
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده')
    ]
    title = models.CharField(max_length = 200, verbose_name = 'عنوان مقاله')
    slug = models.SlugField(max_length = 100, unique = True, verbose_name = 'آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name = 'دسته‌بندی', related_name = "articles")
    content = models.TextField(verbose_name = 'محتوا')
    thumbnail = models.ImageField(upload_to = 'thumbnail', verbose_name = 'تصویر بندانگشتی')
    published = models.DateTimeField(default = timezone.now, verbose_name = 'زمان انتشار')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, verbose_name = 'وضعیت')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def jpublished(self):
        return jalali_converter(self.published)
    
    objects = ArticleManager()