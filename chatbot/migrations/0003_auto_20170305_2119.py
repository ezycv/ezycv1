# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20170305_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eresume',
            old_name='picture1',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='eresume',
            old_name='picture2',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='eresume',
            old_name='picture3',
            new_name='name3',
        ),
        migrations.RenameField(
            model_name='eresume',
            old_name='picture4',
            new_name='name4',
        ),
        migrations.AlterField(
            model_name='eresume',
            name='mobile',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
    ]
