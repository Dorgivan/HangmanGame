from __future__ import unicode_literals

import uuid


from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
     return "%s" %(self.first_name)
  
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class Score(models.Model):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='UUIDUser')
    score = models.IntegerField(default=0, verbose_name='pontuação')

    def __str__(self):
     return self.score
  
    class Meta:
        verbose_name = 'pontuação'
        verbose_name_plural = 'pontuações'

class Word(models.Model):
    word = models.CharField(max_length=15, verbose_name='palavra')
    clue = models.CharField(max_length=150, verbose_name='dica')

    def __str__(self):
     return self.word
  
    class Meta:
        verbose_name = 'palavra'
        verbose_name_plural = 'palavras'

class Match(models.Model):
    aux = (
        (1, 'Finalizado'),
        (2, 'Não finalizado')
    )
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='UUIDUser2')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='Word')
    status = models.IntegerField(choices=aux)
    errors = models.IntegerField(verbose_name='erros', default=0)

    def __str__(self):
     return self.word

    def erro(self):
        self.errors+=1
        return errors

    class Meta:
        verbose_name = 'partida'
        verbose_name_plural = 'partidas'
