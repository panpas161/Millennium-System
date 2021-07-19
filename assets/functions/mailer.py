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

def sendTeacherCredentials(username,password,email,role="Teacher"):
    send_mail(
        subject="Λογαριασμός στο σύστημα της Millenium",
        message="Δημιουργήθηκε με επιτυχία ο λογαριασμός σας με τα παρακάτω στοιχεία:\nΌνομα Χρήστη: " + username + "\nΚωδικός Πρόσβασης: " + password + "\nΤύπος Χρήστη: " + translateUserRole(role),
        html_message="Δημιουργήθηκε με επιτυχία ο λογαριασμός σας με τα παρακάτω στοιχεία:<br>Όνομα Χρήστη: " + username + "<br>Κωδικός Πρόσβασης: " + password + "<br>Τύπος Χρήστη: " + translateUserRole(role),
        from_email="it@millennium.edu.gr",
        recipient_list=[email],
        fail_silently=False
    )
