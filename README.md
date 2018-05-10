# Team44Repo
Twitter,Aurin Analysis
Authors
Arwinder Singh
Yogesh C Kumaravel
Ti Wang 
Sisi li
Sree Sai Vatsav
Ansible script should be used to install required softwares.
CollectOtherTweet.py got the starting code to manually run the other related classes, for
specific functionalites.


## Website 

To briefly visualize the data and research we made, we use Django to design a simple website. 

Run the web application locally,

    python manage.py runserver # 127.0.0.1:8000

Django is a MVC framework, so we assign url to each page and initialize models for different parts.
For example, to create model for each part:

    python manage.py startapp tweet

Generally speaking, after initialize the models, we create template for each page and embeded the googel charts and maps inside the HTML file. 
And define functions and set corresponding route for each page.
