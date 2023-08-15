# bookmarks
Dockerized service for storing user's website bookmarks

### Description

The service is designed to store users' bookmarks for various websites. After registration, the user can save links, create collections of their bookmarks, edit, and delete them. To populate the information about the resource to store it in the database, either HTML markup or Open Graph markup is used.

### .env pattern for database usage

```
SECRET_KEY=
POSTGRES_DATABASE=<the title of the database>
POSTGRES_USER=<login>
POSTGRES_PASSWORD=<password>
DB_HOST=db <the title of the database service from docker-compose>
DB_PORT=5432 <port>
```
### Launch

**.env file needs to be stored in the /infra/ directory**

```
git clone git@github.com:IrinaPolt/bookmarks.git
cd bookmarks/infra/
docker-compose up --build
```

Migrations are performed automatically, while creating a superuser needs to be done manually.

```
docker exec -it <the container ID> python manage.py createsuperuser

```
To find out the container ID:

```
docker ps
```

### Endpoints

- **URL:** `/api/` - drf root. The detailed API schema will be accessible via the Swagger endpoint.
- **URL:** `/swagger/`
- **URL:** `/admin/` - django admin endpoint

### Postman testing

![Example](https://github.com/IrinaPolt/bookmarks/blob/main/infra/image.png)
