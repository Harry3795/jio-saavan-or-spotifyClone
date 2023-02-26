# Generated by Django 4.1 on 2022-08-30 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
        ('items', '0001_initial'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase_DetailsModel',
        ),
        migrations.AlterField(
            model_name='purchase_mastermodel',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.suppliermastermodel'),
        ),
        migrations.AlterField(
            model_name='purchase_tempmodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.itemmastermodel'),
        ),
        migrations.AlterField(
            model_name='purchasedetailsmodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.itemmastermodel'),
        ),
        migrations.DeleteModel(
            name='ItemMasterModel',
        ),
    ]
