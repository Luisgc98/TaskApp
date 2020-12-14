var passwd = document.getElementById('password');
document.getElementById('show').addEventListener('click', function(){
    if(passwd.type == 'password'){
        passwd.type = "text";
    }else {
        passwd.type = "password";
    }
});