# Backend For Shopping Manager
##### Built on Django and Django REST Framework

To setup the local backend follow the below steps:

1) Make sure you have **mysql** setup on your system
    -For Ubuntu, Linux Deb distributions:
        Run ```sudo apt-get install mysql-server mysql client```
        After successfull installation, 
        Run ```sudo mysql```
        Create a new database and a user and assign requisite permissions as given [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql).
2) After above steps, populate the [config.py](https://github.com/ParitoshKabra/OOAD_Project/blob/main/ooad_proj/config.py) file accordingly.

3) On Ubuntu and Linux systems, ```sudo service mysql start``` to start mysql server at the default port 3306
4) Create a virtual environment, ```python3 -m venv <env_name>```
5) Run ```pip install -r requirements.txt``` to install the requisite tools.
6) Run ```python3 manage.py makemigrations; python3 manage.py migrate```
    - Note use **python** in place of **python3** for windows.
7) ##### All set! 
You can start the development server as: ```python3 manage.py runserver```

Clone the frontend repo from [here](https://github.com/IshuGupta02/ShoppingManager-Frontend). Follow steps mentioned in it's **README.md** to setup frontend in your system.

-**Note:** ```npm start``` should start the devleopment server mentioned at any of the hosts in the **CORS_WHITELIST** [settings.py](https://github.com/ParitoshKabra/OOAD_Project/blob/main/ooad_proj/settings.py)  
