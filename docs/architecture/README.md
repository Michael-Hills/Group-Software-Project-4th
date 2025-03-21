Our system architecture is split into three main components: Client, Database and Server.

When the server is accessed, the Django runtime container handles the incoming HTTPS request, and sends the user to the login page.
In order to proceed to access the server, a valid username and password must be entered, if not, the client cannot access the program functionality.
Once the client has entered valid credentials, they are able to access the program in it's entirety.
Most, if not all, of the program functionality relies heavily on the database, which contains all the necessary personal data. 

A diagram of the system can be seen below, detailing the layout of the project, as explained above.
![image](https://github.com/2023-24-UoE-ECMM427/mental-health/assets/19893000/eaf26cbc-ce9c-44bc-87a7-81384f308d98)



The low level functionality of a django app does not sit inside the scope of this element of submission, but can be accessed here:
![image](https://github.com/2023-24-UoE-ECMM427/mental-health/assets/19893000/93ac9d4d-3eec-4c08-9d5a-ce956cebfc2f)

