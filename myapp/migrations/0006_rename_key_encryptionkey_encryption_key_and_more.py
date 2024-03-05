# Generated by Django 5.0.2 on 2024-02-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_encryptionkey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encryptionkey',
            old_name='key',
            new_name='encryption_key',
        ),
        migrations.AddField(
            model_name='encryptionkey',
            name='encrypted_text',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
