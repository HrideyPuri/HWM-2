# Generated by Django 5.0.3 on 2024-03-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_alter_payment_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='total_mark',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
