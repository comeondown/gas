# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_specification_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=500, verbose_name='Название новости')),
                ('text', redactor.fields.RedactorField(max_length=3000, verbose_name='Текст новости')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=redactor.fields.RedactorField(blank=True, max_length=3000, verbose_name='Особенности'),
        ),
    ]
