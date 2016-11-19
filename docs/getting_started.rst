Getting started
===============

Brink requires Python 3.6 which at the moment of writing is not yet released. However, the proposed
development setup uses Docker_ to setup the development environment meaning you don't have to worry about it.

If you do want to run it locally, you can install the dev version of Python 3 on MacOS like so

``brew install --devel python3``

Install brink
-------------

``pip3 install brink``


Start a project
---------------
Starting a project is as simple as running a command and you're good to go. Note, that
as previously noted, you need Docker_ in order to enjoy this no-setup setup. ::

   $ brink start-project myproj
   $ cd myproj
   $ brink run --docker --db --debug

.. note:: If you're running MacOS or Windows, in order for the autoreload feature to work, be sure to use Docker for Mac or Windows rather
   than the a Docker host setup by docker-machine or otherwise. 

Which will create the inital project structure as such::

   ├── myproj
   │   ├── __init__.py
   │   ├── handlers.py
   │   ├── models.py
   │   └── urls.py
   └── settings.py

.. Docker: https://docker.com
