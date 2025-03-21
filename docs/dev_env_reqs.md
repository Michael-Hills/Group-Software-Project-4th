# Development Environment and its Requirements:

It is strongly recommended that developers follow the installation guide present [here](docs/CoLab%20Documentation.pdf). Alternatively, an individual should simply download and install Python 3.10 from the official website, ensuring to add Python to PATH. Then clone the repository (detailed below) and then install the necessary dependencies from the project using Python's PIP package manager. Developer-level instructions are below:

Note: Further development of the program requires basic knowledge and understanding of Django. It is highly recommended to follow the tutorial to [understand the basics](https://www.djangoproject.com/start/) before making changes.

# Setup Instructions:

1. For development, it is strongly recommended to use the "git clone" command to update the project in a chosen local directory:

      ```git clone https://github.com/2023-24-UoE-ECMM427/mental-health.git```

2. As previously mentioned, Python 3.10 is used, and the requirements are found in "requirements.txt", they can be installed by:

      ```pip install -r requirements.txt```

3. Once both commands have been successfully run, the project is ready to run. To verify this, navigate to the "mh" folder within the directory and run:

      ```python manage.py runserver```

Once run, this will start the project, navigate to your localhost to view the site.

# Development Instructions:

The repository structure is detailed [here](rep_layout_testing.md). It follows standard Django practice for each "module" of code. An excellent guide is provided [here](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8) which fully explains each critical component for development and extension.
