# Generated by Django 3.1.2 on 2020-10-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eyehealth',
            name='high_confidence_limit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='eyehealth',
            name='location_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='eyehealth',
            name='low_confidence_limit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='eyehealth',
            name='sample_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='eyehealth',
            name='year_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='eyehealth',
            name='year_start',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='age',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='age_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='category',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='category_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_source',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value_footnote',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value_footnote_symbol',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value_type',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value_type_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='data_value_unit',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='gender',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='gender_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='geo_location',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='location_abbr',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='location_desc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='numerator',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='question',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='question_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='race_ethnicity',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='race_ethnicity_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='response',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='response_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='risk_factor',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='risk_factor_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='risk_factor_response',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='risk_factor_response_ID',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='topic',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eyehealth',
            name='topic_ID',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
