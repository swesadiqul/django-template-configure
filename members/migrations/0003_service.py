# Generated by Django 4.2.5 on 2023-10-08 04:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('icon', models.ImageField(upload_to='services')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
