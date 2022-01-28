# Backend for Donna chrome extension
This is the backend for the [Donna extension](https://github.com/notanumber11/donna-extension).

The backend architecture is as follows:

The client communicates with API gateway that validates the request. API Gateway passes the request to the Lambda. The Lambda calls the OpenAI APIs and store the logs in cloudwatch.
![AWS architecture](readme_assets/diagram.png?raw=true "Title")


## Development

### Python utils
- Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ cd venv/scripts
   $ activate
   ```

- Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```
 
### Run lambda
```bash
    docker build -t donna-backend .   
```

```bash
    docker run -p 9000:8080 donna-backend   
```

````bash
curl --location --request POST 'http://localhost:9000/2015-03-31/functions/function/invocations' --header 'Content-Type: text/plain'  --data-raw '{"customer_prompt": "I would like to have a meeting tomorrow. I can talk about our books and movies. We have several discounts. I am available from 9 to 10 pm. Thanks"}'

````

#### Kill docker vmmem process
[Reference](https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process)
```
wsl --shutdown
```

### Run flask
```bash
    flask --app flask_server run
```
You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

### Run local_test
```bash
    python local_test
```


### Deploy docker
```
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [AWS_ID].dkr.ecr.us-east-1.amazonaws.com
```

```
    docker build -t donna .
```
```
    docker tag donna:latest [AWS_ID].dkr.ecr.us-east-1.amazonaws.com/donna:4
```

```
    docker push [AWS_ID].dkr.ecr.us-east-1.amazonaws.com/donna:4
```