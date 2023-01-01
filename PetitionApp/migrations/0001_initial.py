# Generated by Django 3.2.16 on 2022-12-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetitonCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Наименование категории')),
                ('status', models.BooleanField(default=False, verbose_name='Активация')),
            ],
            options={
                'verbose_name': 'Категория петиции',
                'verbose_name_plural': 'Категории петиции',
            },
        ),
    ]