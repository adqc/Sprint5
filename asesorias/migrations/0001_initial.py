# Generated by Django 2.1.1 on 2018-09-16 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=255)),
                ('horaInicio', models.CharField(max_length=255)),
                ('horaFin', models.CharField(max_length=255)),
                ('lugar', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('creditos', models.IntegerField()),
                ('nivel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesorias.Facultad'),
        ),
        migrations.AddField(
            model_name='asesoria',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asesorias.Curso'),
        ),
        migrations.AddField(
            model_name='asesoria',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
