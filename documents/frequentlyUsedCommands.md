## Frequently Used Commands

<br><br>

* Clear compose container and restart

    ```shell
    docker-compose down && docker-compose build --no-cache && docker-compose up
    ``` 

* Test and Lint

  ```shell
  docker-compose run --rm app sh -c "python manage.py test && flake8"
  ```

* wait_fo_db and test and Lint

  ```shell
  docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"
  ```


* Make migrations, Migrate

```shell
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

```shell
docker-compose run --rm app sh -c "python manage.py migrate"
```

* Wait for DB

```shell
docker-compose run --rm app sh -c "python manage.py wait_for_db"
```