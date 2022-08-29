# LED-Lightsystem
And if I'm sued into submission I can still come home to this


This project uses Python to this uses Python to connect to Spotify, query the current song you are playing, and have song/artist name scroll along WS2812B LED strips. There are 2 options on how to use this. Rather with a computer and an Arduino or a microprocessor (I use Raspberry Pi 4 Model B). 

For Aruino version, this uses Python and Arduino to have song/artist name scroll along WS2812B LED strips. Currently set to do 8x51 since that takes up all the memory in my Arduino Uno. It will also open the album cover on the computer through Mozilla Firefox for display.

The non standard libraries used for Python are Spotipy, pyserial, and selenium. For Arduino it is FastLED.

For the microprocessor, it does the above, but without the album cover display. It also needs Spotipy, but only other non standard library it needs is the Adafruit circuitpython neopixel library.

They both work, but the Arduino version is not as fleshed out and I probably wont be going back to do that.

To use this you will need to sign up for Spotify Developer and create an app. To have spotipy work, you will need to add the client id/secret id/redirect uri as environment variables (SPOTIPY_CLIENT_id, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL), unless you want to hard code them into your code.
