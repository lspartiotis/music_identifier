import os
from flask import Flask, render_template, request, jsonify
import sounddevice as sd
import wavio
from yt_dlp import YoutubeDL



app = Flask(__name__)


def identify_song():
    result = os.popen(f'python3 audfprint/audfprint.py match --dbase fingerprints.pklz song/song.mp3.mp3 {output_path}').read()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():

    return jsonify({'result'})

@app.route('/download', methods=['POST'])
def download():
    # Define the output directory and file
    output_dir = os.path.expanduser('song/')
    output_file = 'song.mp3.mp3'
    output_path = os.path.join(output_dir, output_file)

    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Check if the file exists and delete it
    if os.path.exists(output_path):
        os.remove(output_path)

    # Recording settings
    duration = 5  # Duration in seconds
    fs = 44100    # Sample rate
    channels = 1  # Mono recording

    print("Recording...")

    # Record audio
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()

    # Save as WAV first, then convert to MP3
    wav_path = os.path.join(output_dir, 'temp.wav')
    wavio.write(wav_path, audio, fs, sampwidth=2)

    # Convert WAV to MP3 using ffmpeg
    os.system(f'ffmpeg -i {wav_path} -codec:a libmp3lame -qscale:a 2 {output_path}')
    os.remove(wav_path)

    print(f"Recording saved as {output_path}")

    result = os.popen(f'python3 audfprint/audfprint.py match --dbase fingerprints.pklz song/song.mp3.mp3 {output_path}').read()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
