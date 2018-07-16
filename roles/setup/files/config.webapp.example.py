config = {
    # Create an app over here https://discordapp.com/developers/applications/me
    # and fill these fields out
    'client-id': "Bot - Client ID",
    'client-secret': "Bot - Secret",
    'bot-token': "Bot - Token",

    # Rest API in https://developer.paypal.com/developer/applications
    'paypal-client-id': "PayPal -  Client id",
    'paypal-client-secret': "PayPal -  Client secret",

    # V2 reCAPTCHA from https://www.google.com/recaptcha/admin
    # reCAPTCHA v1 is out of date and will not work with Titan Embeds, do not attempt to use reCAPTCHA v1 as it has been discontiuned by Google.
    # https://i.imgur.com/Rm2NDnV.png
    'recaptcha-site-key': "reCAPTCHA - v2 Site Key",
    'recaptcha-secret-key': "reCAPTCHA - v2 Secret Key",

    # Patreon from https://www.patreon.com/portal
    'patreon-client-id': "Patreon client id",
    'patreon-client-secret': "Patreon client secret",

    # The app-location is where the website will be located.
    # In app-secret, you may type what ever you want to
    'app-location': "/var/www/Titan/webapp/",
    'app-secret': "Type random things in this field",

    # Do not mess with database-uri and redis uri
    # websockets-mode: recommended to use eventlet
    'database-uri': "driver://username:password@host:port/database",
    'redis-uri': "redis://",
    'websockets-mode': "LITTERALLY None or eventlet",
}
