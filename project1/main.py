from fastapi import Body, FastAPI

app = FastAPI()

nba_finals_players = [
    {'name': 'Jamal Murray', 'team':'Denver Nuggets', 'position':'guard'},
    {'name': 'Nikola Jokic', 'team': 'Denver Nuggets', 'position': 'center'},
    {'name': 'Jimmy Butler', 'team': 'Miami Heat', 'position': 'forward'},
    {'name': 'Bam Adebayo', 'team': 'Miami Heat', 'position': 'center'}
]

@app.get("/")
async def welcome():
    return {'message': 'Welcome to the NBA 2023 Finals! Denver Nuggets vs Miami Heat!'}

@app.get("/players")
async def get_all_players():
    return nba_finals_players

@app.get("/players/{player_name}")
async def get_player_info(player_name: str):
    for player in nba_finals_players:
        if player.get('name').casefold() == player_name.casefold():
            return player
        
@app.get("/players/")
async def get_players_by_team_query(team: str):
    players_by_team_return = []
    for player in nba_finals_players:
        if player.get('team').casefold() == team.casefold():
            players_by_team_return.append(player)
    return players_by_team_return

@app.get("/players/by_position/{selected_position}")
async def get_players_by_position(selected_position: str):
    selected_position_return = []
    for player in nba_finals_players:
        if player.get('position').casefold() == selected_position.casefold():
            selected_position_return.append(player)
    return selected_position_return

@app.post("/players/add_player")
async def add_player(new_player=Body()):
    nba_finals_players.append(new_player)

@app.put("/players/update_player")
async def update_player(updated_player=Body()):
    for index in range(len(nba_finals_players)):
        if nba_finals_players[index].get('name').casefold() == updated_player.get('name').casefold():
            nba_finals_players[index] = updated_player

@app.delete("/players/delete_player/{player_name}")
async def delete_player(player_name: str):
    for index in range(len(nba_finals_players)):
        if nba_finals_players[index].get('name').casefold() == player_name.casefold():
            nba_finals_players.pop(index)
            break
