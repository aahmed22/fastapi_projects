# Fast API CRUD Operations
This project outlines how to use **CRUD (CREATE, READ, UPDATE, DELETE)** operations for Fast API projects.  
The requests/endpoints constructed in this project are based on the 2023 NBA Finals teams/players. Enjoy!  

**Prerequisites**: You will need to setup your environment before you can begin using Fast API. Below are the requirments:
* Setup ***"venv"*** in your working directory. `python -m venv nameOfEnvironment` (Ex: **python -n venv fastapienv**)
* Install the requirements.txt via pip: `pip install -r requirements.txt`
* Run the command: `uvicorn main:app --reload` to start running the app.  
  The --reload parameter ensures you don't have to restart the application as your making updates. Just simply refresh. 

## Working with FastAPI Docs
After running the ***uvicorn*** command, launch your browser and enter this URL address: **localhost:8000/docs**  
From there you will be to view a live page of all API endpoints.  

FastAPI provides built-in support for Swagger UI integration, which allows you to automatically generate interactive documentation for your API based on your code. 

Below are the HTTP requests/endpoints we will be working with from this app:
* (GET) /players
* (GET) /players/{player_name}
* (GET) /players/
* (GET) /players/by_position/{selected_position}
* (POST) /players/add_player
* (PUT) /players/update_player
* (DELETE) /players/delete_player/{player_name}

![HTTP Requests Project1](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/http_requests_project1.PNG)


## Default Route
```python
@app.get("/")
async def welcome():
    return {'message': 'Welcome to the NBA 2023 Finals! Denver Nuggets vs Miami Heat!'}
```
When accessing the app via "localhost:8000", you will encounter the welcome message below:


![Preview Default Route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/preview_default_route.PNG)


The cool thing about the Swagger UI is that you can access the same thing on the docs page.  
Proceed with expanding on the first (GET) route "/" and then click the "Try it out" button, followed by "Execute" and you will see the same output in the Response body:

![Output Default Route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/default_route_doc_project1.PNG)

## (GET) /players
This endpoint will showcase the two superstar players on each of the respective teams in the 2023 NBA Finals.

Below is the list constructed:
```python
nba_finals_players = [
    {'name': 'Jamal Murray', 'team':'Denver Nuggets', 'position':'guard'},
    {'name': 'Nikola Jokic', 'team': 'Denver Nuggets', 'position': 'center'},
    {'name': 'Jimmy Butler', 'team': 'Miami Heat', 'position': 'forward'},
    {'name': 'Bam Adebayo', 'team': 'Miami Heat', 'position': 'center'}
]
```

Here is the endpoint for **/players**:
```python
@app.get("/players")
async def get_all_players():
    return nba_finals_players
```
When interacting with the Swagger UI for this endpoint do the following:

* Click on "Try it out":
![Try it Out players route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/try_it_out_project1.PNG)

* Following that clikc on "Execute":
![Execute players route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/execute_project1.PNG)

Following that you should see this output:
![Output for players route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_get_players_project1.PNG)


## (GET) /players/{player_name}
This endpoint **"/players/{player_name}"** indicates that we're using path parameters. This allows for Dynamic routing, where different values can be passed in the URL to represent different resources or entities. This enables the creation of flexible and customizable routes in our API. For instance, a path parameter can represent a specific user ID or a product code, allowing you to retrieve or manipulate specific resources based on the provided parameter.  

In our case, we want to get info on a single player. Thus we need to take in a value in order to accomplish this:
```python
@app.get("/players/{player_name}")
async def get_player_info(player_name: str):
    for player in nba_finals_players:
        if player.get('name').casefold() == player_name.casefold():
            return player
```

Within the Swagger UI, you can enter the value like so:
![Input player name route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_path_parameter_player_name_project1.PNG)

Following that you should see this output:
![Output player name route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_path_parameter_player_name_project1.PNG)


## (GET) /players/
This endpoint **"/players/"** is a bit different compared to the previous endpoints used. In this endpoint we will be using query parameters. Query parameters allow for flexible API requests by providing optional parameters that can be included or excluded based on the client's needs.  

