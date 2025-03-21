# Mental Health Support Project Executive Summary
CoLab is an Exeter based charity which supports people with a complex multitude of issues. Supporting these individuals is a difficult task, and the NHS' system isn't currently set-up to tailor to each individual. CoLab aims to collaborate various charities and trusts together, so an individual can get all the support they need without getting lost in the system. CoLab's approach relies on truly understanding an individual's situation and colaborating together to support them in the best way possible. 

Currently, CoLab's patient data is stored in a spreadsheet. This makes it exteremely challenging for staff to stay ontop of the situation of each client, and monitor them effectively. It also leaves minimal data recorded to be analysed. The underlying efforts of CoLab is to investiagte whether certain methods help individuals more than others. For example, CoLab holds frequent workshops where individuals meet and complete a range of activities. Some improvement has already been seen; The waiting list for the Clocktower GP surgery was reduced by 56%, and for those monitored by the team, attendance at A&E dropped by 55%, showing that their mental health needs were being more appropriately met.

This project aims to deliver three main improvements over the exisitng spreadsheet: database conversion, increased data monitoring and an intuitive user interface. The database conversion will allow for increased efficiency for staff working with the system, as well as an extra layer of security, due to the database being encrypted. This in turn leads to increased data monitoring abilities, as fields can easily be added to collect more data should the client wish. Lastly, providing an intuitive user interface is paramount to this project's success, as anything less will render the system unusable.

The project has been created as a Django project, written in Python 3.10. Once the user has logged-in, the site is split up into 4 main components. Profiles, Workshops, Data Analysis and RAC form. Profiles will allow the client to easily view all the relevant data on a client at a glance, something they weren't previosuly able to do. Workshops allows for custom workshops to be recoreded, along with attendance monitoring. Data analysis allows for the client to quickly and easily generate graphs based on the recorded individuals data, to be able to see their progress. The RAC form is the main method of adding data to the database. Previosuly this was done on pen and paper, but this has been digitised for the current system.

The project is expected to be run locally on a Windows machine, and additionaly work would have to be undertaken to convert this to another operating system, or host this in the cloud.

## **Submission Document Links:**
*  Software Architecture and Development
    * [System Architecture](docs/architecture/README.md)
    * [Development Environment and its Requirements](docs/dev_env_reqs.md)
    * [Repository Layout and Test/CI Setup](docs/rep_layout_testing.md)
    * [Training Data](docs/training_data.md)
    * [Source Code Documentation](docs/decisions/0000-license-decision.md) and [Licence](LICENSE)
    * [Software Bill of Materials](docs/software_bom.xlsx)
*  Installation, Operations and Maintenance (All contained within the same file)
    * [System requirements](docs/CoLab%20Documentation.pdf)
    * [Installation](docs/CoLab%20Documentation.pdf)
    * [Usage Guide – First Steps](docs/CoLab%20Documentation.pdf)
    * [Maintenance](docs/CoLab%20Documentation.pdf)

## **Name of the developers:**
* Harvey Bellini
* Michael Hills
* Theo Dal Pozzo Dos Santos
* Pedro Pereira
* Joshua Prout

**Licence of the project:** 
GNU General Public License v3.0

**Used/required technologies and/or tools**

| Name                    | Version  | Note                                                        |
|-------------------------|----------|-------------------------------------------------------------|
| Python                  | 3.10     | The program will need modification to work with newer versions of Python |
| Django                  | 4.1.6    | Framework for development                                   |
| matplotlib              | 3.6.3    | Package used for generating graphs                          |
| pandas                  | 1.5.3    | Package for data forms                                      |
| seaborn                 | 0.13.2   | Package for graph generation                                |
| django-multiselectfield | 0.1.12   | Plugin for multi-select fields in Django forms              |
| django-filter           | 23.5     | Library for filtering Django QuerySets based on user selections |
| reportlab               | 4.1.0    | Library for PDF generation in Django                        |
| django-auto-logout      | 0.5.1    | Middleware for automatically logging out inactive users     |
| django-cryptography     | 1.1      | Provides cryptography tools for Django models               |
| django-admin-logs       | 1.2.0    | Plugin for tracking admin site activities                   |
| numpy                   | 1.26.4   | Fundamental package for scientific computing in Python      |
