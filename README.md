# Wedding photo galery

You got a request from a friend to create a gallery for his wedding where his friends will be able to upload their photos and he will have a unified gallery with all friend's photos.
He wants to be able to approve the photos before being visible to everyone. He and his wife should be the only ones able to approve new photos.
Users must be able to like photos and add comments to photos.

## Stack used
* Python
* Django
* Django Rest Framewrok
* Mongodb


## How to run the project

1. Create a virtualenv python 3.8
2. Activate your virtualenv
3. Install dependencies
4. Configure the instance with .env file

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/.env-sample .env
```
