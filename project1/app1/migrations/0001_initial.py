# Generated by Django 3.0.3 on 2022-06-24 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organism', models.IntegerField(blank=b'I00\n', unique=True)),
                ('organism_clade', models.CharField(blank=b'I00\n', max_length=50)),
                ('organism_name', models.CharField(blank=b'I00\n', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PfamDes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=b'I00\n', max_length=50, unique=True)),
                ('domain_des', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProteinSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein', models.CharField(blank=b'I00\n', max_length=50, unique=True)),
                ('sequence', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_start', models.IntegerField()),
                ('domain_end', models.IntegerField()),
                ('protein_length', models.IntegerField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.PfamDes', to_field='domain')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Organism', to_field='organism')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ProteinSequence', to_field='protein')),
            ],
        ),
    ]
