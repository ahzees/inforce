# Inforce test task



## How to run test task



#### Firstly, you have to clone the git hub repo
<br></br>
```{r test-python, engine='python'}
git clone git@github.com:ahzees/inforce.git
```
### Open project directory and run docker-compose. You need to have an .env file in django-project folder
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
