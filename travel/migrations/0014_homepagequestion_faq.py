# Generated by Django 5.1.7 on 2025-03-25 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_rename_header_logo_remove_navbars_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagequestion',
            name='faq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_list', to='travel.homepagefaq'),
        ),
    ]
