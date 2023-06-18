# Fast API CRUD Operations
This project outlines how to use **CRUD (CREATE, READ, UPDATE, DELETE)** operations for Fast API projects.  
The routes/endpoints constructed in this project are based on the 2023 NBA Finals teams/players. Enjoy!  

**Prerequisites**: You will need to setup your environment before you can begin using Fast API. Below are the requirments:
* Setup ***"venv"*** in your working directory. `python -m venv nameOfEnvironment` (Ex: **python -n venv fastapienv**)
* Install the requirements.txt via pip: `pip install -r requirements.txt`
* Run the command: `uvicorn main:app --reload` to start running the app.  
  The --reload parameter ensures you don't have to restart the application as your making updates. Just simply refresh. 

## Working with FastAPI Docs
After running the ***uvicorn*** command, launch your browser and enter this URL address: **localhost:8000/docs**  
From there you will be to view a live page of all API routes/endpoints.  

FastAPI provides built-in support for Swagger UI integration, which allows you to automatically generate interactive documentation for your API based on your code. 

Below are the routes we will be working with from this app:
* (GET) /players
* (GET) /players/{player_name}
* (GET) /players/
* (GET) /players/by_position/{selected_position}
* (POST) /players/add_player
* (PUT) /players/update_player
* (DELETE) /players/delete_player/{player_name}

![HTTP Requests Project1](snapshots/projects1/preview_default_route.PNG)


