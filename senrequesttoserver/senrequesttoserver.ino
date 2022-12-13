
#include <WiFi.h>
#include <HTTPClient.h>
#include "Base64.h"
#include "esp_camera.h"

//#define CAMERA_MODEL_M5STACK_PSRAM
//#define CAMERA_MODEL_M5STACK_NO_PSRAM
#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"

const char* ssid = "bichngox";
const char* password = "Thanhlam";

//Your Domain name with URL path or IP address with path
const char* serverName = "http://bffb-27-138-216-119.jp.ngrok.io/api/test-cam/create/";

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 5000;

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();
  
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG; // for streaming
  //config.pixel_format = PIXFORMAT_RGB565; // for face detection/recognition
 // config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
 // config.fb_location = CAMERA_FB_IN_PSRAM;
  //config.jpeg_quality = 12;
  //config.fb_count = 1;

//  if(config.pixel_format == PIXFORMAT_JPEG){
//    if(psramFound()){
//      config.jpeg_quality = 10;
//      config.fb_count = 2;
//      //config.grab_mode = CAMERA_GRAB_LATEST;
//    } else {
//      // Limit the frame size when PSRAM is not available
//      config.frame_size = FRAMESIZE_SVGA;
//      //config.fb_location = CAMERA_FB_IN_DRAM;
//    }
//  } else {
//    // Best option for face detection/recognition
//    config.frame_size = FRAMESIZE_240X240;
//  }

  if(psramFound()){
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }
  
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }
    sensor_t * s = esp_camera_sensor_get();
  // initial sensors are flipped vertically and colors are a bit saturated
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1); // flip it back
    s->set_brightness(s, 1); // up the brightness just a bit
    s->set_saturation(s, -2); // lower the saturation
  }
  // drop down frame size for higher initial frame rate
  s->set_framesize(s, FRAMESIZE_QVGA);

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  randomSeed(analogRead(0));
  
}

long ranNumber;


String Photo2Base64(size_t* fb_len) {
    camera_fb_t * fb = NULL;
    fb = esp_camera_fb_get();  
    if(!fb) {
      Serial.println("Camera capture failed");
      return "";
    }
    *fb_len = fb->len;
  
    String imageFile = "";
    char *input = (char *)fb->buf;
    char output[base64_enc_len(3)];
    for (int i=0;i<fb->len;i++) {
      base64_encode(output, (input++), 3);
      if (i%3 == 0) {
        imageFile += String(output);
        
      }
      
    }
    
    esp_camera_fb_return(fb);
    
    return imageFile;
}

//https://github.com/zenmanenergy/ESP8266-Arduino-Examples/
String urlencode(String str)
{
    String encodedString="";
    char c;
    char code0;
    char code1;
    char code2;
    for (int i =0; i < str.length(); i++){
      c=str.charAt(i);
      if (c == ' '){
        encodedString+= '+';
      } else if (isalnum(c)){
        encodedString+=c;
      } else{
        code1=(c & 0xf)+'0';
        if ((c & 0xf) >9){
            code1=(c & 0xf) - 10 + 'A';
        }
        c=(c>>4)&0xf;
        code0=c+'0';
        if (c > 9){
            code0=c - 10 + 'A';
        }
        code2='\0';
        encodedString+='%';
        encodedString+=code0;
        encodedString+=code1;
        //encodedString+=code2;
      }
      yield();
    }
    return encodedString;
}
int n = 1;
size_t fb_len;
void loop() {
  //Send an HTTP POST request every 10 minutes
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
    
      // Your Domain name with URL path or IP address with path
      http.begin(client, serverName);
      camera_fb_t * fb = NULL;
      fb = esp_camera_fb_get();

      n++;
      
      String data_frame = "{\"frame_buf\":\"";
      String base64frame = Photo2Base64(&fb_len);
      data_frame += base64frame;
      data_frame += "\"";
      data_frame += ",\"lenght\":";
      data_frame +=  fb_len;
      data_frame += ",\"veget\":";
      data_frame += n;
      data_frame += "}";
      
      if (n==3) {
        n = 0;
      }
      //String s = "jieorjwqiorjwoqijriwoqjrowiqjriwqjroiwqjriowqjirjieorjwqiorjwoqijriwoqjrowiqjriwqjroiwqjriowqjir" ;
      // If you need an HTTP request with a content type: application/json, use the following:
      http.addHeader("Content-Type", "application/json");
      int httpResponseCode = http.POST(data_frame);

      // If you need an HTTP request with a content type: text/plain
      //http.addHeader("Content-Type", "text/plain");
      //int httpResponseCode = http.POST("Hello, World!");
     
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      //Serial.println(s);
       
      // Free resources

      http.end();
    }
    else {
      Serial.println(
        "WiFi Disconnected");
      WiFi.begin(ssid, password);
    WiFi.setSleep(false);  
    while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
    }
    lastTime = millis();
  }
}
