from app import Mail
from flask_mail import Message

mail = Mail()

def email_message(username, email, passwd):
    msg = Message(
        'Successful registration to TaskApp!',
        sender='bresjonny@gmail.com',
        recipients=[email]
    )
    msg.html = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Document</title>
            </head>
            <body>
                <div class=header>
                    <h1>Congratulations!</h1>
                    <hr>
                </div>
                <div class="container">
                    <h3>
                        <p>
                            Your account was successfully registered.<br><br>
                            Username: {}<br>
                            email: {}<br>
                            TaskApp password: {}
                        </p>
                    </h3>
                </div>
                <footer class="footer">
                    Thanks for your support.
                </footer>
            </body>
            </html>
    '''.format(username, email, passwd)

    mail.send(msg)

def email_change_passwd(username, email, passwd):
    msg = Message(
        'Successful Password Change!',
        sender='bresjonny@gmail.com',
        recipients=[email]
    )
    msg.html = '''<!DOCTYPE html>
    <html lang="en">
            <head>
                <meta charset="UTF-8"><title>Change of Password</title>
            </head>
            <body>
                <div class=header>
                    <h1>Change of Password.</h1>
                    <hr>
                </div>
                <div class="container">
                    <h3>
                        <p>
                            <b>The password for your TaskApp account ({}) has been changed to:</b><br>
                            {}
                        </p>
                    </h3>
                </div>
                <footer class="footer">
                    Any questions consult the e-mail: bresjonny@gmail.com
                </footer>
            </body>
            </html>
    '''.format(username, passwd)

    mail.send(msg)

def email_change_email(username, new_email, passwd):
    msg = Message(
        'Successful Password Change!',
        sender='bresjonny@gmail.com',
        recipients=[new_email]
    )
    msg.html = '''<!DOCTYPE html>
    <html lang="en">
            <head>
                <meta charset="UTF-8"><title>Change of Email</title>
            </head>
            <body>
                <div class=header>
                    <h1>Change of Email.</h1>
                    <hr>
                </div>
                <div class="container">
                    <h3>
                        <p>
                            <b>The e-mail for your TaskApp account ({}) has been changed to:</b><br>
                            {}<br><br>
                        </p>
                    </h3><hr>
                    <h4>
                        <p>
                            The new details of your account are:<br><br>
                            Username: {}<br>
                            email: {}<br>
                            TaskApp password: {}<br>
                            <p><b>Nota:</b> For security reasons, your password is encrypted.<br>Verify your password in the email that was sent to you earlier.</p>
                        </p>
                    </h4>
                </div>
                <footer class="footer">
                    Any questions consult the e-mail: bresjonny@gmail.com
                </footer>
            </body>
            </html>
    '''.format(username, new_email, username, new_email, passwd.split(':')[2])

    mail.send(msg)