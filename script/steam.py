import requests
import os
import time
import pandas as pd
import datetime


API_KEY = os.environ["API_KEY"]
STEAM_ID = '76561198447352948'
GAME_LIBRARY_URL = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'

# The parameters for the API request
params = {
    'key': API_KEY,
    'steamid': STEAM_ID,
    'include_played_free_games': 1,
    'format': 'json'
}
response = requests.get(GAME_LIBRARY_URL, params=params)
data = response.json()
game_id = []
game_time = []
game_finnaly_play = []
for game in data['response']['games']:
    game_id.append(game['appid'])
    game_time.append(game["playtime_forever"])
    game_finnaly_play.append(game["rtime_last_played"])

game_name = []
figure_path = []
for i in game_id:
    APP_ID = i
    APP_DETAILS_URL = f'https://store.steampowered.com/api/appdetails?appids={APP_ID}'
    response = requests.get(APP_DETAILS_URL)
    time.sleep(0.5)
    data = response.json()
    name = data[str(APP_ID)]['data']['name']
    game_name.append(name)
    header_image_url = data[str(APP_ID)]['data']['header_image']
    response = requests.get(header_image_url)
    with open(f'docs/doc_images/steam/{APP_ID}.jpg', 'wb') as f:
        f.write(response.content)
    figure_path.append("![](../doc_images/steam/{}.jpg)".format(APP_ID))

df = pd.DataFrame(
    {"Game figure":figure_path,
      "Game name":game_name,
     "Game time":game_time,
     "Last Played Time":game_finnaly_play,
     }
)

def time_change(rtime_last_played):
  dt = datetime.datetime.fromtimestamp(rtime_last_played)
  date_str = dt.strftime('%Y-%m-%d %H:%M:%S')
  return date_str
df["Last Played Time"] = df["Last Played Time"].map(time_change)
df = df[df["Game time"] > 10].reset_index(drop=True)
df = df.sort_values("Game time",ascending=False).reset_index(drop=True)
md_table = df.to_markdown()


with open('docs/hobby/steam.md', 'w') as f:
    f.write("# Steam Game time\n")
    f.write("Note: 下表是自动抓取的steam的游戏时间，过滤删除了只打开一会会的游戏（小于10min）\n")
    f.write("\n")
    f.write(md_table)
