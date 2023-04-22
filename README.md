# Inforce test task



## How to run test task



#### Firstly, you have to clone the git hub repo
<br></br>
```{r test-python, engine='python'}
git clone git@github.com:ahzees/inforce.git
```
### Open project directory and run docker-compose. You need to have an .env file in the root folder
<br></br>
```{r test-python, engine='python'}
docker-compose build
```
### And
<br></br>
```{r test-python, engine='python'}
docker-compose up
```
### Now, server is ready so you can open the api documentation
<br></br>
```{r test-python, engine='python'}
http://127.0.0.1:8000/api/schema/swagger-ui/
```

### If u want to start the project on yout local computer, then you have to install poetry and dependecies for poetry
<br></br>
```{r test-python, engine='python'}
pip install poetry
poetry install
```
### Then, you have to use
<br></br>
```{r test-python, engine='python'}
poetry shell
```
### Also, u have to remember that if you don`t use docker, you have to uncomments Database setup in inforce/settings.py
<br></br>
```{r test-python, engine='python'}
cd inforce
./manage.py runserver
```
