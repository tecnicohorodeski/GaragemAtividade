# Generated by Django 4.2.4 on 2023-08-12 16:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0007_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="veiculo",
            name="modelo",
        ),
    ]
