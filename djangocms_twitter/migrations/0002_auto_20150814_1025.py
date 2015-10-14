# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_twitter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter',
            name='follow_button',
        ),
        migrations.RemoveField(
            model_name='twitter',
            name='show_avatar',
        ),
        migrations.RemoveField(
            model_name='twitter',
            name='show_username',
        ),
        migrations.AlterField(
            model_name='twitter',
            name='plugin_template',
            field=models.CharField(default=b'djangocms_twitter/default.html', max_length=150, verbose_name='Design', choices=[(b'twitter/sidebar.html', b'Sidebar')]),
            preserve_default=True,
        ),
    ]
