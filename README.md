This project is for running **Stremio** using ADB commands on a **FireStick** to search for a movie/tv show and play the video using voice input.
The idea is to run this on a Raspberry Pi which is always listening like a Google Home/Alexa , but can run in any Python env in Windows/Linux/Mac.

It utilizes Google's gemini-2.5-flash model to determine whether a Title is a Show or a Movie. **(This model is currently free of cost and pretty fast).**

Could've scraped a dataset to determine this as well, however seemed like given the huge library of shows and movies would be slower than just hitting this endpoint.

Few Steps before running this.
1. Access your FireTVs settings and enable ADB 
2. Generate a Google AI Studio API Key from: https://aistudio.google.com/app/apikey
3. Make sure whichever system/server thats running the python code is on the same network as the FireTV.
4. Make sure you can connect the FireTV using ADB on your system:

    `adb connect 192.168.x.x`
5. Modify the .env file and enter the API Key from aistudio as well as your FireTV's IP
6. if you're running code on a Mac:
* ARM Mac:
```
brew install portaudio
pip install pyaudio --global-option='build_ext' --global-option='-I/opt/homebrew/include' --global-option='-L/opt/homebrew/lib'
```
* Intel Mac:
```
pip install pyaudio --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib'
```
* Windows or Linux should just work by installing the requirements.txt
7. Running the code:
* Open terminal in your solution's folder
  ```
  python -m venv venv  # Create a virtual environment
  source venv/bin/activate  # Activate on macOS/Linux
  venv\Scripts\activate  # Activate on Windows
  pip install -r requirements.txt
7. Run the code 
8. Speak the title of the show/movie and it should atleast bring you to the Post search menu.


**NOTE** :This probably works with other Android based TV's as well. Also might need to play around with the timings if it doesn't work for your setup.