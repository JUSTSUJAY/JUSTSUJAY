# # NjY2MDFjYzVjYTJkZjUwMTkyYTM4ZmVmLjZidDU3MElyS1o2NkJxMnRIbVY2c3p6RDhSdVlHMWR0

# import requests
# import json
# import requests


# """ URLS """
# stats_url = 'https://api.monkeytype.com/users/stats'
# personal_best_url = 'https://api.monkeytype.com/users/personalBests'
# rank_url = 'https://api.monkeytype.com/leaderboards/rank'

# """ HEADERS """
# headers = {
#     'Authorization': 'ApeKey NjY2MDFjYzVjYTJkZjUwMTkyYTM4ZmVmLjZidDU3MElyS1o2NkJxMnRIbVY2c3p6RDhSdVlHMWR0'  # replace with your actual ApeKey
# }

# """ FETCH DATA """
# # Stats
# stats = requests.get(stats_url, headers=headers).json()['data']
# Tests_Started = stats['startedTests']
# Tests_Completed = stats['completedTests']
# Time_Typing = stats['timeTyping']

# print("Tests Started: ", Tests_Started)
# print("Tests Completed: ", Tests_Completed)
# print("Time Typing: ", Time_Typing)

# # Personal Bests
# params = {"mode":"time"}
# personal_best = requests.get(url=personal_best_url,params= params,headers = headers).json()['data']


# acc_15 = personal_best['15'][0]['acc']
# wpm_15 = personal_best['15'][0]['wpm']
# acc_30 = personal_best['30'][0]['acc']
# wpm_30 = personal_best['30'][0]['wpm']
# acc_60 = personal_best['60'][0]['acc']
# wpm_60 = personal_best['60'][0]['wpm']

# print("15 Second Accuracy: ", acc_15)
# print("30 Second Accuracy: ",acc_30)
# print("60 Second Accuracy: ",acc_60)
# print("15 Second WPM: ",wpm_15)
# print("30 Second WPM: ",wpm_30)
# print("60 Second WPM: ",wpm_60)

# # rank

# params_15 = {"language":"english","mode":"time","mode2":"15"}
# params_30 = {"language":"english","mode":"time","mode2":"30"}
# params_60 = {"language":"english","mode":"time","mode2":"60"}
# rank_15 = requests.get(url=rank_url,params= params_15,headers = headers).json()['data']
# rank_30 = requests.get(url=rank_url,params= params_30,headers = headers).json()['data']
# rank_60 = requests.get(url=rank_url,params= params_60,headers = headers).json()['data']
# print(rank_15['rank'])
# print(rank_30['rank'])
# print(rank_60['rank'])

import requests
from PIL import Image, ImageDraw, ImageFont
import os

# Constants
APE_KEY = 'NjY2MDFjYzVjYTJkZjUwMTkyYTM4ZmVmLjZidDU3MElyS1o2NkJxMnRIbVY2c3p6RDhSdVlHMWR0'  # replace with your actual ApeKey
STATS_URL = 'https://api.monkeytype.com/users/stats'
PERSONAL_BEST_URL = 'https://api.monkeytype.com/users/personalBests'
RANK_URL = 'https://api.monkeytype.com/leaderboards/rank'
HEADERS = {'Authorization': f'ApeKey {APE_KEY}'}

# Fetch Data
def fetch_data():
    stats = requests.get(STATS_URL, headers=HEADERS).json()['data']
    personal_best = requests.get(PERSONAL_BEST_URL, headers=HEADERS, params={"mode": "time"}).json()['data']
    rank_15 = requests.get(RANK_URL, headers=HEADERS, params={"language": "english", "mode": "time", "mode2": "15"}).json()['data']
    rank_30 = requests.get(RANK_URL, headers=HEADERS, params={"language": "english", "mode": "time", "mode2": "30"}).json()['data']
    rank_60 = requests.get(RANK_URL, headers=HEADERS, params={"language": "english", "mode": "time", "mode2": "60"}).json()['data']
    
    return stats, personal_best, rank_15, rank_30, rank_60

# Generate Card
def generate_card(stats, personal_best, rank_15, rank_30, rank_60):
    # Constants
    WIDTH, HEIGHT = 500, 300
    BACKGROUND_COLOR = (0,0,0)
    TEXT_COLOR = (100, 150, 255)
    STREAK_COLOR = (255, 140, 0)
    XP_COLOR = (255, 255, 0)
    BADGE_COLORS = [(255, 0, 0), (0, 0, 255), (255, 165, 0)]
    FONT_PATH = "Hegemonic.ttf"
    FONT_SIZE_LARGE = 40
    FONT_SIZE_SMALL = 20

    # Create image
    card = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(card)

#   Load fonts
    font_large = ImageFont.truetype(FONT_PATH, FONT_SIZE_LARGE)
    font_small = ImageFont.truetype(FONT_PATH, FONT_SIZE_SMALL)

    # Add text to the image
    draw.text((10, 10), f"Tests Started: {stats['startedTests']}", font=font_small, fill=(255,255,255))
    draw.text((10, 30), f"Tests Completed: {stats['completedTests']}", font=font_small, fill=(255,255,255))
    draw.text((10, 50), f"Time Typing: {stats['timeTyping']}", font=font_small, fill=(255,255,255))
    draw.text((10, 90), f"15s Best: {personal_best['15'][0]['wpm']} WPM, {personal_best['15'][0]['acc']}% ACC", font=font_small, fill=(255,255,255))
    draw.text((10, 110), f"30s Best: {personal_best['30'][0]['wpm']} WPM, {personal_best['30'][0]['acc']}% ACC", font=font_small, fill=(255,255,255))
    draw.text((10, 110), f"30s Best: {personal_best['30'][0]['wpm']} WPM, {personal_best['30'][0]['acc']}% ACC", font=font_small, fill=(255,255,255))

    draw.text((10, 170), f"15s Rank: {rank_15['rank']}", font=font_small, fill=(255,255,255))
    draw.text((10, 190), f"30s Rank: {rank_30['rank']}", font=font_small, fill=(255,255,255))
    draw.text((10, 210), f"60s Rank: {rank_60['rank']}", font=font_small, fill=(255,255,255))

    # Save the image
    card_path = 'monkeytype_card.png'
    card.save(card_path)
    return card_path

def main():
    stats, personal_best, rank_15, rank_30, rank_60 = fetch_data()
    card_path = generate_card(stats, personal_best, rank_15, rank_30, rank_60)
    print(f"Card saved at {card_path}")

if __name__ == "__main__":
    main()

