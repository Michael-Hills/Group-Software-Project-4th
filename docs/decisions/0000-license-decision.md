The license chosen for this project is the GNU, General Public License (GPL) version 3. The reasonings for this are outlined below:

*  In all cases, the licenses used by each software component (i.e. PSF-2.0, 0GSD, BSD-3-Clause and GPL-2.0-or-later) are all GPL compatible. Therefore, there are no dependencies that stop this project from being released under GPL.

Currently, the client plans to locally host the project. However, to give the client more freedom in how they can use this project, option 1 was picked to allow for the web-application to be publicly available at no extra cost to the client.

* Potential for a future student group to extend on this project has been discussed with the client. As this project is licensed under GPL, the source code is publicly available and can be modified and offered to others without the need to release any changes to customers, allowing for future groups to easily continue from the work in this project and make their own decision on how to distribute their version.
  
* As the client is a charity, it is important to ensure that the source code in this project remains free. By using a GPL license, the source code cannot be turned into a paid closed source product.
<h3>Appendix</h3>
<h4>Software Inventory</h4>

| Component Name           | Vendor                                                                                            | Version | End of Life   | License (SPDX)   | License Model   | Dependency Type       | Additional Notes                        |
|--------------------------|---------------------------------------------------------------------------------------------------|---------|---------------|------------------|-----------------|-----------------------|-----------------------------------------|
| Python                   | [https://www.python.org/downloads/](https://www.python.org/downloads/)                            | 3.9     | 05/10/2025    | PSF-2.0 and 0BSD | Perpetual, Free | Development & Runtime | Duel license                            |
| Django                   | [https://www.djangoproject.com/download/](https://www.djangoproject.com/download/)                | 4.2     | 01/04/2026    | BSD-3-Clause     | Perpetual, Free | Development & Runtime |                                         |
| NumPy                    | [https://numpy.org/install/](https://numpy.org/install/)                                          | 1.26    | 17/09/2025    | BSD-3-Clause     | Perpetual, Free | Development & Runtime | Requires python 3.9.x or newer          |
| Pandas                   | [https://pandas.pydata.org/](https://pandas.pydata.org/)                                          | 2.1.2   | Not specified | BSD-3-Clause     | Perpetual, Free | Development & Runtime |                                         |
| matplotlib               | [https://matplotlib.org/stable/users/installing.html](https://matplotlib.org/stable/users/installing.html) | 3.6.3   | Not specified | BSD-3-Clause | Perpetual, Free | Development & Runtime | Visualization library                  |
| seaborn                  | [https://seaborn.pydata.org/installing.html](https://seaborn.pydata.org/installing.html)          | 0.13.2  | Not specified | BSD-3-Clause     | Perpetual, Free | Development & Runtime | Statistical data visualization         |
| django-multiselectfield  | [https://pypi.org/project/django-multiselectfield/](https://pypi.org/project/django-multiselectfield/) | 0.1.12  | Not specified | LGPL-3  | Perpetual, Free | Development           | Enhances Django's multiple choice field |
| django-filter            | [https://django-filter.readthedocs.io/en/stable/](https://django-filter.readthedocs.io/en/stable/) | 23.5    | Not specified | Not specified  | Perpetual, Free | Development           | Dynamic queryset filtering for Django   |
| reportlab                | [https://www.reportlab.com/opensource/](https://www.reportlab.com/opensource/)                    | 4.1.0   | Not specified | BSD              | Perpetual, Free | Development           | PDF generation in Python               |
| django-auto-logout       |[https://pypi.org/project/django-auto-logout/](https://pypi.org/project/django-auto-logout/) | 0.5.1   | Not specified | MIT     | Perpetual, Free | Development           | Auto logout for Django apps            |
| django-cryptography      | [https://github.com/georgemarshall/django-cryptography](https://github.com/georgemarshall/django-cryptography) | 1.1     | Not specified | BSD-3-Clause     | Perpetual, Free | Development           | Encryption fields for Django models    |
| django-admin-logs        | [https://pypi.org/project/django-admin-logs/](https://pypi.org/project/django-admin-logs/)   | 1.2.0   | Not specified | MIT     | Perpetual, Free | Development           | Admin action logs for Django           |
