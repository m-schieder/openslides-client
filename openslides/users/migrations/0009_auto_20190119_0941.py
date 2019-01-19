# Generated by Django 2.1.5 on 2019-01-19 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={
                'default_permissions': (), 'ordering': ('last_name', 'first_name', 'username'),
                'permissions': (
                    ('can_see_name', 'Can see names of users'),
                    ('can_see_extra_data', 'Can see extra data of users (e.g. present and comment)'),
                    ('can_change_password', 'Can change its own password'),
                    ('can_manage', 'Can manage users'))},
        ),
    ]