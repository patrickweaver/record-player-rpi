# Record Player for Raspberry Pi

This is a version of [Record Player](https://github.com/patrickweaver/record-player) that will run on a Raspberry Pi. It requires a [camera module](https://www.raspberrypi.org/products/camera-module-v2/) for the Raspberry Pi. You do not need a screen, but it helps to get the camera positioned correctly.

This is a [Rube Goldberg Machine](https://en.wikipedia.org/wiki/Rube_Goldberg_machine) of the [Google Cloud Vision API](https://cloud.google.com/vision/) and the [Spotify API](https://beta.developer.spotify.com/documentation/web-api/). After logging into Spotify, upload an image. The image will be sent to the Google Vision API, which will guess what it is. The app will then search Spotify using Google's guess, and give you the first result to play.

You will need the following to make your own:

- [Google Cloud API Key](https://cloud.google.com/docs/authentication/api-keys) (this is set as GCP_API_KEY ENV variable)
- Create a [Spotify App](https://beta.developer.spotify.com/dashboard/applications) (SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET ENV variables)
- SPOTIFY_STATE_STRING env variable is used to confirm the correct redirect during Spotify auth.

Set PORT ENV variable to 3000

### On the Raspberry Pi:

- Set Chromim to allow spotify to play music:

    - Settings > Advanced > Content Settings > Flash
        - Allow:
            - https://open.spotify.com
    - Install 'User-Agent Switcher for Chome' from Chrome web store
    - Set User-Agent to Firefox Windows

## Starting the apps:

Start the Node.js server:

`PORT=3000 npm start`

In another terminal tab or after sending the node server to the backgorund, start the Python camera script:

`python3 camera.py`





