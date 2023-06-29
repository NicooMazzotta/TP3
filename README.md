# TP3
Este es un proyecto web desarrollado utilizando el framework Django.

El proyecto es una aplicación web que permite a los usuarios registrarse como compradores o vendedores, acceder a sus respectivas cuentas y poder agregar objetos vendidos/comprados a una lista que tenian dentro de sus clases.-

La web se basa en una pagina de inicio donde hay 4 botones:

    Boton Inicio: Esta presente en  todos los templates, siempre vuelve a la pagina de inicio.

    Boton Comprador: Te dirige al template base de los compradores. Aca se pueden seguir visualizando los primeros 4 botones y se pueden visualizar dos nuevos. Los botones Registrar y Acceder.

        Boton Registrar: te lleva al template donde hay un formulario donde el usuario-comprador se puede registrar. Cuenta con 4 campos (Email, usuario,contrasenia y direccion para las entregas), los 4 son obligatorios. Agregue tambien que el email tiene que ser unico. esto lo chequea a la hora de mandar el formulario, lo corrobora a la hora de crear el perfil fijandose en la base de datos.
        Algunas pruebas que hice para testear fue crear varias cuentas, intentando repetir el email pero no se registra. Lo que es el nombre de usuario, contrasenia y direccion se puede repetir y no se solapa con las otras cuentas.
        una vez que se crea el perfil ya te redirige a otro template que seria con la 'sesion iniciada' donde te muestra todos los datos ingresados y ademas la lista de objetos comprados(vacia) donde hay un boton para crear objetos. Este te redirige a crear objetos. En esta vista tambien se pueden visualizar los primeros 4 botones para poder desplazarse.

        Boton Acceder: Te lleva a un template que tiene un registro para iniciar secion. No va a iniciar secion si el email o la contrasenia no coincide. Lo probe ingresando varios mails y contrasenias validos, lo cual me da acceso al template donde se muestra todos los datos del usuario. Tambien lo probe ingresando email incorrectos o contrasenias incorectas, lo cualrefresca el formulario sin datos y muestra un mensaje que avisa que no se pudo ingresar. Cuando se accede es lo mismo que cuando se crea, Muestra los datos y la lista de objetos(vacia)
    
    Boton Vendedor: Te muestra el template de los vendedores. Se pueden seguir visualizando los 4 botones principales, y tambien los botones de Registro y Acceso. La funcionalidad es la misma que en los de comprador y se realizaron las mismas pruebas. Otra cosa importante que se testeo fue que no se mezclen las cuentas de Comprador y Vendedor. Cree varias cuentas de Comprador y probe el acceso en vendedor para chequear que no se esten cruzando los datos. Asi mismo probe de forma inversa, creando cuentas de Vendedor y probando el acceso en Comprador. Cuando se accede a comprador este tambien te deja ingresar nuevos objetos con el boton.

    Boton Objetos: Este nos muestra un template separado en 2 partes. 

        La primera tiene un boton agregar objeto, este nos lleva a otro template con un formulario donde vamos a poder agregar un objeto con su nombre, tipo y descripcion. Los objetos si deje que se puedan repetir, ya que considere la posibilidad de que la persona tenga 2 televisores del mismo tipo y con la misma caracteristica. Todos los campos del formulario tiene que completarse para poder crear el objeto. Cuando se crea el objeto volvemos al template principal.

        La segunda parte muestra una lista de los objetos creados, tambien podes buscar objetos o alguna letra para filtrar objetos y que muestre los deseados (Es la misma implementacion de la clase). Cuando se ingrese algun nombre que no este se mostrara un mensaje que informe que no se cuentra dicho nombre de objeto. Tambien probe en ingresar nombres de usuarios, mails, contrasenias y direcciones para testear que no se crucen con los datos de los usuarios (compradores, vendedores)

Soy conciente de que a las clases le faltan algun metodo, pero mi enfasis estuvo en la creacion de la web y en su correcto funcionamiento. Intente probar todos los casos que se me ocurrieron para ver si habia alguna fuga de informacion o saltaba algun error que impidiera el funcionamiento de la misma. 

Mi idea era poder hacer una lista de objetos para cada usuario, tanto comprador como vendedor, pero se me dificulto bastante. Tengo pensado seguir desarrollando la idea para el proyecto final en caso de que sea necesaria.

Muchas gracias por tomarse el tiempo de revisarlo y leer el Readme. :)