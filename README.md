# Wedding photo galery API
API Available on Heroku at [https://gallery-fns-api.herokuapp.com/docs/](https://gallery-fns-api.herokuapp.com/docs/)

Website available on Heroku at [https://gallery-fns-vuejs.herokuapp.com/](https://gallery-fns-vuejs.herokuapp.com/)


You got a request from a friend to create a gallery for his wedding where his friends will be able to upload their photos and he will have a unified gallery with all friend's photos.
He wants to be able to approve the photos before being visible to everyone. He and his wife should be the only ones able to approve new photos.
Users must be able to like photos and add comments to photos.

## Stack used
* Python
* Django
* Django Rest Framewrok
* Mongodb
* Heroku
* AWS S3
* Cloud.mongodb.com
* Swagger


## How to run the project

1. Create a virtualenv python 3.8
2. Activate your virtualenv
3. Install dependencies (gunicorn is not necessary to local development)
4. Configure the instance with .env file
5. Run Mongodb using docker (recommended)
6. Run the migrations
7. Run the development server

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/.env-sample .env
docker run -d -v $PWD/mongodata:/data/db -p 27017:27017 mongo
python manage.py migrate
python manage.py run server
```

## Links
API Repository: [https://github.com/fnscoder/gallery-api](https://github.com/fnscoder/gallery-api)

API Live: [https://gallery-fns-api.herokuapp.com/docs/](https://gallery-fns-api.herokuapp.com/docs/)

Frontend Repository: [https://github.com/fnscoder/gallery-vuejs](https://github.com/fnscoder/gallery-vuejs)

Frontend Live: [https://gallery-fns-vuejs.herokuapp.com/](https://gallery-fns-vuejs.herokuapp.com/)

