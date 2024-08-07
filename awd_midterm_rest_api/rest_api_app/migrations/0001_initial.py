# Generated by Django 4.2 on 2023-07-17 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('domain_id', models.CharField(default=0, max_length=50)),
                ('d_description', models.CharField(max_length=100)),
                ('start_coor', models.IntegerField()),
                ('end_coor', models.IntegerField()),
                ('d_pfam_description', models.CharField(default='nothing', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('taxa_id', models.IntegerField(primary_key=True, serialize=False)),
                ('clade', models.CharField(max_length=50)),
                ('genus', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('protein_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=100)),
                ('protein_length', models.IntegerField(default=0)),
                ('domain', models.ManyToManyField(related_name='proteins', to='rest_api_app.domain')),
                ('taxonomy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proteins', to='rest_api_app.organism')),
            ],
        ),
        migrations.CreateModel(
            name='DomainProtein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api_app.domain')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api_app.protein')),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='protein',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='rest_api_app.protein'),
        ),
    ]
