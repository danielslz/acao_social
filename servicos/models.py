# -*- coding: utf-8 -*-

from django.db import models
from filer.fields.image import FilerImageField


class AreaAtuacao(models.Model):
    class Meta:
        verbose_name_plural = u'áreas de atuação'

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    imagem = FilerImageField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL  # Important
    )

    def __unicode__(self):
        return self.nome


class Servico(models.Model):
    class Meta:
        verbose_name_plural = u'serviços'

    areaAtuacao = models.ForeignKey(AreaAtuacao)
    nome = models.CharField(max_length=500)

    def __unicode__(self):
        return self.nome
