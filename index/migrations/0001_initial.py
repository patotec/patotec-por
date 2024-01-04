# Generated by Django 2.2 on 2023-12-10 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=46)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/media')),
                ('body', models.TextField(max_length=200000)),
            ],
        ),
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/ads')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('detail', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/media')),
                ('status', models.CharField(choices=[('active', 'active'), ('pending', 'pending')], default='pending', max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=200, null=True)),
                ('visit_count', models.IntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Catagory',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=2000)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='index.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='catagories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='index.Catagory'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='index.Tag'),
        ),
    ]