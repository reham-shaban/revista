from django.contrib import admin
from .models import UserStatus, Topic, TopicFollow, Follow, Post, Point, Like, Comment, Reply, Block, SavedPost

# Register your models here.
admin.site.register(UserStatus)
admin.site.register(Topic)
admin.site.register(TopicFollow)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Point)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Block)
admin.site.register(SavedPost)