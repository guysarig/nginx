# nginx-based get date-time Microservice

## Installation

Build the microservice's image
```
docker build -t [repo_name]/nginx_date_time:[version]
```

Push the microservice to the image regisry
```
docker push [repo_name]/nginx_date_time:[version]
```

Install `datetime` helm chart 1st:
```
helm install datetime datetime_chart
```
(delete it using `helm delete` command)


## Testing

Forward the service port from k8s to the local machine
```
kubectl port-forward service/datetime 80:80
```

Run the test script using python3:
```
python3 test.py
```
