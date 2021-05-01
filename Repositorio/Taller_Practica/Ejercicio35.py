correo = "clubpenguin@gmail.com"
contraseña = 12345

correoingresado = str(input("Ingrese su correo/usuario: "))
contraseñaingresada = int(input("Ingrese su contraseña: "))

if correoingresado==correo and contraseñaingresada==contraseña:
    print("A sus ordenes mi rey")
else:
    print("sorry, but you look kinda sus")