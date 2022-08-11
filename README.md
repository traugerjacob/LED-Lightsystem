# LED-Lightsystem
And if I'm sued into submission I can still come home to this


This uses Python and Arduino to have song/artist name scroll along WS2812B LED strips. Currently set to do 8x51 since that takes up all the memory in my Arduino Uno.

The non standard libraries used for Python are Spotipy and pyserial. For Arduino it is FastLED.

To use this you will need to sign up for Spotify Developer and create an app. Add the client id/secret id/redirect uri as environment variables (SPOTIPY_CLIENT_id, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL) unless you want to hard code them into your code.
