# Generated by Django 3.2.7 on 2021-09-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_academy', '0003_alter_native_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='native',
            name='image',
            field=models.ImageField(upload_to='native_images/'),
        ),
    ]
