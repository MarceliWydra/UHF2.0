from django import forms
from .models import Participant, Ticket
from django_countries.widgets import CountrySelectWidget
from django.utils.safestring import mark_safe

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'is_staff']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'communication_agreement': mark_safe('I agree to <a href="http://urbanhighline.pl/uhf-2019/files/regulations/"> terms and conditions</a> of Urban Highline Festival 2022'),
            'gdpr_agreement': mark_safe('The controller of the personal data of the Participants are Firmament Fundation<br> with registered office at Cyrkoniowa 8/3, 20-538 Lublin. <br> The personal data of the Participants will be processed to organize an artistic event, for statistical purposes and for archiving (evidential)<br> purposes for securing information in case a legal need arises to demonstrate facts, which is a legitimate interest of Firmament Fundation<br> (pursuant to art 6 sec 1 let f of the General Data Protection Regulation of 27 April 2016 further referred to as GDPR).'),
        }