# Generated by Django 2.0.5 on 2018-07-06 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180705_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assets',
            options={'ordering': ['-asset_create_time'], 'verbose_name': '总资产表', 'verbose_name_plural': '总资产表'},
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': '业务表', 'verbose_name_plural': '业务表'},
        ),
        migrations.AlterModelOptions(
            name='diskassets',
            options={'verbose_name': '磁盘资产表', 'verbose_name_plural': '磁盘资产表'},
        ),
        migrations.AlterModelOptions(
            name='networkassets',
            options={'verbose_name': '网络资产表', 'verbose_name_plural': '网络资产表'},
        ),
        migrations.AlterModelOptions(
            name='networkcardassets',
            options={'verbose_name': '服务器网卡资产表', 'verbose_name_plural': '服务器网卡资产表'},
        ),
        migrations.AlterModelOptions(
            name='officeassets',
            options={'verbose_name': '办公资产表', 'verbose_name_plural': '办公资产表'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目表', 'verbose_name_plural': '项目表'},
        ),
        migrations.AlterModelOptions(
            name='ramassets',
            options={'verbose_name': '内存资产表', 'verbose_name_plural': '内存资产表'},
        ),
        migrations.AlterModelOptions(
            name='securityassets',
            options={'verbose_name': '安全资产表', 'verbose_name_plural': '安全资产表'},
        ),
        migrations.AlterModelOptions(
            name='serverassets',
            options={'verbose_name': '服务器资产表', 'verbose_name_plural': '服务器资产表'},
        ),
        migrations.AlterModelOptions(
            name='softwareassets',
            options={'verbose_name': '软件资产表', 'verbose_name_plural': '软件资产表'},
        ),
        migrations.AlterModelOptions(
            name='storageassets',
            options={'verbose_name': '存储资产表', 'verbose_name_plural': '存储资产表'},
        ),
    ]
