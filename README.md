# INIT

Copy docker-compose.override.yml.dist to docker-compose.override.yml and adapt as desired.
Copy .env.dist and adapt as desired.

# USE

Start services:

```dcoker
docker-compose up -d
```

# ROUTES

```http
POST http://localhost:5000/example/route
```

Returns

```json
{
    "data": "POST DATA",
    "example": "ENV VAR FROM_ENV VALUE"
}
```

```http
GET http://development:5000/example/<data1>/test/<int:data2>><OPTINAL QUERY STRING>
```

Returns

```json
{
  "data1": "data1 PARAM VALUE", 
  "data2": "data2 PARAM VALUE", 
  "query_params": "QUERY PARAMS"
}
```