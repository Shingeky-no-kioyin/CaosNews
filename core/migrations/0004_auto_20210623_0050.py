# Generated by Django 3.2.3 on 2021-06-23 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210623_0011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categorias',
        ),
        migrations.RenameModel(
            old_name='Noticia',
            new_name='Noticiass',
        ),
        migrations.RenameField(
            model_name='noticiass',
            old_name='categoria',
            new_name='categorias',
        ),
    ]
