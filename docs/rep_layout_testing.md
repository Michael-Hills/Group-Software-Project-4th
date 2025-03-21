# Repository Layout and Test/CI Setup

## Repository Layout

The repository structure is set up as the following. The "requirements.txt" file contains all the project requirements. The "README.md" details the premise of the project, the links to relevant files and other important information. The "LICENSE" file details the license selected for this project and the "gitignore" file is for ignoring files for GitHub uploads. There are then two main folders: "docs" and "mh".

The "docs" folder contains all the relevant documentation for the project. The main item of importance is "Colab Documentation.pdf" which details the installation, operation and usage guide for the project. Other documents are of lesser importance.

The main code is contained within the "mh" file which is split into several sub folders. Within the "mh" folder is the database: "db.sqlite3", Django's "manage.py" file and the Colab logo. The "base" file contains the code for the Profiles, Workshops and Data Analysis elements of the project whilst "rac" contains the RAC form. The "mh" subfolder contains several Django critical files, including "settings.py". Additionally, there is a "templates" folder, containg the main HTML templates for the project and navbar. 


## Test/CI Setup

For the project we implemneted various strict testing criteria. Our initial testing criteria is database specific and is contained within "mh/base/tests.py". The file contains unit tests that test the database operations when the project is run, to ensure that database operations are as expected, before modifying any fields. Failure of these unit tests notifies the client and suggests that a backup database be restored.

Secondly, we implemented branching. Each new feature is assigned a new branch, so that coding can be done both simultaneously and effectively. This ensured that our code was written independetly, and we could ensure feature functionality before integrating it within the main branch.

Coupled with branching, we utilised manual integration testing when using pull requests. This means that another person must read, test, and verify any new code entering the main branch. This rule ensures that coding works on multiple environments, and ensure it works within the main branch. This also stops the flow of low quality code entering the "production" environment.

As the RAC form functionality is a database specific task, this was given its own subfolder, making any problems that arise easier to diagnose, due to localised programming. It is strongly recommended that any new additions to the codebase be created in a similar fashion, making a potential rollback easier to implement.

