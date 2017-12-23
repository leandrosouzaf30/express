# Generated by Django 2.0 on 2017-12-19 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20171217_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemVendido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_unitario', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('desconto', models.FloatField()),
                ('data_venda', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Produto')),
            ],
        ),
    ]