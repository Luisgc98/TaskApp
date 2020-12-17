from flask_mail import Message
from .config import Config
from . import Mail

mail = Mail()

def mail_sender_wel(email, user_name, password):
    if email:
        try:
            subject = 'Felicidades! Bienvenido a TaskApp'
            msg = Message(
                subject=subject, 
                recipients=[email], 
                sender=Config.MAIL_USERNAME
            )
            msg.html = '''
                    <div class=header>
                        <h1>Felicidades! Su registro fue un éxito!</h1>
                        <hr>
                    </div>
                    <div class="container">
                        <p>
                            Bienvenido a TaskApp.<br>En TaskApp usted puede administrar sus<br>
                            tareas faltantes, ver los examenes pendientes, o las fechas de futuros examenes.<br>
                            Además de poder mantener comunicación con su Coach asignado.
                        </p>
                        <h3>
                            <p>
                                Su cuenta fue registrada con los siguientes datos:<br><br>
                                Username: {}<br>
                                email: {}<br>
                                TaskApp password: {}
                            </p>
                        </h3>
                    </div>
                    <footer class="footer">
                        Gracias por su apoyo.
                    </footer>'''.format(user_name, email, password)

            mail.send(msg)
            return f'Correo enviado a {email}.'
        except:
            return 'Algo salió mal en el envió de correo.'