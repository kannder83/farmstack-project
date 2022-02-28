## For Development

In the file .env you need to change value of

```sh
PRODUCTION_ENVIRONMENT=False
```

For run backend in depelopment:

```sh
docker-compose -f Developer.yml build
docker-compose -f Developer.yml up
```

To remove:

```sh
docker-compose -f Developer.yml down --remove-orphans -v
```
