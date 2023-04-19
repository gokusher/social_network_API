from django.contrib import admin

from .models import (PostModel, GroupModel, CommentModel,
                     FollowModel, LikesModel)


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    # Изменение поля group в любом посте
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'slug',)
    # Автозаполнение slug по полю title
    prepopulated_fields = {'slug': ('title',)}


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(PostModel, PostAdmin)
admin.site.register(GroupModel, GroupAdmin)
admin.site.register(CommentModel)
admin.site.register(FollowModel)
admin.site.register(LikesModel)