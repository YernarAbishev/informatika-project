from django.db import models
from pytils.translit import slugify
from datetime import datetime
from tinymce.models import HTMLField

class Level(models.Model):
    levelName = models.CharField("Деңгей атауы", max_length=100)

    def __str__(self):
        return f"{self.levelName}"

    class Meta:
        verbose_name = "Деңгей"
        verbose_name_plural = "Деңгейлер"

class Category(models.Model):
    categoryName = models.CharField("Категория атауы", max_length=150)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.categoryName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"

class Course(models.Model):
    courseName = models.CharField("Курс атауы", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    courseDescription = models.TextField("Курстың сипаттамасы")
    courseLogo = models.ImageField("Курс логотипі",  upload_to="images/")
    postDate = models.DateTimeField("Курстың жариялау уақыты мен күні", default=datetime.now)
    courseAge = models.IntegerField("Жас")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="Деңгей")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.courseName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.courseName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курстар"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    lessonName = models.CharField("Сабақ тақырыбы", max_length=255)
    videoLesson = models.CharField("Видео сабақ сілтемесі", max_length=500, blank=True, null=True)
    practiceLesson = HTMLField("Практикалық сабақ сипаттамасы", blank=True, null=True)

    def __str__(self):
        return f"{self.lessonName}"

    class Meta:
        verbose_name = "Сабақ"
        verbose_name_plural = "Сабақтар"