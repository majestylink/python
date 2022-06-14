from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_api_story_id = models.IntegerField("Story ID", null=True)
    story_type = models.CharField("Type of item", max_length=15, null=True)
    author = models.CharField("Author", max_length=50, null=True)
    slug = models.SlugField(max_length=2000, null=True)
    created_by = models.ForeignKey(get_user_model(), related_name="stories", on_delete=models.CASCADE, null=True)
    time = models.DateTimeField("Date created", null=True)
    text = models.TextField("The comment, story or poll text.", null=True)
    dead = models.BooleanField(default=False)
    story_url = models.URLField("URL", max_length=1000, null=True)
    score = models.IntegerField("Score", null=True)
    descendants = models.IntegerField("Descendants", null=True)
    title = models.TextField("Title", null=True)
    parent_id = models.IntegerField("Parent ID", null=True)

    class Meta:
        unique_together = ("unique_api_story_id", "title")
        verbose_name = "Latest News"
        verbose_name_plural = "Latest News"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:story_detail", kwargs={"id": self.id, "slug": self.slug})


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_comment_api_id = models.IntegerField("Story ID", null=True, unique=True)
    story = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments", null=True)
    author = models.CharField("Author", max_length=50, null=True)
    time = models.DateTimeField("Date created", null=True)
    text = models.TextField("Text", null=True)
    dead = models.BooleanField(default=False)
    comment_url = models.URLField("URL", max_length=1000, null=True)
    score = models.IntegerField("Score", null=True)
    title = models.TextField("Title", null=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.story.title