In our project case we want to get all the superstar players associated from a single team. 
```python
@app.get("/players/")
async def get_players_by_team_query(team: str):
    players_by_team_return = []
    for player in nba_finals_players:
        if player.get('team').casefold() == team.casefold():
            players_by_team_return.append(player)
    return players_by_team_return
```

Here's what you would enter when query via URL: `http://localhost:8000/players/?team=Miami%20Heat`

Let's try it out via Swagger UI, we'll enter "Miami Heat" as our input:
![Input team players route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_query_parameter_players_project1.PNG)

We should then see this output:
![Output team players route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_query_parameter_players_project1.PNG)

## (GET) /players/by_position/{selected_position}
For our endpoint **"/players/by_position/{selected_position}"** we will be using path parameters again and this time we would like to get all the players available based on the position they play on the court.

Below is the endpoint defined:
```python
@app.get("/players/by_position/{selected_position}")
async def get_players_by_position(selected_position: str):
    selected_position_return = []
    for player in nba_finals_players:
        if player.get('position').casefold() == selected_position.casefold():
            selected_position_return.append(player)
    return selected_position_return
```

Our input choice will be "center":
![Input position route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_selected_position_project1.PNG)

Here is the output:
![Output position route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_selected_position_project1.PNG)



## (POST) /players/add_player
For our endpoint **"/players/add_player"** we will be using the **"POST"** method to create/add a player to the list.

Below is the endpoint defined:
```python
@app.post("/players/add_player")
async def add_player(new_player=Body()):
    nba_finals_players.append(new_player)
```
Notice that we are using the Body() method. This method is typically used as a parameter in the function signature of a FastAPI endpoint. It is used to describe the structure and data type of the request body that the API endpoint expects. 

Here is the request body we will be using, adding an additional player to the list for the Denver Nuggets team:
```json
{
    "name": "Aaron Gordon",
    "team": "Denver Nuggets",
    "position": "forward"
}
```
Here's the input via Swagger UI:
![Input Add player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_add_player_project1.PNG)

Now, lets view the output by executing the **/players** endpoint and view the new addition made:
![Output Add player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_add_player_project1.PNG)


## (PUT) /players/update_player
For our endpoint **"/players/update_player"** we will be using the **"PUT"** method to update a player in our list.

Below is the update endpoint defined:
```python
@app.put("/players/update_player")
async def update_player(updated_player=Body()):
    for index in range(len(nba_finals_players)):
        if nba_finals_players[index].get('name').casefold() == updated_player.get('name').casefold():
            nba_finals_players[index] = updated_player
```

We will be using this response body to update Bam Adebayo position from ***center to forward***:
```json
{
    "name": "Bam Adebayo",
    "team": "Miami Heat",
    "position": "forward"
}
```
Here's the input via Swagger UI:
![Input update player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_update_player_project1.PNG)

Now, lets view the output by executing the **/players** endpoint and view the update on Bam Adebayo record:
![Output update player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_update_player_project1.PNG)


## (DELETE) /players/delete_player/{player_name}
Finally to conclude our CRUD operations project we will be using the **Delete** method for our endpoint **"/players/delete_player/{player_name}"**

Below is the delete endpoint defined:
```python
@app.delete("/players/delete_player/{player_name}")
async def delete_player(player_name: str):
    for index in range(len(nba_finals_players)):
        if nba_finals_players[index].get('name').casefold() == player_name.casefold():
            nba_finals_players.pop(index)
            break
```

For our input parameter, we will just enter the player's name via Swagger UI:
![Input delete player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/input_delete_player_project1.PNG)

Now, lets view the output by executing the **/players** endpoint and we should see "Aaron Gordon" removed from our list:
![Output update player route](https://github.com/aahmed22/fastapi_projects/blob/main/snapshots/project1/output_delete_player_project1.PNG)


## Project 2
Testing...

[Click Here for Project 2 Details](project2/project2_readme.md)