# Generated by Django 4.0.3 on 2022-08-15 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrgen_app', '0006_alter_qrgenmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrgenmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
