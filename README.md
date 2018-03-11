# SMCEBI-Map

This project is about creating virtual, 2-dimensional map of SMCEBI

## Getting Started

Download git repository

```
git clone https://github.com/bartlomiejkrzys/smcebi.git
```

Enter to project folder

```
cd smcebi
```

Build && run application

```
docker-compose up --build
```


### Prerequisites

What things you need to install beforehand and how to install them

## For Ubuntu

```
sudo apt-get install docker
sudo apt-get install docker-compose
sudo apt-get install git
```

## For Windows

Docker https://docs.docker.com/docker-for-windows/install/

Git https://git-scm.com/download/win


### Environment variables

Environment variables are stored in **.env** file and should be approach with caution.

By default, SMCEBI-Map is running on port 8000. To change it to port 80, type:

```
export DJANGO_PORT=80
```

## Built With

* [Leaflet](http://leafletjs.com/) - Framework used to display the map
* [GeoDjango](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/) - Framework used to create web application with spatial data

## Authors

* **Bartlomiej Krzys** - *Initial work* - [BartlomiejKrzys](https://github.com/bartlomiejkrzys)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

