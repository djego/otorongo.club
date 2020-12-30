# Generated by Django 3.1.4 on 2020-12-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0009_auto_20201228_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompiledOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('idOrganizacionPolitica', models.IntegerField(null=True)),
                ('total_sentencia_penal', models.IntegerField(default=0, null=True)),
                ('total_sentencia_obliga', models.IntegerField(default=0, null=True)),
                ('total_sentencias', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='strOrganizacionPolitica',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]