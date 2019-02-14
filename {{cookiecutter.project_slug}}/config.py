"""
Page mappings config
--------------------
Here you can define all your page mappings with path and optionally a
class_page if you want your specific page object implementation.
By default the :py:class:`.pages.BasePage` will be instanciated.

For example you could configure your own page object implementations:

.. code-block:: python

    PAGE_MAPPINGS = {
        'HomePage': {'path': '/'},
        'HelloPage': {'path': '/hello'},
        'AnotherPage': {'path': '/anotherpage', 'class_page': AnotherPage},
        'AnotherPage': {
            'path': '/myfleet/cnh/app/view/io_profile.html',
            'page_class': {'skin1': ListingPage,
                           'skin2': Listing2Page,
                           'fallback': ListingPage},
            'links': {'edit': 'DigitalInputEditPage'}},
    }


This is only an example, you can also decide to add extra optional info such
as ``links`` that tells you where the current page leads you to another
page or whatever you want.
"""

# Here we define the fallback page object classes if you don't specify
# in PAGE_MAPPINGS any class
DEFAULT_PAGES = {
    'skin1': '.pages.BasePage',
}


PAGE_MAPPINGS = {
    'HomePage': {'path': '/'},
    'LoginPage': {'path': '/'},
}
