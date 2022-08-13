# AlanMRamirez

## Cafeteria

<h6>Este proyecto es una aplicacion web pensada para ser utilizada por una Cafeteria o negocio</h6> 

![](https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png)

## Librerias necesarias se encuentran en el archivo requirements

<p>Se recomienda utilizar un entorno virtual</p>

`pip install -r requirements.txt`

<p>La libreria necesaria para poder conectar la api a postgreSQL ya se encuentra en el archivo requirements</p>

## Desarrollo

<p>Recordar que durante la fase de desarrollo se tiene colocar True en el DEBUG y si se requiere colocar localhost y 127.0.0.1 en ALLOWED_HOST</p>

    DEBUG = True
    
    ALLOWED_HOSTS = []


<h6>Para levantar el servidor local</h6>

`python manage.py runserver`

<h6>Para poder recivir correos de gmail sera necesario modificar el archivo views y en el archivo settings agregar algunas variables </h6>

        email = EmailMessage(
                    "La Caffettiera: Nuevo mensaje de contacto",
                    "De {} <{}>\n\nEscribio\n\n{}".format(name, email, content),
                    "no-contestar@inbox.mailtrap.io",
                    ["alanmo@gmail.com"],
                    reply_to=[email]
                )
