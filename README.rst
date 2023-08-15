mozilla-django-oidc-demo
====================================
* This repository for mozilla-django-oidc.
* PyPI https://pypi.org/project/mozilla-django-oidc/
* Github https://github.com/mozilla/mozilla-django-oidc
* Readthedocs https://mozilla-django-oidc.readthedocs.io
* Mozilla https://infosec.mozilla.org/guidelines/iam/openid_connect.html

Demo python django app installation
====================================
* Get repo and runserver.

.. code::

    $ python3.9 -m venv /tmp/mozilla-django-oidc-demo && source /tmp/mozilla-django-oidc-demo/bin/activate
    $ git clone https://github.com/andcolombia/libreria-django-python-auth
    $ cd mozilla-django-oidc-demo
    $ pip install setuptools --upgrade && pip install pip --upgrade
    $ pip install -r requirements.txt
    $ cp .env.sample.google .env  # Please check env variables.
    $ python manage.py migrate
    $ python manage.py runserver 127.0.0.1:8000

* Access with your browser.

.. code::

    http://localhost:8000/

.. code::

    # Example

    $ cp .env.sample.line .env

