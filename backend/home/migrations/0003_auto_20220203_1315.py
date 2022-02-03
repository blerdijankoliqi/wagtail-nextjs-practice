# Generated by Django 3.2.12 on 2022-02-03 12:15

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_tekst',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Hey', max_length=100),
        ),
    ]