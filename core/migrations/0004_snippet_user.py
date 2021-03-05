# Generated by Django 3.1.7 on 2021-03-05 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_snippet_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='core.user'),
            preserve_default=False,
        ),
    ]
