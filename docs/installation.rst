Installation
============

Recipe Monkey runs as an instance of Django.  It can be run on a local machine through the built-in development server or deployed as a web service.  The recommended installation procedure described below uses pip, a python virtual environemnt, git and fabric to deploy Recipe Monkey to a server running Apache2 and mod_wsgi

Requirements
++++++++++++

* Python
* pip
* virtualenv and virtualenv wrapper
* git
* fabric
* For production: apache2, mod_wsgi

Procedure
+++++++++

1. Ensure the machine has met the installation requirements (outside the scope of this document)

2. Clone the latest version:

	$ git clone git://github.com/vanessacochrane/Recipe-Monkey.git recipemonkey
	
	$ cd recipemonkey
	
3. Update the sub repository, fabtools:

	$ git submodule init
	
	$ git submodule update
	
4. Edit fabfile.py, settings_development.py, settings_staging.py and settings_production.py to meet your system requirements.

5. Setup the server (create directories, create virtualenv, install requirements, syncdb, collectstatic)

	$ fab production setup

	
	
