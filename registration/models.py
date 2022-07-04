from email import message
from unicodedata import name
from django.db import models
from django_countries.fields import CountryField
from django.core import mail

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField()
    birth_date = models.DateField(blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    communication_agreement = models.BooleanField(default=True, blank=False, null=False)
    gdpr_agreement = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Participant, self).save(*args, **kwargs)
        if not self.created_at == self.updated_at: 
            ticket = Ticket.objects.create(participant=self)
            if self.country == "Ukraine":
                text = "Hi!" \
                    "<br>We are looking forward to meet with you this year! We sent you an e-mail with confirmation of your registration. " \
                    "<br><b>Your ticket no.: {}" \
                    "<br><b>Thanks to being part of the UHF 2022!</b> We hope you will enjoy the event!".format(ticket.pk)
                text_plain = "Hi! " \
                            "We are looking forward to meet with you this year! We sent you an e-mail with confirmation of your registration. " \
                            "This year you can pay by bank transfer to the number given below or at the festival by card. See you in Lublin!" \
                            "<b>Your ticket no.: {}" \
                            "<b>Thanks to being part of the UHF 2022!</b> We hope you will enjoy the event!".format(ticket.pk)
            else:
                text = "Hi!" \
                    "<br>We are looking forward to meet with you this year! We sent you an e-mail with confirmation of your registration. " \
                    "This year you can pay by bank transfer to the number given below or at the festival by card. See you in Lublin! <br>" \
                    "<b>Your ticket no.: {}<br>" \
                    "<b>Payment information:<br>" \
                    "<b>Ticket price: 25 eur/ 100 PLN <br>" \
                    "<b>SFIWT:</b> PL93 1140 2004 0000 3302 7889 4300<br>" \
                    "<b>Bank account number:</b> PL93 1140 2004 0000 3302 7889 4300<br>" \
                    "<b>Recipient:</b><br> Fundacja Firmament,<br>Cyrkoniowa 8/3,<br> 20-583 Lublin, Poland <br>" \
                    "<i><strong>Please add your ticket number in transfer description!</strong></i>".format(ticket.pk)
                text_plain = "Hi! " \
                            "We are looking forward to meet with you this year! We sent you an e-mail with confirmation of your registration. " \
                            "This year you can pay by bank transfer to the number given below or at the festival by card. See you in Lublin!" \
                            "<b>Your ticket no.: {}" \
                            "Payment information:" \
                            "Ticket price: 25 eur/ 100 PLN" \
                            "Bank account number:PL93 1140 2004 0000 3302 7889 4300" \
                            "Recipient: Fundacja Firmament,Cyrkoniowa 8/3, 20-583 Lublin Poland" \
                            "Please add your ticket number in transfer description!".format(ticket.pk)
            msg = mail.EmailMessage(
                'UHF 2022 - Registration confirmation',
                text,
                'no-replay@firmament.org.pl',
                [self.email],
            )
            msg.content_subtype = "html"
            msg.send()

class Ticket(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.participant.name}  {self.is_paid}"

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    