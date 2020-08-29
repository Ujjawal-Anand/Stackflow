# Generated by Django 2.2 on 2020-08-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200828_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apidata',
            name='migated',
        ),
        migrations.AddField(
            model_name='apidata',
            name='migrated',
            field=models.BooleanField(blank=True, help_text='True to return only questions migrated away from a site', null=True, verbose_name='migrated'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='accepted',
            field=models.BooleanField(blank=True, help_text='True to return only questions with accepted answers', null=True, verbose_name='accepted'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='answers',
            field=models.PositiveIntegerField(blank=True, help_text='The minimum number of answers returned questions must have', null=True, verbose_name='Number of answers'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='body',
            field=models.CharField(blank=True, help_text="Text which must appear in returned questions' bodies.", max_length=1023),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='closed',
            field=models.BooleanField(blank=True, help_text='True to return only closed questions, false to return only open ones', null=True, verbose_name='closed'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='fromdate',
            field=models.DateField(blank=True, help_text='Return questions from date', null=True, verbose_name='From Date'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='notagged',
            field=models.CharField(blank=True, help_text='a semicolon delimited list of tags, none of which will be present on returned questions.', max_length=253, verbose_name='Not tagged'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='notice',
            field=models.BooleanField(blank=True, help_text='True to return only questions with post notices', null=True, verbose_name='Notice'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='order',
            field=models.CharField(choices=[('desc', 'Descending'), ('asc', 'Ascending')], default='desc', help_text='order of data returned', max_length=20, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='page',
            field=models.PositiveIntegerField(blank=True, help_text='Returns specified Page of result', null=True, verbose_name='Page number'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='pagesize',
            field=models.PositiveIntegerField(blank=True, help_text='Number of pages to be returned', null=True, verbose_name='Page Size'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='q',
            field=models.CharField(blank=True, help_text='A free form text parameter, will match all question properties ', max_length=1023, verbose_name='q'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='tagged',
            field=models.CharField(blank=True, help_text='A semicolon delimited list of tags, of which at least one will be present on all returned questions', max_length=255, verbose_name='Tagged'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='title',
            field=models.CharField(blank=True, help_text="Text which must appear in returned questions' titles", max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='todate',
            field=models.DateField(blank=True, help_text='Returns question up to date', null=True, verbose_name='To Date'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='url',
            field=models.CharField(blank=True, help_text='A url which must be contained in a post, may include a wildcard.', max_length=255, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='user',
            field=models.PositiveIntegerField(blank=True, help_text='The id of the user who must own the questions returned.', null=True, verbose_name='Id of user'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='views',
            field=models.PositiveIntegerField(blank=True, help_text='The minimum number of views returned questions must have.', null=True, verbose_name='views'),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='wiki',
            field=models.BooleanField(blank=True, help_text='True to return only community wiki questions', null=True, verbose_name='wiki'),
        ),
    ]