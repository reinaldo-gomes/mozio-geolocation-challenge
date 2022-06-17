# Mozio Geolocation Challenge

A link to a running instance has been provided at AWS:<br/>
<http://ec2-18-119-104-82.us-east-2.compute.amazonaws.com:8000>

GeoJson is expected to be in the following format:
```
{
    "provider": "provider01",
    "name": "area01",
    "price": 1000.0,
    "geolocation": {
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [10, 20],
                [12, 20],
                [12, 22],
                [10, 22]
            ]
        }
    }
}
```

## Endpoints available

- List and add providers:<br/>
<http://ec2-18-119-104-82.us-east-2.compute.amazonaws.com:8000/providers>
- List and add service areas:<br/>
<http://ec2-18-119-104-82.us-east-2.compute.amazonaws.com:8000/serviceareas>
- List areas overlapping any given geographic point described in Latitude and Longitude:<br/>
e.g. overlappingareas?lat=10.5&lng=21.3<br/>
<http://ec2-18-119-104-82.us-east-2.compute.amazonaws.com:8000/overlappingareas>
- OpenAPI-generated docs:<br/>
<http://ec2-18-119-104-82.us-east-2.compute.amazonaws.com:8000/docs>