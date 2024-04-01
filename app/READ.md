
## 0. [OPTIONAL] Pull mongo image from docker hub: 
```bash
$ docker pull mongo:latest
```
## 1. Start the mongo container: 
```bash
$ docker run --name <image_name> -d mongo:latest 
```
## 2. Verify container running status: 
```bash
$ docker ps
```
## 3. Retrieve container IPAdderess: 
```bash
$ docker inspect <container_id> | grep IPAddress
```
## 4. Connect to mongo client: 
```py
import pymongo as pm

client = pm.MongoClient("mongodb://<IPAddress>:27017/")
```
## 5. Connect to mongo from shell: 
```bash
$ docker exec -it mongo bash
$ ...
$ mongosh
```
## 6. Stop the container: 
```bash
$ docker stop <container_name>
```