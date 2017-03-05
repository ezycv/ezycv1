# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eresume',
            name='displaypicture',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='dob',
            field=models.CharField(default=b'NULL', max_length=1250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='githublink',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='instagramlink',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='picture1',
            field=models.CharField(default=b'NULL', max_length=1250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='picture2',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='picture3',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='picture4',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='workdescribe1',
            field=models.CharField(default=b'NULL', max_length=1250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='workdescribe2',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='workdescribe3',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='workdescribe4',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eresume',
            name='cvlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='description',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='elaborate',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='emailid',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fbid',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fblink',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='location',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='state',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='twitterlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work1',
            field=models.CharField(default=b'NULL', max_length=1250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work2',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work3',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work4',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
    ]
