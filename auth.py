# -*- coding: utf-8 -*-
"""auth"""


import sqlite3
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.conf import settings
from django.http import HttpResponse
 

class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    """CustomOIDCAuthenticationBackend"""
    


    def create_claims(conn, claims,email):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = 'update app_user set data_claims=? where email=?'
        cur = conn.cursor()
        cur.execute(sql,(claims,email))
        conn.commit()
        conn.close()
        


    def create_connection():
        """ create a database connection to the SQLite database
            specified by db_file
        :return: Connection object or None
        """
        conn = None
        conn = sqlite3.connect("db.sqlite3")
        
        return conn

    def get_email(self, claims):
        #print("1---------",claims)
        claims_txt=str(claims)
                #print("1---------",usuario)
        email = claims.get('email')
        """
        conn = sqlite3.connect("db.sqlite3")
        sql = 'update app_user set data_claims=? where email=?'
        cur = conn.cursor()
        cur.execute(sql,(claims_txt,email))
        conn.commit()
        """
        sql="select data_claims from app_user where email='"+email+"'"
        conn = sqlite3.connect("db.sqlite3")
        cur = conn.cursor()
        res =cur.execute(sql)
        print(res.fetchone())

        conn.close()

        if not email:
            email = claims.get('sub')
        return email

    def filter_users_by_claims(self, claims):
        """Create user with email base custom user model."""
        #print("2---------",claims)
        email = self.get_email(claims)
        if not email:
            return self.UserModel.objects.none()
        try:
            return self.UserModel.objects.filter(email=email)
        except self.UserModel.DoesNotExist:
            return self.UserModel.objects.none()


    def create_user_1(self, claims):
        """ Overrides Authentication Backend so that Django users are
            created with the keycloak preferred_username.
            If nothing found matching the email, then try the username.
        """
        user = super(CustomOIDCAuthenticationBackend, self).create_user(claims)
        #user.first_name = claims.get('PrimerNombre')
        #user.last_name = claims.get('family_name' )
        #user.email = claims.get('email')
        user.is_staff = True #Here the fix that error
        #user.username = claims.get('preferred_username')
        user.save()
        
        print("creando usuario .......... "+user)

        return user

     
    def create_user(self, claims):
        """Create user with email base custom user model."""
        email = self.get_email(claims)
        return self.UserModel.objects.create_user(email)
        """ Overrides Authentication Backend so that Django users are
            created with the keycloak preferred_username.
            If nothing found matching the email, then try the username.
        
        print("3---------",claims)
        user = super(CustomOIDCAuthenticationBackend, self).create_user(claims)
        user.first_name = claims.get('PrimerNombre', '')
        user.last_name = claims.get('SegundoNombre', '')
        #user.email = claims.get('email')
        user.is_staff = True #Here fix that error
        user.username = claims.get('preferred_username')
        user.save()
        
        return user
        """
    # def verify_claims(self, claims):
    #     """Verify the provided claims to decide
    #     if authentication should be allowed."""
    #     scopes = self.get_settings('OIDC_RP_SCOPES')
    #     if not scopes:
    #         return False
    #     elif 'offline' in scopes.split():
    #         return 'offline' in claims
    #     return False
