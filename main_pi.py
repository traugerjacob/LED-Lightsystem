import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import time
import requests.exceptions
import neopixel
import board
import sys
import threading

A = [0b01110, 0b10001, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001, 0b10001]
B = [0b11110, 0b10001, 0b10001, 0b11110, 0b11110, 0b10001, 0b10001, 0b11111]
C = [0b11111, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b11111]
D = [0b11110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b11110]
E = [0b11111, 0b10000, 0b10000, 0b11110, 0b11110, 0b10000, 0b10000, 0b11111]
F = [0b11111, 0b10000, 0b10000, 0b11110, 0b11110, 0b10000, 0b10000, 0b10000]
G = [0b01111, 0b10000, 0b10000, 0b10111, 0b10111, 0b10001, 0b10001, 0b01110]
H = [0b10001, 0b10001, 0b10001, 0b11111, 0b11111, 0b10001, 0b10001, 0b10001]
I = [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b11111]
J = [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b10100, 0b10100, 0b11100]
K = [0b10001, 0b10010, 0b10100, 0b11000, 0b11000, 0b10100, 0b10010, 0b10001]
L = [0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b11111]
M = [0b10001, 0b11011, 0b11011, 0b10101, 0b10001, 0b10001, 0b10001, 0b10001]
N = [0b10001, 0b11001, 0b11101, 0b10101, 0b10101, 0b10011, 0b10011, 0b10001]
O = [0b01110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110]
P = [0b11111, 0b10001, 0b10001, 0b11111, 0b10000, 0b10000, 0b10000, 0b10000]
Q = [0b01110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110, 0b00001]
R = [0b11110, 0b10001, 0b10001, 0b10001, 0b11110, 0b10010, 0b10001, 0b10001]
S = [0b01111, 0b10000, 0b10000, 0b01110, 0b01110, 0b00001, 0b00001, 0b11110]
T = [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100]
U = [0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110]
V = [0b10001, 0b10001, 0b10001, 0b10001, 0b01010, 0b01010, 0b01010, 0b00100]
W = [0b10001, 0b10001, 0b10101, 0b10101, 0b10101, 0b10101, 0b10101, 0b01110]
X = [0b10001, 0b10001, 0b01010, 0b00100, 0b00100, 0b01010, 0b10001, 0b10001]
Y = [0b10001, 0b10001, 0b01010, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100]
Z = [0b11111, 0b00001, 0b00010, 0b00100, 0b00100, 0b01000, 0b10000, 0b11111]
one = [0b11100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b11111]
two = [0b11111, 0b00001, 0b00001, 0b11111, 0b11111, 0b10000, 0b10000, 0b11111]
three = [0b11110, 0b00001, 0b00001, 0b00001, 0b01110, 0b00001, 0b00001, 0b11110]
four = [0b10001, 0b10001, 0b10001, 0b11111, 0b00001, 0b00001, 0b00001, 0b00001]
five = [0b11111, 0b10000, 0b10000, 0b11111, 0b11111, 0b00001, 0b00001, 0b11111]
six = [0b10000, 0b10000, 0b10000, 0b10000, 0b11111, 0b10001, 0b10001, 0b11111]
seven = [0b11111, 0b00001, 0b00001, 0b00001, 0b00010, 0b00010, 0b00100, 0b00100]
eight = [0b01110, 0b10001, 0b10001, 0b01110, 0b10001, 0b10001, 0b10001, 0b01110]
nine = [0b11111, 0b10001, 0b10001, 0b111111, 0b00001, 0b00001, 0b00001, 0b00001]
dash = [0b00000, 0b00000, 0b00000, 0b11111, 0b11111, 0b00000, 0b00000, 0b00000]
exclaim = [0b1, 0b1, 0b1, 0b1, 0b1, 0b0, 0b0, 0b1]
period = [0b0, 0b0, 0b0, 0b0, 0b0, 0b0, 0b0, 0b1]
apos = [0b1, 0b1, 0b1, 0b0, 0b0, 0b0, 0b0, 0b0]
amper = [0b01000, 0b10100, 0b10100, 0b01000, 0b10101, 0b10010, 0b10010, 0b01101]
space = [0b000, 0b000, 0b000, 0b000, 0b000, 0b000, 0b000, 0b000]
paran_o = [0b001, 0b010, 0b100, 0b100, 0b100, 0b100, 0b010, 0b001]
paran_c = [0b100, 0b010, 0b001, 0b001, 0b001, 0b001, 0b010, 0b100]

