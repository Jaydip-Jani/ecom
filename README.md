
# ecom

ecom is a Django application for running web-based eapp. Each
Visitors can use the search button to find out how many products are present.

Quick start
-----------

1. Add "ecom" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'eapp',
    ]
    
2.Add "ecom" to your TEMPLATES setting like this:

TEMPLATES = [
    {
    'DIRS': [os.path.join(BASE_DIR, "templates")],    
     },
]

3. Include the ecom URLconf in your project urls.py like this::

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eapp.urls')),
]

4. Run ``python manage.py migrate`` to create the eapp models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a ecom (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/eapp/ to participate in the ecom.
