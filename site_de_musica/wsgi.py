import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_de_musica.settings')
application = get_wsgi_application()
