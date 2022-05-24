# Generated by Django 4.0.1 on 2022-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('education', models.CharField(default='', max_length=100)),
                ('experience', models.TextField(blank=True, default='', null=True)),
                ('website', models.URLField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('projects', models.TextField(blank=True, default='', null=True)),
                ('resume', models.FileField(blank='False', null='False', upload_to='resume/', verbose_name='File')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='Applied', max_length=100)),
            ],
        ),
    ]
