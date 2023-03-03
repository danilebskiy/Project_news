from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_ratings = sum(list(map(lambda rating: rating['content_rating'] * 3,
                                    Post.objects.filter(author_id=self.id).values('content_rating'))))

        comment_author_rating = sum(list(map(lambda rating: rating['rating_comment'],
                                             Comment.objects.filter(user_id=self.user.id).values('rating_comment'))))

        posts_id = list(map(lambda rating: rating['content_rating'],
                            Post.objects.filter(author_id=self.id, content_type=ContentType.ARTICLE).values(
                                'content_rating')))

        comment_author_article_rating = sum(list(map(lambda rating: rating['rating_comment'],
                                                     Comment.objects.filter(post_id__in=posts_id,
                                                                            user_id=self.user.id).values(
                                                         'rating_comment'))))

        self.rating = post_ratings + comment_author_rating + comment_author_article_rating


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)


class ContentType(models.TextChoices):
    NEWS = 'новости'
    ARTICLE = 'статья'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=256, choices=ContentType.choices)
    data = models.DateTimeField(auto_now_add=True)
    content_header = models.CharField(max_length=256)
    content_text = models.CharField(max_length=5000)
    content_rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)

    def like(self):
        self.content_rating = self.content_rating + 1

    def dislike(self):
        self.content_rating = self.content_rating - 1

    def preview(self):
        return self.content_text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    datatime = models.DateTimeField(auto_now=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment = self.rating_comment + 1

    def dislike(self):
        self.rating_comment = self.rating_comment - 1
