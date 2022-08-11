import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests.exceptions
import serial
import time

def send_message(message, arduino):
    arduino.flushOutput()
    message = message[0: 49] #only holds 150 characters rn due to memory limitations
    #start is the column you want to start on
    for i in message:
        arduino.write(bytes(i,"utf-8"))
        time.sleep(.01)
    arduino.write(bytes("\n","utf-8"))
    while (arduino.out_waiting != 0):
        continue



arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
arduino.flushOutput()
arduino.flushInput()
time.sleep(3)
scope = "playlist-read-private,streaming,user-read-playback-state"
#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
driver = webdriver.Firefox()

driver.fullscreen_window()
current_image = None
current_song = ""
while True:
    flag = False
    while not flag:
        try:
            m = spotify.current_playback()
            flag = True
        except (spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError) as e:
            print("caught exception")
            time.sleep(3)
    if m == None:
        time.sleep(3)
        continue
    dic = m["item"]
    if current_song != dic['name']:
        print(f"artist(s): {', '.join([dic['artists'][i]['name'] for i in range(len(dic['artists']))])}")
        print(f"song: {dic['name']}")
        print(f"album: {dic['album']['name']}")
        print(f"album: {dic['album']['images'][0]['url']}")
        send_message(dic['name'], arduino)
        send_message(', '.join([dic['artists'][i]['name'] for i in range(len(dic['artists']))]), arduino)
        print(arduino.readline())
        time.sleep(.1)
        print(arduino.readline())
        current_song = dic['name']
    if current_image != dic['album']['images'][0]['url']:
        driver.get(dic['album']['images'][0]['url'])
        current_image = dic['album']['images'][0]['url']
        driver.set_context("chrome")
        # Create a var of the window
        win = driver.find_element_by_tag_name("html")
        # Send the key combination to the window itself rather than the web content to zoom out
        # (change the "-" to "+" if you want to zoom in)
        for c in range(4):
            win.send_keys(Keys.CONTROL + "+")
        # Set the focus back to content to re-engage with page elements
        driver.set_context("content")
    time.sleep(3)

