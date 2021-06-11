from django.core.mail import send_mail

def sendEspaCredentials(username,password,email):
    send_mail(
        subject='Στοιχεία Πρόσβασης Για Την Πλατφόρμα ΕΣΠΑ',
        message='Όνομα Χρήστη: ' + username + '\nΚωδικός: ' + password + "\nEmail: " + email,
        html_message='Όνομα Χρήστη: ' + username + '<br>Κωδικός: ' + password + "<br>Email: " + email,
        from_email="it@millennium.edu.gr",
        recipient_list=[email],
        fail_silently=False
    )