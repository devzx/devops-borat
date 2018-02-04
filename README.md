# devops-borat
A fun little python app that posts a random DevOps Borat tweet to a given Hipchat channel

## Dependencies
```docker```
## Usage
``` sh
$ git clone git@github.com:devzx/devops-borat.git
$ cd devops-borat
```
Edit the Dockerfile and add a valid Hipchat Integration URL as the value to the ENV BORAT variable.

The application by default will post to the channel twice a day, at 8AM and 3PM. You can customise this to your liking by editing the cronjob which also resides within the Dockerfile.
```
$ docker build -t borat .
$ docker run -d --name borat borat
```
