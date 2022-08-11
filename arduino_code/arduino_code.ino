#include <FastLED.h>
#define LONGEST_NAME 50
#define NUM_LED 408
CRGB leds[NUM_LED];
char s[LONGEST_NAME];
char artist[LONGEST_NAME];
int s_len = 0;
int artist_len = 0;
boolean end_message = false;
int cur_pos = 0;
const byte A[8] = {B01110, B10001, B10001, B10001, B11111, B10001, B10001, B10001};
const byte B[8] = {B11110, B10001, B10001, B11110, B11110, B10001, B10001, B11111};
const byte C[8] = {B11111, B10000, B10000, B10000, B10000, B10000, B10000, B11111};
const byte D[8] = {B11110, B10001, B10001, B10001, B10001, B10001, B10001, B11110};
const byte E[8] = {B11111, B10000, B10000, B11110, B11110, B10000, B10000, B11111};
const byte F[8] = {B11111, B10000, B10000, B11110, B11110, B10000, B10000, B10000};
const byte G[8] = {B01111, B10000, B10000, B10111, B10111, B10001, B10001, B01110};
const byte H[8] = {B10001, B10001, B10001, B11111, B11111, B10001, B10001, B10001};
const byte I[8] = {B11111, B00100, B00100, B00100, B00100, B00100, B00100, B11111};
const byte J[8] = {B11111, B00100, B00100, B00100, B00100, B10100, B10100, B11100};
const byte K[8] = {B10001, B10010, B10100, B11000, B11000, B10100, B10010, B10001};
const byte L[8] = {B10000, B10000, B10000, B10000, B10000, B10000, B10000, B11111};
const byte M[8] = {B10001, B11011, B11011, B10101, B10001, B10001, B10001, B10001};
const byte N[8] = {B10001, B11001, B11101, B10101, B10101, B10011, B10011, B10001};
const byte O[8] = {B01110, B10001, B10001, B10001, B10001, B10001, B10001, B01110};
const byte P[8] = {B11111, B10001, B10001, B11111, B10000, B10000, B10000, B10000};
const byte Q[8] = {B01110, B10001, B10001, B10001, B10001, B10001, B01110, B00001};
const byte R[8] = {B11110, B10001, B10001, B10001, B11110, B10010, B10001, B10001};
const byte S[8] = {B01111, B10000, B10000, B01110, B01110, B00001, B00001, B11111};
const byte T[8] = {B11111, B00100, B00100, B00100, B00100, B00100, B00100, B00100};
const byte U[8] = {B10001, B10001, B10001, B10001, B10001, B10001, B10001, B11111};
const byte V[8] = {B10001, B10001, B10001, B10001, B01010, B01010, B01010, B00100};
const byte W[8] = {B10001, B10001, B10101, B10101, B10101, B10101, B10101, B01110};
const byte X[8] = {B10001, B10001, B01010, B00100, B00100, B01010, B10001, B10001};
const byte Y[8] = {B10001, B10001, B01010, B00100, B00100, B00100, B00100, B00100};
const byte Z[8] = {B11111, B00001, B00010, B00100, B00100, B01000, B10000, B11111};
const byte one[8] = {B11100, B00100, B00100, B00100, B00100, B00100, B00100, B11111};
const byte two[8] = {B11110, B00001, B00001, B01110, B01110, B10000, B10000, B01111};
const byte three[8] = {B11110, B00001, B00001, B00001, B01110, B00001, B00001, B11110};
const byte four[8] = {B10001, B10001, B10001, B11111, B00001, B00001, B00001, B00001};
const byte six[8] = {B10000, B10000, B10000, B10000, B11111, B10001, B10001, B11111};
const byte seven[8] = {B11111, B00001, B00001, B00001, B00010, B00010, B00100, B00100};
const byte eight[8] = {B01110, B10001, B10001, B01110, B10001, B10001, B10001, B01110};
const byte nine[8] = {B11111, B10001, B10001, B111111, B00001, B00001, B00001, B00001};
const byte *letter_arr[] = {A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, O, one, two, three, four, S, six, seven, eight, nine};


void setup() {
  // put your setup code here, to run once:
  const int led_data_pin = 3;
  FastLED.addLeds<WS2812B, led_data_pin, GRB>(leds, NUM_LED);
  set_strip_off();
  Serial.begin(9600);
  Serial.setTimeout(1000000);

  Serial.print("ready");


}

void loop() {
  //see if new song/artist name from serial port
  if (Serial.available()) {
    get_message();
    Serial.println(s);
    Serial.println(artist);
    cur_pos = NUM_LED / 8;
  }
  //does the actual LED stuff
  delay(50);
  scroll_message();

}

void scroll_message() {
  set_strip_off();
  int total_written = 0;
  int displacement = 0;
  for (int i = 0; i < s_len; i++) {
    if (s[i] == ' ') {
      displacement += 3;
    }
    else if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')) {
      total_written += write_letter(s[i], cur_pos + displacement, false);
      displacement += 6;
    }
  }
  displacement += 6;
  for (int i = 0; i < artist_len; i++) {
    if (artist[i] == ' ') {
      displacement += 3;
    }
    else if ((artist[i] >= 'a' && artist[i] <= 'z') || (artist[i] >= 'A' && artist[i] <= 'Z') || (artist[i] >= '0' && artist[i] <= '9')) {
      total_written += write_letter(artist[i], cur_pos + displacement, true);
      displacement += 6;
    }
  }
  FastLED.show();
  cur_pos -= 1;
  if (total_written == 0 && cur_pos != (NUM_LED / 8 - 1)) {
    cur_pos = NUM_LED / 8;
  }

}

int write_letter(char let, int pos, bool is_artist) {
  int written = 0;
  const byte *letter;
  if ((let >= 'A' && let <= 'Z')) {
    letter = letter_arr[let - 65];
  }
  else if((let >= '0' && let <= '9')){
    letter = letter_arr[let - 48 + 26];
    }
  
  for (int i = 0; i < 8; i++) {
    byte mask = B10000;
    for (int j = 0; j < 5; j++) {
      int add = (j + pos) % 2 == 0 ? i : 7 - i;
      int value = 8 * (j + pos) + add;
      if ((mask & letter[i]) > 0 && value >= 0 && value < NUM_LED) {
        //Serial.println(value);
        if (!is_artist) {
          leds[value] = CRGB (10, 0, 0);
        }
        else {
          leds[value] = CRGB (0, 0, 3);
        }
        written += 1;
      }
      mask = mask >> 1;
    }
  }
  return written;
}//returns total amount of leds written


void get_message() {
  while (!end_message) {
    recvWithEndMarker();
  }
  end_message = false;
}

void set_strip_off() {
  for (int i = 0; i < NUM_LED; i++) {
    leds[i] = CRGB::Black;
  }
}

void recvWithEndMarker() {
  for (int i = 0; i < LONGEST_NAME; i++) {
    s[i] = '\0';
    artist[i] = '\0';
  }

  for (int i = 0; i < 2; i++) {
    int idx = 0;
    char last_read = ' ';
    while (last_read != '\n') {
      while (Serial.available() == 0) {
      }
      last_read = Serial.read();
      if ((toupper(last_read) >= 'A' && toupper(last_read) <= 'Z') || last_read == ' ' || (last_read >= '0' && last_read <= '9')) {
        if (i == 0) {
          s[idx] = toupper(last_read);
        }
        else {
          artist[idx] = toupper(last_read);
        }
        idx += 1;
      }
    }
    if (i == 0) {
      s_len = idx + 1;
    }
    else {
      artist_len = idx + 1;
    }
  }

  end_message = true;
}
