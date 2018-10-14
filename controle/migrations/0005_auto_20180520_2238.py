# Generated by Django 2.0 on 2018-05-21 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_auto_20180520_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvendido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='controle.Cliente'),
        ),
        migrations.AlterField(
            model_name='itemvendido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='controle.Produto'),
        ),
    ]