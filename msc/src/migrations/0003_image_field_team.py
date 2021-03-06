# Generated by Django 2.0 on 2018-01-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('src', '0002_auto_20180130_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Field_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Image', models.ImageField(default='logo.png', height_field='height_field', upload_to=None, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('fb_link', models.CharField(max_length=50)),
                ('git_link', models.CharField(max_length=50)),
                ('linkedin_link', models.CharField(max_length=50)),
            ],
        ),
    ]
