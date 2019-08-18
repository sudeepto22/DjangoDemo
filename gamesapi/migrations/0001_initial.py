# Generated by Django 2.2.4 on 2019-08-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('score', models.FloatField()),
                ('genre', models.CharField(max_length=50)),
                ('editors_choice', models.CharField(max_length=1)),
            ],
        ),
    ]