letter_dict = {"A": (A,5), "B" : (B,5), "C" : (C,5), "D" : (D,5), "E" : (E,5), "F" : (F,5), "G" : (G,5), "H" : (H,5), "I" : (I,5), "J" : (J,5), "K" : (K,5), "L" : (L,5), "M" : (M,5), "N" : (N,5), "O" : (O,5), "P" : (P,5), "Q" : (Q,5), "R" : (R,5), "S" : (S,5), "T" : (T,5), "U" : (U,5), "V" : (V,5), "W" : (W,5), "X" : (X,5), "Y" : (Y,5), "Z" : (Z,5), "0" : (O,5), "1" : (one,5), "2" : (two,5), "3" : (three,5), "4" : (four,5), "5" : (five,5), "6" : (six,5), "7" : (seven,5), "8" : (eight,5), "9" : (nine,5), "-" : (dash,5), "!": (exclaim, 1), "." : (period, 1), "'" : (apos,1), "&" : (amper,5), " " : (space,3), "(" : (paran_o,3), ")" : (paran_c,3)}


PIN = board.D18
NUM_LED = 512
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(PIN, NUM_LED, auto_write=False, pixel_order=ORDER)


def write_letter(let, pos, is_artist):
    written = 0
    if letter_dict.get(let) != None:
        letter, length = letter_dict[let]
        for i in range(8):
            mask = 2**(length-1)
            for j in range(length):
                add = i if (j + pos) %2 == 0 else 7-i
                value = int(8*(j + pos) + add)
                if mask & letter[i] > 0 and value >=0 and value < NUM_LED:
                    if not is_artist:
                        pixels[value] = (10,0,0)
                    else:
                        pixels[value] = (0,0,3)
                    written += 1
                mask = mask >> 1
    return written

def scroll_message(num_leds, height):
    max_pos = int(num_leds/height)
    cur_names = []
    with song_artist_lock:
        song = current_song
        artist = current_artist
        cur_names = [[song, max_pos]]
    while True:
        with kill_thread_lock:
            if kill_thread:
                break
        with song_artist_lock:
            if current_song != song or current_artist != artist:
                song = current_song
                artist = current_artist
                cur_pos = num_leds/height
                cur_names = [[song,max_pos]]
        time.sleep(.001)
        pixels.fill((0,0,0))
        total_written = 0
        next_names = []
        total_displacement = 0
        for i in range(len(cur_names)):
            name = cur_names[i][0]
            displacement_from_start_name = 0
            cur_name_pos = cur_names[i][1]
            total_displacement = cur_name_pos
            for let in name:
                if (let in letter_dict.keys()):
                    total_written += write_letter(let, total_displacement, name != current_song)
                    displacement_from_start_name += letter_dict[let][1] + 1
                    total_displacement = cur_name_pos + displacement_from_start_name
            if total_displacement > 0:
                next_names.append([name, cur_name_pos - 1])
            if i == len(cur_names) - 1 and total_displacement == max_pos - 6:
                if name == current_song:
                    next_names.append([artist, max_pos])
                else:
                    next_names.append([song, max_pos])
        cur_names = next_names
        pixels.show()
        time.sleep(.04)

#time.sleep(3)
scope = "playlist-read-private,streaming,user-read-playback-state"
#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

current_image = None

current_song = ""
current_artist = ""
song_artist_lock = threading.Lock()

kill_thread = False
kill_thread_lock = threading.Lock()
t1 = threading.Thread(target=scroll_message, args=(NUM_LED, 8))
t1.start()

while True:
    try:
        try:
            m = spotify.current_playback()
        except (spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError) as e:
            print("caught exception")
            time.sleep(3)
        if m == None:
            time.sleep(3)
            continue
        dic = m["item"]
        if current_song != dic['name'].upper() or current_artist != ', '.join([dic['artists'][i]['name'] for i in range(len(dic['artists']))]).upper():
            print(f"artist(s): {', '.join([dic['artists'][i]['name'] for i in range(len(dic['artists']))])}")
            print(f"song: {dic['name']}")
            print(f"album: {dic['album']['name']}")
            print(f"album: {dic['album']['images'][0]['url']}")
            with song_artist_lock:
                current_song = dic['name'].upper()
                current_artist = ', '.join([dic['artists'][i]['name'] for i in range(len(dic['artists']))]).upper()
        time.sleep(3)
    except KeyboardInterrupt:
        with kill_thread_lock:
            kill_thread = True
        t1.join()
        pixels.fill((0,0,0))
        pixels.show()
        sys.exit(0)
