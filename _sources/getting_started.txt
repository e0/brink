Getting started
===============

Brink requires Python 3.6 which at the moment of writing is not yet released. However, the proposed
development setup uses Docker to setup the development environment meaning you don't have to worry about it.

If you do want to run it locally, you can install the dev version of Python 3 on MacOS like so

``brew install --devel python3``

Install brink
-------------

``pip3 install brink``


Start a project
---------------
Starting a project is as simple as running a command and you're good to go.

::

   $ brink start-project myproj
   $ cd myproj
   $ brink sync-db
   $ brink run

Which will create the inital project structure as such ::

   ├── myproj
   │   ├── __init__.py
   │   ├── handlers.py
   │   ├── models.py
   │   └── urls.py
   └── settings.py

