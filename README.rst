=============
Pelican Slideshare
=============

Pelican Slideshare is a plugin to enabled you to embed Slideshare slides in your pages
and articles.

Installation
============

To install pelican-slideshare, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-slideshare

Then enabled it in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_slideshare',
        # ...
    ]

Usage
=====

In your article or page, you simply need to add a line to embed you video.

.. code-block:: rst

    .. slideshare:: SLIDE_ID

Which will result in:

.. code-block:: html

    <div class="slideshare" align="left">
    <iframe width="420" height="315" src="https://www.slideshare.net/slideshow/embed_code/key/SLIDE_ID" frameborder="0"></iframe>
    </div>

Additional arguments
--------------------

You can also specify a `width`, `height` and `alignment`

.. code-block:: rst

	.. slideshare:: 2UU5C0fJf2cygQ
        :width: 800
        :height: 500
        :align: center

Which will result in:

.. code-block:: html

    <div class="slideshare" align="center">
    <iframe width="800" height="500" src="https://www.slideshare.net/slideshow/embed_code/key/2UU5C0fJf2cygQ" frameborder="0"></iframe>
    </div>

License
=======

`MIT`_ license.

.. _MIT: http://opensource.org/licenses/MIT
