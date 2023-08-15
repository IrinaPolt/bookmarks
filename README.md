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
### Endpoints

...