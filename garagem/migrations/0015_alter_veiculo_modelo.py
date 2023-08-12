# Generated by Django 4.2.4 on 2023-08-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0014_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="modelo",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="veiculos",
                to="garagem.modelo",
            ),
        ),
    ]