# Generated by Django 2.2.12 on 2020-05-28 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='institutes', to='CV.Section'),
            preserve_default=False,
        ),
    ]
