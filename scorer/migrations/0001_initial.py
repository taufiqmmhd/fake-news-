# Generated by Django 2.0.2 on 2018-02-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(help_text='Url of the Article')),
                ('title', models.TextField(help_text='Headline of Article')),
                ('body', models.TextField(help_text='Body of Article')),
                ('stance', models.CharField(help_text='Stance of Title in relation to Body', max_length=20)),
            ],
        ),
    ]