# Generated by Django 2.0.7 on 2019-03-18 21:17

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
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=150)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('population', models.IntegerField()),
                ('utc_offset', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('country_code_alpha2', models.CharField(max_length=3)),
                ('country_code_alpha3', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='CountryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField(max_length=150)),
                ('subregion', models.TextField(max_length=150)),
                ('population', models.IntegerField()),
                ('flag_url', models.TextField(null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationFinder.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('code', models.CharField(max_length=3)),
                ('symbol', models.CharField(max_length=250)),
                ('countries', models.ManyToManyField(blank=True, to='destinationFinder.CountryDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('iso639_1', models.CharField(max_length=2)),
                ('iso639_2', models.CharField(max_length=2)),
                ('countries', models.ManyToManyField(blank=True, to='destinationFinder.CountryDetails')),
            ],
        ),
        migrations.AddField(
            model_name='countrydetails',
            name='currencies',
            field=models.ManyToManyField(blank=True, to='destinationFinder.Currency'),
        ),
        migrations.AddField(
            model_name='countrydetails',
            name='languages',
            field=models.ManyToManyField(blank=True, to='destinationFinder.Language'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationFinder.Country'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinationFinder.City'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationFinder.Country'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationFinder.BlogPost'),
        ),
    ]
