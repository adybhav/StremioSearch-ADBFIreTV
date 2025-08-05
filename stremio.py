import subprocess
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()
PACKAGE = "com.stremio.one"
API_KEY = os.getenv("GEMINI_API_KEY")
DEVICE_IP = os.getenv("DEVICE_IP")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
def classify_title_with_gemini(title):
    prompt = f"Is '{title}' a movie or a TV show? Just reply with 'movie' or 'series'."

    response = model.generate_content(prompt)
    answer = response.text.strip().lower()

    if "movie" in answer:
        return "movie"
    elif "series" in answer or "tv show" in answer:
        return "series"
    else:
        return "unknown"

def adb(cmd):
    result = subprocess.run(["adb"] + cmd.split(), capture_output=True, text=True)
    return result.stdout.strip()

def press(key, delay=0.1):
    print(f"🔘 Pressing: {key}")
    adb(f"shell input keyevent {key}")
    time.sleep(delay)

def navigate_to_search():
    press("21")  # DPAD_LEFT
    press("19")  # DPAD_UP
    press("66")  # SELECT (OK)

def play_show():
    press("20")
    time.sleep(0.3)
    press("66")

def play_movie():
    press("66")
    time.sleep(0.5)
    press("66")
def search_for(query,type):
    safe_query = query.replace(" ", "_")

    print(f"🔍 Typing search query: {query}")
    subprocess.run(["adb", "shell", "input", "text", safe_query])
    time.sleep(0.1)

    print("⬇️ Navigating down to on-screen Next and selecting...")
    press("61")  # SELECT
    time.sleep(0.5)
    if type == "movie":
        play_movie()
    elif type == "series":
        play_show()

def main():
    title = get_voice_input()

    print("🔌 Connecting to Fire Stick...")
    adb(f"connect {DEVICE_IP}")

    print("🚀 Launching Stremio...")
    adb(f"shell monkey -p {PACKAGE} -c android.intent.category.LAUNCHER 1")
    time.sleep(0.5)

    type = classify_title_with_gemini(title)
    print(type)
    print("🎮 Navigating to content...")
    navigate_to_search()
    search_for(title, type)
    print("Complete")

def get_voice_input(prompt="🎤 Say the title now..."):
    print(prompt)
    result = subprocess.check_output(["termux-speech-to-text"])
    return result.decode().strip()

if __name__ == "__main__":
    main()
