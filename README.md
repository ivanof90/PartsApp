# PartsApp

Run postgresql in docker:
docker run --name postgres-container -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -v /path/to/local/data:/var/lib/postgresql/data -p 5432:5432 -d postgres

Run docs/DDL.sql in your database

Run in dev
uvicorn app:app --reload --port 5000

swagger docs: http://127.0.0.1:5000/docs

Postman collection in docs