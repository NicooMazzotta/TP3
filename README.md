# TP3
Este proyecto web fue desarrollado utilizando el framework Django.

El proyecto consiste en una aplicación web que permite a los usuarios registrarse como Usuarios, acceder a sus cuentas, publicar objetos para vender y comprar. También pueden editar sus perfiles, agregar imágenes y utilizar un sistema de mensajería entre usuarios.

La página de inicio cuenta con 3 botones principales:

    Botón "Inicio": Este botón está presente en todos los templates y te lleva de vuelta a la página de inicio. Dependiendo si estás o no logueado, el mensaje del botón cambia.

    Botón "Acerca de mí": Muestra un pequeño recorrido por mis estudios en programación y lo que me gustaría estudiar en el futuro. También incluye un video explicativo.

    Botón "Usuarios": Este botón te lleva a un template donde encontrarás 2 botones adicionales.

        Botón "Registrar": Te lleva a un formulario donde los usuarios/compradores pueden registrarse. El formulario incluye 4 campos obligatorios (Email, usuario, contraseña y repetir contraseña). Está basado en la vista de registro de perfiles. Una vez que se crea el perfil, te redirige a otro template para acceder a la cuenta.

        Botón "Acceder": Te lleva a un formulario de inicio de sesión. No permitirá el acceso si el email o la contraseña no coinciden. Una vez que inicias sesión, se mostrarán los demás botones.

Una vez que la sesión está iniciada, se despliegan los demás botones. Los botones "Inicio" y "Acerca de mí" siguen presentes. A partir de ahora, se mostrarán los siguientes botones:

    Botón "Desconectar": Cierra la sesión actual y oculta los demás botones. Para volver a verlos, deberás acceder a tu cuenta nuevamente.

    Botón con el nombre del usuario: Accede al template de perfil, donde se muestra la información del usuario, como el nombre de usuario, nombre, apellido, email y foto de perfil (si el usuario tiene una foto cargada). En esta ventana, se encuentran 2 botones:

    Botón "Editar Datos": Te lleva a un formulario donde puedes modificar campos opcionales que no son requeridos al registrarse, como el nombre, apellido y la foto de avatar. No es posible cambiar el nombre de usuario para evitar problemas futuros. Los datos previamente ingresados se siguen visualizando hasta que los cambios se confirmen. Al presionar el botón "Guardar cambios", se regresa a la vista del perfil.

    Botón "Editar Contraseña": Te lleva a un formulario donde debes ingresar la contraseña actual y dos veces la nueva contraseña. Una vez confirmados los cambios, se regresa a la vista del perfil.

Ahora llegamos a las funcionalidades más interesantes, los botones en los que se dedicó más desarrollo y donde se cumplen los requisitos para la entrega final.

    Botón "Objetos": Este botón te lleva a un template donde puedes vender y comprar objetos.

    "Vender Objetos": Aquí se encuentran dos botones adicionales que se explicarán más adelante: "Publicar Objeto" e "Historial de Objetos Vendidos". Al desplazarse hacia abajo, encontrarás una lista con los objetos que has publicado hasta el momento. Puedes buscar objetos por su nombre en esta lista. Los objetos se muestran con su foto, nombre, valor y fecha de publicación. También puedes ver otros 3 botones:

    "Eliminar Publicación": Al presionar este botón, se mostrará un template que te pregunta si estás seguro de eliminar el objeto. Si confirmas la eliminación, el objeto se borra de la base de datos y ya no se mostrará en la lista ni en los objetos disponibles para comprar. Al confirmar, regresarás a la vista de la lista de objetos.

    "Modificar Objeto": Aquí puedes cambiar todas las características del objeto, como la imagen, nombre, precio, tipo y descripción. La descripción permite incluir todas las características del producto con un richfield. Los datos previamente ingresados se siguen visualizando antes de realizar modificaciones. Al presionar "Modificar", regresarás a la lista de objetos.

    "Mostrar Detalles": En esta opción, puedes ver más información que no se muestra en "Modificar", como el estado (si está en venta o no), el nombre del vendedor y la fecha de publicación.

    "Historial de Objetos Vendidos": En este template, puedes visualizar los objetos que has vendido previamente. No puedes eliminar ni modificar estos objetos, solo puedes ver los detalles de los objetos que alguna vez publicaste. También cuenta con un formulario de búsqueda para buscar objetos vendidos.

