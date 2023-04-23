
<!-- language: lang-none -->

    ██████╗      ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗      █████╗ ██████╗ ██╗  
    ██╔══██╗     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗██║  
    ██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║    ███████║██████╔╝██║  
    ██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║    ██╔══██║██╔═══╝ ██║  
    ██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝    ██║  ██║██║     ██║  
    ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝  
                                                                                 
    ██████╗ ██████╗  ██████╗ ████████╗ ██████╗ ████████╗██╗   ██╗██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║   ██║    ╚████╔╝ ██████╔╝█████╗  
    ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║   ██║   ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  
    ██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝   ██║      ██║   ██║     ███████╗
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝    ╚═╝      ╚═╝   ╚═╝     ╚══════╝
                                                                                 
    ███╗   ███╗██████╗ ███████╗                                                  
    ████╗ ████║██╔══██╗██╔════╝                                                  
    ██╔████╔██║██████╔╝███████╗                                                  
    ██║╚██╔╝██║██╔══██╗╚════██║                                                  
    ██║ ╚═╝ ██║██████╔╝███████║                                                  
    ╚═╝     ╚═╝╚═════╝ ╚══════╝                                                                                                       

Introduction:
Welcome to the prototype repository for eliciting requirements and assessing the impact of implementing a REST API for a selection of 
internal and external stakeholders for one of my assignments. This project is built on the Django framework and is my opinionated take 
on how the API should work for this specific project.

The purpose of this repository is to serve as a starting point for exploring the implementation of a REST API and gathering feedback from stakeholders. 
It is designed to be a collaborative effort that involves the entire team, with a focus on refining and further deliberating on the requirements and 
impact of the API implementation.

While this prototype takes a stance on how the API should work, it serves a starting point for further refinement and improvement based on 
stakeholder feedback. I encourage all stakeholders to provide their input and participate in the development of this prototype, so 
that we can create an API that truly meets the needs of all involved.

Outline of the repo:

<!-- language: lang-none -->
    repo/
    ├─ prepoc/ --> dir containing my implementation of the django code
    │  ├─ __pycache__/
    │  ├─ migrations/
    │  ├─ templates/
    │  │  ├─ docs.html --> previous template file, not using now
    │  │  ├─ swagger-ui.html --> template file for setting up the swagger for demos
    │  ├─ admin.py
    │  ├─ asgi.py
    │  ├─ models.py
    │  ├─ serializers.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  ├─ views.py
    │  ├─ wsgi.py
    │  ├─ __init__.py
    ├─ .gitignore
    ├─ dataGenerator.R --> R script for generating the fake data used in this project
    ├─ PoC.drawio --> drawio to outline the proces
    ├─ README.txt --> this file :)

Resources used: 
Django: https://www.django-rest-framework.org/
Tutorial: https://www.youtube.com/watch?v=i5JykvxUk_A&t=218s
Swagger: https://www.youtube.com/watch?v=JC6gHKeegk4
Swagger gist: https://gist.github.com/dotja/6da4783e3f1f1e1dd569a116660e9c42


Commands:
start venv:   `. .venv/bin/activate`
stop venv:    `deactivate`
start server: `python manage.py runserver`
migrate:      `python manage.py makemigrations` / `python manage.py migrate`
superuser:    `python manage.py createsuperuser`



