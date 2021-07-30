# Generated by Django 3.2.4 on 2021-07-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invite", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="invite", options={"ordering": ["id", "created_at", "updated_at"]}
        ),
        migrations.AddField(
            model_name="invite",
            name="guests",
            field=models.ManyToManyField(to="invite.Guest"),
        ),
        migrations.AlterUniqueTogether(name="invite", unique_together=set()),
        migrations.RemoveField(model_name="invite", name="guest"),
    ]