## Search app

### installation

**Required**

- docker
- docker-compose

1. Clone backend repository

`git clone git@github.com:qbasista/<repo_name>.git`

2. On the root directory create `.env` with your ENV for database base on `.env.dist` file.

3. Open project directory
   `cd <django_project>/<django_app>`

4. Create `.env` file for django app base on `.env.dist`

`<django_project>/<django_app>/.env.dist`

Important! Paste the same database ENVs for Django project in `.env` as for database.

`DATABASE_URL=psql://<USER>:<PASSWORD>@db:5432/<DATABASE>`

5. Clone frontend repository to main directory `./<FRONT_APP>`

`git clone git@github.com:qbasista/<vue_app>.git`

6. Create `.env` file for frontend from `.env.dist` where is set url for backend.

7. Back to main project directory (`./<DJANGO_APP>`) and run docker-compose.

`docker-compose up --build -d`

8. Migrate database

   1. Check name of django container
      `docker ps`

      should be:
      `<project_name>_api_1`

   2. Open django container
      `docker exec -it <container name> bash`

      example:
      `docker exec -it <project_name>_api_1 bash`

   3. In the container run migration.
      `python manage.py migrate`

   4. Leave django container.
      `ctrl + d`

9. Paste app url in browser. Enjoy!
   `http://localhost:9090`