A continuación, se encuentra la sección de "Comprar Objetos". Aquí puedes ver todos los objetos publicados por todos los usuarios. También encontrarás el botón "Mostrar Detalles", que tiene la misma funcionalidad que los anteriores.

    "Botón Comprar": Este botón te lleva a una vista de confirmación de compra, donde se mostrará el nombre y el precio del objeto. Al aceptar, regresarás a la vista de objetos publicados. Una vez que hayas realizado la compra, el objeto cambiará su estado de "en venta" a "vendido". Ya no aparecerá en la lista de objetos publicados del vendedor y se agregará a la lista de objetos comprados por el usuario.

    "Historial de Objetos Comprados": Esta opción te muestra una lista de los objetos que has comprado y sus detalles. También puedes buscar objetos por su nombre en esta lista.

Botón "Mensajes": Para esta funcionalidad, implementé dos clases: "Chat" y "Mensaje".

    "Chat": Tiene dos claves foráneas relacionadas con dos usuarios: el remitente y el destinatario. Estas claves vinculan el chat entre ellos y crean un chat "único" para cada usuario. Utilicé la duplicación del chat para implementar una funcionalidad de eliminación de mensajes y chats (similar a WhatsApp). Si uno de los usuarios elimina un mensaje o el chat, el otro usuario todavía mantendrá su copia. Además de las claves, el chat tiene un estado de leído, que se utiliza para notificar al usuario sobre nuevos mensajes que aún no ha leído, tanto en la vista previa como en el menú de inicio de mensajes. También cuenta con una fecha de actualización para ordenar los chats por los más recientes en una lista de chats del usuario. El modelo cuenta con dos métodos: __str__ para mostrar cómo se devuelve el modelo y meta que ayuda a ordenar los chats.

    "Mensaje": Este modelo tiene una clave foránea que relaciona el mensaje con un chat, el remitente que indica quién envió el mensaje, el contenido que muestra el contenido del mensaje y la fecha de envío que muestra la hora en la que se publicó el mensaje. El modelo también cuenta con dos métodos: __str__ y mostrar_fecha_hora que devuelve la fecha y la hora como un string.

El template comienza mostrando un mensaje que indica la cantidad de mensajes sin leer que tienes o si no hay ninguno. Al desplazarse hacia abajo, se encuentra el primer botón:

    "Enviar Nuevo Mensaje": Este botón te lleva a una lista de todos los usuarios registrados en la página, donde se muestra el botón "Enviar Mensaje" junto a cada usuario.

    "Enviar Mensaje": Al presionar este botón, se accede al template del chat. Aquí se muestran todos los mensajes existentes (si los hay). Los mensajes se muestran con el siguiente formato: remitente - contenido - fecha y hora de envío - barra de separación entre mensajes. Al final de los mensajes, tanto del remitente (que aparecerá como 'tu') como del destinatario (nombre de usuario), se muestra un formulario para escribir y enviar un nuevo mensaje. Al enviar el mensaje, la página se actualiza para mostrar el nuevo mensaje enviado. Cuando se envía un mensaje, se actualiza el estado del chat paralelo del otro usuario, que pasará a ser "no leído" y se mostrará en el menú de inicio de mensajes.
    
Al desplazarse más hacia abajo, se encuentra la sección de "Chats", donde se muestran todos los chats existentes. Para que aparezcan en esta sección, es necesario haber accedido al chat para crearlo. Cada chat tiene un botón "Ir al Chat" que te redirecciona al chat correspondiente. Además, al lado del nombre del chat, se muestra si hay mensajes sin leer.

Hasta aquí las funcionalidades de la página. Espero haberme explicado de manera clara en esta sección. En el video que se debe subir, mostraré el funcionamiento de estas funcionalidades. ¡Muchas gracias por llegar hasta aquí! Si tienes alguna consulta sobre el código, no dudes en preguntar, ¡estaré encantado de explicarlo!

Aca el link:
https://www.youtube.com/watch?v=3hh6dob7QvE