*docker-compose.yml*

version: '3'
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: 'date'
      POSTGRES_PASSWORD: '123456789'
      POSTGRES_DB: 'basedatos'
    ports:
      - "4500:5432"


*README.md*
