## in-house Ad System

### Install

```
$ git clone ...

$ cd pycon

$ virtualenv env --python=`which python3`

$ pip install -r adtech/requirements.txt

$ cd adtech

$ python manage.py migrate # once
```

### Run Server

```
$ cd adtech

$ python manage.py runserver

$ open http://localhost:8000
```

### Create Admin

```
$ cd adtech

$ python manage.py createsuperuser

$ open http://localhost:8000/admin
```

### Create `YOU.APPI` Campaign

```
$ cp youappi_token.txt.example youappi_token.txt

$ vi youappi_token.txt # and set valid API token
```

```
$ python manage.py runscript scripts.crawl # once

$ python manage.py runscript scripts.analyze # and open your admin page
```