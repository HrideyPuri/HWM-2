# Generated by Django 5.0.3 on 2024-03-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='max_questions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
