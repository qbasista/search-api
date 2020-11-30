## Search app

### installation

**Required**

- docker
- docker-compose

1. Clone backend repository

`git clone git@github.com:qbasista/search-api.git`

2. On the root directory create `.env` with your ENV for database base on `.env.dist` file.

```
POSTFRES_USER=<db_user>
POSTGRES_PASSWORD=<db_password>
POSTGRES_DB=<db_name>
```

3. Open project directory
   `cd search_api/search_api`

4. Create `.env` file for django app base on `.env.dist`

`search_api/search_api/.env.dist`

.env
```
DEBUG=on
SECRET_KEY=your-secret-key #django secret key
DATABASE_URL=psql://<USER>:<PASSWORD>@db:5432/<DATABASE> #database connector
SQLITE_URL=sqlite:///my-local-sqlite.db #copy
GOOGLE_API_KEY=your-google-secret-key #google developer key
GOOGLE_CSE_ID=your-google-cse-id #google custom search enging - https://programmablesearchengine.google.com/
QUERY_TIME_DELTA_SECONDS=1000 #delta time between new requests in seconds
```

Important! Paste the same database ENVs for Django project in `.env` as for database.

`DATABASE_URL=psql://<USER>:<PASSWORD>@db:5432/<DATABASE>`

5. Clone frontend repository to main directory `./search-frontend`

`git clone git@github.com:qbasista/search-frontend.git`

search-api/

```
- README.md
- docker-compose.yml
- search_api
- search-frontend
```

6. Create `.env` file for frontend from `.env.dist` where is set url for backend.

7. Back to main project directory (`./search-api`) and run docker-compose.

`docker-compose up --build -d`

8. Migrate database

   1. Check name of django container
      `docker ps`

      should be:
      `search-api_api_1`

   2. Open django container
      `docker exec -it <container name> bash`

      example:
      `docker exec -it search-api_api_1 bash`

   3. In the container run migration.
      `python manage.py migrate`

   4. Leave django container.
      `ctrl + d`

9. Paste app url in browser. Enjoy!
   `http://localhost:9090`
