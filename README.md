# RANDOM JOKE SERVICE
Python Module to get Random Jokes

## INSTALLATION

```bash
pip3 install -r requirements.txt
docker build -t joke_image .
docker run --name joke_container -p 5000:5000 joke_image
```

## LOGS
Avoided logging to file . Just kept it simple currently printing on Screen  

##TEST . 

#Unitest:

export NAME_URI='https://api.namefake.com/'
export JOKE_URI='http://api.icndb.com/jokes/random?firstName={first_name}&lastName={last_name}&limitTo=[nerdy];'
cd tests/ &&  python -m unittest  


##Enjoy Random jokes on. 


http://0.0.0.0:5000/
