from django.core.mail import send_mail
from .authentication import translateUserRole

def sendEspaCredentials(username,password,email,role):
    send_mail(
        subject='Στοιχεία Πρόσβασης Για Την Πλατφόρμα ΕΣΠΑ',
        message='Όνομα Χρήστη: ' + username + '\nΚωδικός: ' + password + "\nEmail: " + email +"\nΤύπος Χρήστη: " + translateUserRole(role),
        html_message='Όνομα Χρήστη: ' + username + '<br>Κωδικός: ' + password + "<br>Email: " + email + "<br>Τύπος Χρήστη: " + translateUserRole(role),
        from_email="it@millennium.edu.gr",
        recipient_list=[email],
        fail_silently=False
    )