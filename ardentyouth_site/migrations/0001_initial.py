# Generated by Django 4.0.6 on 2023-01-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ptittle', models.TextField()),
                ('Pdescr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/ArticleDets')),
                ('Atittle', models.TextField()),
                ('Adescr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GalleryDets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/GalleryDets')),
                ('Atittle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/mission')),
                ('mtext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OutlookDets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/OutlookDets')),
                ('Ptittle', models.TextField()),
                ('Pdescr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pcauses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/PopularCauses')),
                ('Ptittle', models.TextField()),
                ('Ptext', models.TextField()),
                ('Pdescr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/purpose')),
                ('ptext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('stittle', models.TextField()),
                ('stext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=100)),
                ('Timg', models.ImageField(upload_to='pics/Team')),
                ('Ttittle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/values')),
                ('vvtext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/vision')),
                ('vtext', models.TextField()),
            ],
        ),
    ]
