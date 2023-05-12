# Davaat-BackEnd-API-Service
The contract registration system
<hr>


Davaat BackEnd API Service in **Django** Framework. [Nima Dorostkar](https://nimadorostkar.com/)


### Clone this repository

```
rm -rf
```

```
git clone https://github.com/davaat/Davaat-BackEnd-API-Service.git
```


#### Pip
```bash
pip install -r requirements.txt

```

#### Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

<br>

![davaat](https://github.com/davaat/Davaat-BackEnd-API-Service/blob/main/Screenshot.png)


<br><br>



Build code with docker compose
```
docker-compose build
```

Run the built container
```
docker-compose up -d
```



Build the image and spin up the containers:
```
docker-compose up -d --build
```



Migrate databases
```
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```


Migrate all apps at the same time
```
docker-compose exec app python manage.py makemigrations authentication contract landing signature reminders message subscription
```




Collect static files
```
docker-compose exec app python manage.py collectstatic
```



Create super user
```
docker-compose exec app python manage.py createsuperuser
```


