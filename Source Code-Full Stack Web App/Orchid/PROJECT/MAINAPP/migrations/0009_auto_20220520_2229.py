# Generated by Django 3.2.5 on 2022-05-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0008_braintumordiagnosishistory_diabetesdiagnosishistory_heartdiseasediagnosishistory_liverdiseasediagnos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heartdiseasediagnosishistory',
            old_name='col',
            new_name='chol',
        ),
        migrations.AddField(
            model_name='heartdiseasediagnosishistory',
            name='oldpeak',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
