from django.db import models

class Message(models.Model):
    user_text = models.TextField('вопрос')
    ai_text = models.TextField('ответ')
    created_at = models.DateTimeField('создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']
