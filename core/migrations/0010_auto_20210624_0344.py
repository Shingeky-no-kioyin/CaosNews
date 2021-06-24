# Generated by Django 3.2.3 on 2021-06-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_periodista_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut de Usuario')),
                ('nombreUsu', models.CharField(max_length=35, verbose_name='Nombre Usuario')),
                ('correoUsu', models.CharField(max_length=60, verbose_name='Correo Usuario')),
                ('contrasenna', models.CharField(max_length=35, verbose_name='Contraseña Usuario')),
            ],
        ),
        migrations.RenameField(
            model_name='periodista',
            old_name='contrasena',
            new_name='contrasenaPe',
        ),
        migrations.RenameField(
            model_name='periodista',
            old_name='nombre',
            new_name='nombrePe',
        ),
        migrations.RemoveField(
            model_name='periodista',
            name='correo',
        ),
        migrations.AddField(
            model_name='periodista',
            name='correoPe',
            field=models.CharField(default=1, max_length=60, verbose_name='Correo electrónico'),
            preserve_default=False,
        ),
    ]
