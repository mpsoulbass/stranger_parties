# Generated by Django 3.2.4 on 2021-07-30 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("invite", "0002_auto_20210730_0110")]

    operations = [
        migrations.AlterModelOptions(name="invite", options={}),
        migrations.AddField(
            model_name="event",
            name="guests",
            field=models.ManyToManyField(through="invite.Invite", to="invite.Guest"),
        ),
        migrations.AddField(
            model_name="invite",
            name="guest",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_invitations",
                to="invite.guest",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="invite", unique_together={("guest", "event")}
        ),
        migrations.RemoveField(model_name="invite", name="guests"),
    ]
