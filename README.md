# hyazinth
A vessel for the future ⛵


# Current list of modules and to do's

## User Management (accounts)

As a user on the Hyazinth I want to...

* register on the website
    * Depending on who I am I want to register as a...
        * Admin (StaFü, Stellv. StaFü, Kassenwart, Technical Admins)
        * FüRü Mitglied (Ämter (aktiv & passiv), Beauftratge)
        * Gruppenmitglied (Sippling und Wölfling)
        * Elternteil
        * Gastzugang
    * Password change -> django.contrib.auth
    * Password reset -> django.contrib.auth, BUT needs mailing capabilities!
* log in using my credentials
    * ID: E-Mail adress
    * Password: something complex
* log out 
    * be redirected to the front page

## Fahrten
* Create new Fahrt
* Search capability

## Dark Mode Support
Weil wichtig.




# Zettelkasten

* Django hat in contrib.auth viele vordefinierte Views und Funktionen. Auch Password change, was die Django Admin look and feel hat. Zum Ändern:
If you want to customize these two password change pages to match the look and feel of your website, it is only necessary to override the existing templates. Django already provides us with the views and URLs. To do this, create two new template files in the registration directory:

    templates/registration/password_change_form.html
    templates/registration/password_change_done.html
