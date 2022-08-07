# Generated by Django 4.0.6 on 2022-08-04 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0003_alter_cargo_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('-create_date',), 'verbose_name': 'Водитель', 'verbose_name_plural': 'Водители'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-create_date',), 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('-create_date',), 'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-create_date',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='truck',
            options={'ordering': ('-create_date',), 'verbose_name': 'Грузовик', 'verbose_name_plural': 'Грузовики'},
        ),
        migrations.AlterModelOptions(
            name='waybill',
            options={'ordering': ('-create_date',), 'verbose_name': 'Путивой лист', 'verbose_name_plural': 'Путевые листы'},
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='higth',
            new_name='hight',
        ),
        migrations.AlterField(
            model_name='waybill',
            name='point_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='waybill_loaction_a', to='cargo_app.location'),
        ),
    ]