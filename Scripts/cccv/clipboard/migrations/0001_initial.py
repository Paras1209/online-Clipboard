# Generated by Django 5.1.2 on 2024-10-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clipboardiems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UniqueCode', models.IntegerField(unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('documents', models.FileField(blank=True, null=True, upload_to='uploads/documents')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isfetched', models.BooleanField(default=False)),
            ],
        ),
    ]
