var passwd = document.getElementById('password');
document.getElementById('show').addEventListener('click', function(){
    if(passwd.type == 'password'){
        passwd.type = "text";
    }else {
        passwd.type = "password";
    }
});

var signup_opc = document.getElementsByClassName('opc_tabs')[0];
var login_opc = document.getElementsByClassName('opc_tabs')[1];
var a_signup = document.getElementById('a_signup');
a_signup.addEventListener('click', function(){
    if(login_opc.getAttribute('class') == 'opc_tabs active'){
        signup_opc.setAttribute('class', 'opc_tabs active');
        login_opc.setAttribute('class', 'opc_tabs');
    }
});

function confirmation(field){
    var email = document.getElementById('email');
    if(field == email){
        var cont=0;
        var validate_email = document.getElementsByClassName('validate')[0];
        for(var i in field.value){
            if(field.value[i] == '@'){
                cont++;
            }
        }
        if((cont <= 0 || cont > 1) && email.value != ''){
            email.style.border = 'red 1px solid';
            validate_email.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Por favor valide que su Correo sea correcto.</b>';
            validate_email.style.display = 'inline';
        }else if(email.value == ''){
            email.style.border = '1px solid #ccc';
            validate_email.textContent = '';
            validate_email.style.display = 'none';
        }
    }
    var names = document.getElementById('names');
    var validate_names = document.getElementsByClassName('validate')[1];
    if(names.value.length > 25 && names.value != ''){
        names.style.border = 'red 1px solid';
        validate_names.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Nombre(s) no puede contener mas de 25 caracteres.</b>';
        validate_names.style.display = 'inline';
    }else {
        names.style.border = '1px solid #ccc';
        validate_names.textContent = '';
        validate_names.style.display = 'none';
    }
    var surnames = document.getElementById('surnames');
    var validate_surnames = document.getElementsByClassName('validate')[3];
    if(surnames.value.length > 25 && surnames.value != ''){
        surnames.style.border = 'red 1px solid';
        validate_surnames.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Apellidos no pueden contener mas de 25 caracteres.</b>';
        validate_surnames.style.display = 'inline';
    }else {
        surnames.style.border = '1px solid #ccc';
        validate_surnames.textContent = '';
        validate_surnames.style.display = 'none';
    }
    var new_password = document.getElementById('new_password');
    if(field == new_password){
        var nums = [1,2,3,4,5,6,7,8,9];
        var contSpaces=0, contNums=0;
        var validate_new_password = document.getElementsByClassName('validate')[2];
        for(var i in new_password.value){
            if(new_password.value[i] == ' '){
                contSpaces++;
            }else if(new_password.value[i] in nums){
                contNums++;
            }
        }
        if((contSpaces > 0 || contNums == 0 || contNums == new_password.value.length) && new_password.value != ''){
            new_password.style.border = 'red 1px solid';
            validate_new_password.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;La contraseña no puede tener espacios, debe contener al menos un número y una letra.</b>';
            validate_new_password.style.display = 'inline';
        }else{
            new_password.style.border = '1px solid #ccc';
            validate_new_password.textContent = '';
            validate_new_password.style.display = 'none';
        }
    }
    var password_confirmation = document.getElementById('password_confirmation');
    if(field == password_confirmation){
        var validate_passwords = document.getElementsByClassName('validate')[4];
        if(new_password.value != ''){
            if(new_password.value.length == password_confirmation.value.length){
                var cont=0;
                for(var i in password_confirmation.value){
                    if(password_confirmation.value[i] != new_password.value[i]){
                        cont++;
                    }
                }
                if(cont > 0){
                    password_confirmation.style.border = 'red 1px solid';
                    validate_passwords.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Las contraseñas no coinciden.</b>';
                    validate_passwords.style.display = 'inline';
                }else{
                    password_confirmation.style.border = '1px solid #ccc';
                    validate_passwords.textContent = '';
                    validate_passwords.style.display = 'none';
                }
            }else {
                password_confirmation.style.border = 'red 1px solid';
                validate_passwords.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Las contraseñas no coinciden.</b>';
                validate_passwords.style.display = 'inline';
            }
        }else if(password_confirmation.value != ''){
            password_confirmation.style.border = 'red 1px solid';
            validate_passwords.innerHTML = '<b>(!) &nbsp;&nbsp;&nbsp;Ingrese una contraseña nueva primero.</b>';
            validate_passwords.style.display = 'inline';
        }
        if(password_confirmation.value == ''){
            password_confirmation.style.border = '1px solid #ccc';
            validate_passwords.textContent = '';
            validate_passwords.style.display = 'none';
        }
    }
}