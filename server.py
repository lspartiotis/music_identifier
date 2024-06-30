import os
from flask import Flask, render_template, request, jsonify
import sounddevice as sd
import wavio
from yt_dlp import YoutubeDL



app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():

    return jsonify({'result'})

@app.route('/download', methods=['POST'])
def download():

    data = request.get_json()
    youtube_url = data['youtube_url']
    # Define the output directory and file
    output_dir = 'song/'
    output_file = 'song.mp3'
    output_path = os.path.join(output_dir, output_file)

    # Check if the file exists and delete if it does
    if os.path.exists(output_path):
        os.remove(output_path)


    # yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractaudio': True,
        'audioformat': 'mp3',
    }

    # Download audio
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


    result = os.popen(f'python3 audfprint/audfprint.py match --dbase fingerprints.pklz song/song.mp3.mp3').read()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
