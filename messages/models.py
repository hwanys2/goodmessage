from django.db import models

class Message(models.Model):
    content = models.TextField(verbose_name="메시지 내용")
    category = models.CharField(max_length=50, default="일반", verbose_name="카테고리")
    is_active = models.BooleanField(default=True, verbose_name="활성화")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    
    class Meta:
        verbose_name = "메시지"
        verbose_name_plural = "메시지들"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content
