from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    if request.method == 'POST':
        if "text-input" in request.form:
            transcript = request.form['text-input']
        elif "audio-file" in request.files:
            audio_file = request.files['audio-file']
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                transcript = recognizer.recognize_google(audio_data)
    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True)