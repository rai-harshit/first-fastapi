from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    #return 'Hello World! This is my first server using FastAPI!'
    return {
        'home':{
            'name':'Harshit Rai'
        }
    }

@app.get('/about')
def about():
    return {
        'about':{
            'name': 'Harshit Rai'
        }
    }