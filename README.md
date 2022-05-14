# autopros.app

## Notes
- Currently github actions are disabled.

## Description
- A prototype website for providing auto services to consumers. 
- Built with VueJs frontend and a Django backend, with a postgresql database.
- Deployed on a cloud server with a live url at https://autopros.app/log-in, which utilizes gunicorn, and nginx. 

## Features
- Supports log-in and register using token authentication.
- Uses a REST API to communicate between Django and VueJs.
- Automatically deploys changes and restarts the server on the cloud via a github actions workflow.
- Allows an admin to add, manage, view and sort car services in the business-listings page.

## Requirements
  ### Digital Ocean Droplet car-catch-prod implicit dependencies (** Separate into prod and dev**)
  - git 2.25.1
  - nginx
  - OpenSSH_8.2p1 Ubuntu-4ubuntu0.2, OpenSSL 1.1.1f 31 Mar 2020
  - postgresql 12.7 (Database)
  - postgresql-contrib
  - Python3: 3.8.5
  - pip: 20.0.2 (sudo apt install python3-pip)
  - python3-dev
  - pipenv (Used to install the django project dependencies) (pip install --user pipenv)
  - libpq-dev
  - npm (Used to install the vue project dependencies)
  - certbot
  - python3-certbot-nginx
  - Ubuntu: 20.04.01
  - supervisor (apt install supervisor)

  ### pipenv virtual environment dependencies (Django/backend)
  - Dependencies that are not installed directly on the droplet/server, but are installed at during deployment which are not needed until run-time. They       are stored within the Pipfile and Pipfile.lock in the auto_pros_django project.

  ### npm dependencies (VueJs/frontend)
  - Dependencies that are not installed directly on the droplet/server, but are installed at during deployment which are not needed until run-time. They       are stored within the package.json in the auto_pros_vue project.
