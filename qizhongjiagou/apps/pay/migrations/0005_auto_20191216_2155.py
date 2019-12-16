# Generated by Django 2.0.7 on 2019-12-16 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pay', '0004_auto_20191213_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='消费时间')),
                ('number', models.IntegerField(verbose_name='书币数量')),
                ('payment_detail', models.CharField(max_length=64, verbose_name='消费详情')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='消费用户')),
            ],
            options={
                'verbose_name_plural': '消费表',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='coin',
            field=models.IntegerField(null=True, verbose_name='书币数量'),
        ),
        migrations.AddField(
            model_name='order',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='支付总额'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_way',
            field=models.IntegerField(choices=[(0, '支付宝'), (1, '微信')], verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pey_status',
            field=models.IntegerField(choices=[(0, '未支付'), (1, '支付成功')], verbose_name='支付状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]