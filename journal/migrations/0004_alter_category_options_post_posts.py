# Generated by Django 5.1 on 2024-08-24 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Catagories'},
        ),
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.category'),
            preserve_default=False,
        ),
    ]
