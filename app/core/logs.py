from django.conf import settings


MESSAGES_LOGS ={
    # app core
    'mensaje1':{
        'es':'Se listaron los logs',
        'en':'Logs were listed',
        'fr':'Les journaux ont été logs'
    },
    'mensaje2':{
        'es':u'Ocurrió una excepción el la vista logs',
        'en':'An exception occurred in the Logs view',
        'fr':'Une exception produite dans la vue Logs'
    },
    'mensaje3':{
        'es':u'Cuenta registrada correctamente',
        'en':'Account successfully registered.',
        'fr':'Compte enregistré avec succès'
    },
    'mensaje4':{
        'es':u'Cuenta previamente registrada',
        'en':'Account previously registered',
        'fr':'Compte précédemment enregistré'
    },
    'mensaje5':{
        'es':u'La clave no es válida, es posible que esté corrupta o que la contraseña no sea correcta',
        'en':'The key is not valid, it is possible that it is corrupt or the password is not correct',
        'fr':'La clé pas valide, il est possible quelle soit corrompue ou que le mot de passe ne soit pas correct'
    },
    'mensaje6':{
        'es':u'La validez de la firma electrónica no es válida, el período de validez comienza el {}',
        'en':'Validity of the electronic signature invalid, the period of validity begins on {}',
        'fr':'Validité de la signature électronique invalide, la période de validité commence le {}'
    },
    'mensaje7':{
        'es':u'Se produjo un error al firmar el manifiesto',
        'en':'An error occurred when signing the manifest',
        'fr':'Une erreur produite lors de la signature du manifeste'
    },
    'mensaje8':{
        'es':u'El archvio no se puede encontrar en la ruta',
        'en':'The file cannot be found in the path',
        'fr':'Le fichier est introuvable dans le chemin'
    },
    'mensaje9':{
        'es':u'Se produjo una excepción al descargar el archivo xml {}',
        'en':'An exception occurred while downloading the xml file {}',
        'fr':"Une exception s'est produite lors du téléchargement du fichier xml {}"
    },
    'mensaje10':{
        'es':u'Se produjo un error al actualizar el logotipo del cliente: {}',
        'en':"An error occurred while updating the customer's logo: {}",
        'fr':"Une erreur s'est produite lors de la mise à jour du logo du client: {}"
    },
    'mensaje11':{
        'es':u'El logotipo del cliente se ha actualizado correctamente {}',
        'en':'Customer logo has been updated successfully {}',
        'fr':'Le logo du client a été mis à jour avec succès {}'
    },
    'mensaje12':{
        'es':u'Se produjo un error al registrar la dirección: {}',
        'en':'An error occurred when registering the address: {}',
        'fr': "Une erreur s'est produite lors de l'enregistrement de l'adresse: {}"
    },
    'mensaje13':{
        'es':u'La información fiscal del cliente ha sido actualizada.',
        'en':'The client fiscal information has been updated',
        'fr':'Les informations fiscales du client ont été mises à jour'
    },
    'mensaje14':{
        'es':u'El correo electrónico se agregó correctamente {}',
        'en':'Email was successfully added {}',
        'fr':"L'e-mail a été ajouté avec succès {}"
    },
    'mensaje15':{
        'es':u'Se produjo un error al modificar el correo electrónico {}: {}',
        'en':'An error occurred when modifying email {}: {}',
        'fr':"Une erreur s'est produite lors de la modification de l'e-mail {}: {}"
    },
    'mensaje16':{
        'es':u'Se creo un nuevo email',
        'en':'A new email was created',
        'fr':'Un nouvel e-mail a été créé'
    },
    'mensaje16':{
        'es':u'Correo electrónico eliminado con éxito {}',
        'en':'Email successfully deleted {}',
        'fr':'E-mail supprimé avec succès {}'
    },
    'mensaje17':{
        'es':u'Se produjo un error al eliminar el correo electrónico {}: {}',
        'en':'An error occurred when deleting the email {}: {}',
        'fr':"Une erreur s'est produite lors de la suppression de l'e-mail {}: {}"
    },
    'mensaje18':{
        'es':u'Los certificados se registraron correctamente {} - {}',
        'en':'Certificates was successfully register {} - {}',
        'fr':'Le certificat a été enregistré avec succès {} - {}'
    },
    'mensaje19':{
        'es':u'Se produjo un error al agregar un certificado: {}',
        'en':'An error occurred when adding a certificate: {}',
        'fr':"Une erreur s'est produite lors de l'ajout d'un certificat: {}"
    },
    'mensaje20':{
        'es':u'La contraseña del cliente se actualizó correctamente',
        'en':'Client password was successfully updated',
        'fr':'Le mot de passe du client a été mis à jour avec succès'
    },
    'mensaje21':{
        'es':u'Se produjo un inconveniente al actualizar la contraseña del cliente: {}',
        'en':"An inconvenience occurred when updating the client's password: {}",
        'fr':"Un désagrément s'est produit lors de la mise à jour du mot de passe du client: {}"
    },
    'mensaje22':{
        'es':u'La serie {} se creó con éxito',
        'en':'The serie {} was created successfully',
        'fr':'La série {} a été créée avec succès'
    },
    'mensaje23':{
        'es':u'Se produjo un error al crear la serie {}: {}',
        'en':'An error occurred when creating the serie {}: {}',
        'fr':"Une erreur s'est produite lors de la création de la série {}: {}"
    },
    'mensaje24':{
        'es':u'La serie se actualizó con éxito {}',
        'en':'The serie was successfully updated {}',
        'fr':'La série a été mise à jour avec succès {}'
    },
    'mensaje25':{
        'es':u'Se produjo un problema al actualizar la serie {}',
        'en':'An issue occurred while updating the series {}',
        'fr':'Un problème est survenu lors de la mise à jour de la série {}'
    },
    'mensaje26':{
        'es':u'Se produjo un problema al cargar la sección de perfil: {}',
        'en':'An issue occurred while loading the profile section: {}',
        'fr':'Un problème est survenu lors du chargement de la section de profil: {}'
    },
    # app invoicing
    'mensaje27':{
        'es':u'Se obtuvieron un total de {} Productos o Servicios',
        'en':'A total of {} Products or Services were obtained',
        'fr':'Un total de {} produits ou services ont été obtenus'
    },
    'mensaje28':{
        'es':u'Ocurrió una excepcion en stuffs',
        'en':'An exception occurred in stuffs',
        'fr':"Une exception s'est produite dans stuffs"
    },
    'mensaje29':{
        'es':u'Las facturas fueron listadas',
        'en':'Invoices were listed',
        'fr':'Les factures ont été répertoriées'
    },
    'mensaje30':{
        'es':u'Peticion de cancelacion realizada con exito :{}',
        'en':'Request for successful cancellation: {}',
        'fr':"Demande d'annulation réussie: {}"
    },
    'mensaje31':{
        'es':u'Se descargo el XML{}',
        'en':'XML {} was downloaded',
        'fr':'XML {} a été téléchargé'
    },
    'mensaje32':{
        'es':u'Se descargo el PDF {}',
        'en':'The PDF {} was downloaded',
        'fr':'Le PDF {} a été téléchargé'
    },
    'mensaje33':{
        'es':u'Los negocios fueron listados',
        'en':'Business were listed',
        'fr':'Les entreprises ont été répertoriées'
    },
    'mensaje34':{
        'es':u'No se puede registrar el Receptor, el RFC {} no se encuentra en la BD, por favor agregue un RFC valido',
        'en':'Unable to register the Receiver, the RFC {} is not found in the DB, please add a valid RFC',
        'fr':"Impossible d'enregistrer le récepteur, le RFC {} est introuvable dans la base de données, veuillez ajouter un RFC valide"
    },
    'mensaje35':{
        'es':u'Los productos y servicios fueron listados.',
        'en':'Products and services were listed',
        'fr':'Les produits et services ont été répertoriés'
    },
    'mensaje36':{
        'es':u'Producto / Servicio registrado con éxito',
        'en':'Product/Service successfully registered',
        'fr':'Produit / service enregistré avec succès'
    },
    'mensaje37':{
        'es':u'Producto / servicio duplicado',
        'en':'Duplicate Product/Service',
        'fr':'Produit / service en double'
    },
    'mensaje38':{
        'es':u'Se produjo una excepción al registrar el producto / servicio',
        'en':'An exception occurred when registering the product/service',
        'fr':"Une exception s'est produite lors de l'enregistrement du produit / service"
    },
    'mensaje39':{
        'es':u'Producto / Servicio editado con éxito',
        'en':'Product/Service successfully edited',
        'fr':'Produit / service modifié avec succès'
    },
    'mensaje40':{
        'es':u'No se pudo obtener información del producto o servicio',
        'en':'Could not get product or service information',
        'fr':"Impossible d'obtenir des informations sur le produit ou le service"
    },
    #app support
    'mensaje41':{
        'es':u'Tickets listados correctamente',
        'en':'Tickets listed correctly',
        'fr':'Tickets correctement répertoriés'
    },
    'mensaje42':{
        'es':u'Se produjo una excepción al listar los tickets',
        'en':'An exception occurred while listing tickets',
        'fr':"Une exception s'est produite lors de la liste des tickets"
    },
    'mensaje43':{
        'es':u'Ticket creado con éxito',
        'en':'Ticket created successfully',
        'fr':'Ticket créé avec succès'
    },
    'mensaje44':{
        'es':u'Se produjo una excepción al enumerar entradas.',
        'en':'An exception occurred while listing tickets',
        'fr':"Une exception s'est produite lors de la liste des billets"
    },
    #app users
    'mensaje45':{
        'es':u'Cuenta bloqueada por múltiples intentos fallidos',
        'en':'Account blocked for multiple failed attempts',
        'fr':'Compte bloqué pour plusieurs tentatives infructueuses'
    },
    'mensaje46':{
        'es':u'Se intentó iniciar sesión con el usuario {}, y esto no existe',
        'en':'An attempt was made to log in with the user {}, and this is non-existent',
        'fr':"Une tentative de connexion avec l'utilisateur {} a été effectuée, ce qui est inexistant"
    },
    'mensaje47':{
        'es':u'Se produjo una excepción al iniciar sesión',
        'en':'An exception occurred at login',
        'fr':"Une exception s'est produite lors de la connexion"
    },
    'mensaje48':{
        'es':u'Se listaron los usuario',
        'en':'List users',
        'fr':'Liste des utilisateurs'
    },
    'mensaje49':{
        'es':u'Se produjo una excepción al listar usuarios',
        'en':'An exception occurred when listing users',
        'fr':"Une exception s'est produite lors de la liste des utilisateurs"
    },
    'mensaje50':{
        'es':u'Personalización exitosa {} => {}',
        'en':'Successful customization {} => {}',
        'fr':'Personnalisation réussie {} => {}'
    },
    'mensaje51':{
        'es':u'La información del usuario {} ha sido actualizada',
        'en':'User {} information has been updated',
        'fr':"Les informations de l'utilisateur {} ont été mises à jour"
    },
    'mensaje52':{
        'es':u'Hubo un problema al actualizar la información',
        'en':'There was a problem when updating the information',
        'fr':'Un problème est survenu lors de la mise à jour des informations'
    },
    'mensaje53':{
        'es':u'La respuesta obtenida al validar al usuario fue: {}',
        'en':'The response obtained when validating the user was: {}',
        'fr':"La réponse obtenue lors de la validation de l'utilisateur était: {}"
    },
    'mensaje54':{
        'es':u'El RFC {} fue validado correctamente',
        'en':'The RFC {} was validated correctly',
        'fr':'Le RFC {} a été validé correctement'
    },
    'mensaje55':{
        'es':u'Un nuevo usuario se registró con el correo {}',
        'en':'A new user was registered with mail {}',
        'fr':'Un nouvel utilisateur a été enregistré avec la messagerie {}'
    },
    'mensaje56':{
        'es':u'RFC {} previamente registrado',
        'en':'Previously registered RFC {}',
        'fr':'RFC précédemment enregistré {}'
    },
    'mensaje57':{
        'es':u'Usuario {} agregado correctamente {}',
        'en':'User {} added successfully {}',
        'fr':"L'utilisateur {} a bien été ajouté {}"
    },
    'mensaje58':{
        'es':u'Usuario {} previamente registrado',
        'en':'User {} already has a previous registration',
        'fr':"L'utilisateur {} a déjà un enregistrement précédent"
    },
    'mensaje59':{
        'es':u'Registrando nuevo usuario',
        'en':'Registering new user.',
        'fr':"Enregistrement d'un nouvel utilisateur."
    },
    'mensaje60':{
        'es':u'Correo inválido',
        'en':'Invalid email',
        'fr':'Email invalide'
    },
    'mensaje61':{
        'es':u'Se produjo un error al realizar la operación.',
        'en':'An error occurred while performing the operation',
        'fr':"Une erreur s'est produite lors de l'exécution de l'opération"
    },
    'mensaje62':{
        'es':u'El usuario está registrado con otra cuenta',
        'en':'The User is registered under another account',
        'fr':"L'utilisateur est enregistré avec un autre compte"
    },
    'mensaje63':{
        'es':u'La contraseña debe tener al menos 8 carácteres entre mayúsculas, minúsculas, dígitos y un carácter especial.',
        'en':'The password must have at least 8 uppercase, lowercase characters, digits and a special character.',
        'fr':'Le mot de passe doit comporter au moins 8 majuscules, minuscules, chiffres et un caractère spécial.'
    },
    'mensaje64':{
        'es':u'Seleccione el recaptcha',
        'en':'Select the recaptcha',
        'fr':'Sélectionnez le recaptcha'
    },
    'mensaje65':{
        'es':u'Correo de activación enviado',
        'en':'Reactivation email sent',
        'fr':'E-mail de réactivation envoyé'
    },
    'mensaje66':{
        'es':u'Espera al menos 30 minutos para reenviar la solicitud',
        'en':'Wait at least 30 minutes to resend the request',
        'fr':'Attendez au moins 30 minutes pour renvoyer la demande'
    },
    'mensaje67':{
        'es':u'El usuario {} ingresó una contraseña incorrecta ({} intento)',
        'en':'User {} entered an incorrect password ({} attemp)',
        'fr':"L'utilisateur {} a entré un mot de passe incorrect ({} attemp)"
    },
    'mensaje68':{
        'es':u'El usuario {} inicio sesión',
        'en':'User {} login',
        'fr':'Utilisateur {} en ligne'
    },
    'mensaje69':{
        'es':u'El usuario {} cerro sesión',
        'en':'User {} logout',
        'fr':"Déconnexion de l'utilisateur {}"
    },
    
}