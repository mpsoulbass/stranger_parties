from django.db.models.signals import post_save
from django.dispatch import receiver

from stranger_parties.invite.models import Invite, Guest
from stranger_parties.invite.util import MailContext, EmailThread


@receiver(post_save, sender=Guest)
def send_password(sender, instance: Guest, created, **kwargs):
    if created:
        context = MailContext()
        context.from_mail = "admin@stranger-parties.com.br"
        context.to = [instance.email]
        context.subject = "Welcome to Stranger Parties"
        context.template_notification = "new_guest.html"
        context.mail_context = {"guest_email": instance.email}

        EmailThread(context).run()


@receiver(post_save, sender=Invite)
def send_invite(sender, instance: Invite, created, **kwargs):
    if created:
        context = MailContext()
        context.from_mail = "admin@stranger-parties.com.br"
        context.to = [instance.guest.email]
        context.subject = f"{instance.guest.name}, you were invited!!!"
        context.template_notification = "invite.html"
        context.mail_context = {
            "guest_name": instance.guest.name,
            "event_name": instance.event.name,
            "event_date": instance.event.date_time.strftime("%d/%m/%Y"),
            "event_hour": instance.event.date_time.strftime("%H:%M"),
            "confirm_link": instance.confirmation_link,
        }

        EmailThread(context).run()
