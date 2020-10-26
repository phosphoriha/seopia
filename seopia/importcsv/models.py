from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


def pid_validation(PID):
    if not KW.objects.filter(id=PID).exists() and PID != 0:
        raise ValidationError(
            _('PID Not valid')
        )


class KW(models.Model):
    keyword = models.CharField(blank=False, max_length=50)
    id = models.IntegerField(auto_created=True, primary_key=True)
    PID = models.IntegerField(blank=False, default=0,
                              validators=[pid_validation])
    convert_rate = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    difficulty = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    search_volume = models.IntegerField()
    landing_title = models.CharField(max_length=100)
    landing_slug = models.CharField(max_length=50)
    hint = models.TextField()
    external_anchor_text = models.CharField(blank=False, max_length=50)
    external_link = models.URLField()
    internal_link = models.URLField()
    back_link = models.URLField()
    blog_post = "‌BP"
    blog_tag = "BT"
    blog_cat = "BC"
    page = "Pa"
    product = "Pr"
    product_cat = "PC"
    product_tag = "PT"
    product_attr = "PA"
    landing_type_item = [
        (blog_post, 'مقاله‌ی وبلاگ'),
        (blog_tag, 'برچسب وبلاگ'),
        (blog_cat, 'دسته‌بندی وبلاگ'),
        (page, 'برگه'),
        (product, 'محصول'),
        (product_cat, 'دسته‌بندی محصول'),
        (product_tag, 'برچسب محصول'),
        (product_attr, 'ویژگی محصول'),
    ]
    landing_type = models.CharField(max_length=3,
                                    choices=landing_type_item,
                                    default=blog_post)
    available = "Av"
    release = "Re"
    writing = "Wr"
    unavailable = "Ua"

    landing_status_item = [
        (available, 'موجود'),
        (release, 'منتشر شد'),
        (writing, 'درحال نوشتن'),
        (unavailable, 'ناموجود'),
    ]
    landing_status = models.CharField(
        max_length=3,
        choices=landing_status_item,
        default=unavailable)

    def __str__(self):
        return self.keyword
