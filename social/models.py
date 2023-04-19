from django.db import models
from django.conf import settings


class GroupModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Группа')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class PostModel(models.Model):
    text = models.TextField('Текст поста', help_text='Введите текст поста')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    group = models.ForeignKey(GroupModel,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              related_name='posts',
                              verbose_name='Группа',
                              help_text='Выберете группу')
    image = models.ImageField('Картинка', upload_to='posts/', blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        LEN_OF_POST = 15
        return self.text[:LEN_OF_POST]


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Текст поста',
                             blank=True,
                             null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    text = models.TextField('Комментарий', help_text='Напишите комментарий')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class FollowModel(models.Model):
    """ Подписка на авторов
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following',
                               on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-author',)
        verbose_name = 'Лента автора'
        verbose_name_plural = 'Лента авторов'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'], name='unique_members')]


class LikesModel(models.Model):
	post = models.ForeignKey(PostModel, on_delete = models.CASCADE, 
                            verbose_name = 'post')
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete = models.CASCADE, 
                            verbose_name = 'user')
	date_creating = models.DateTimeField(auto_now_add = True, 
                                        verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id}'

	class Meta:
		verbose_name_plural = 'Лайки'
		verbose_name = 'Лайк'
		ordering = ['-date_creating']
