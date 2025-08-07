from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BASE_MUSIC_FOLDER = os.path.join(os.getcwd(), 'music')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tamil')
def tamil():
    # Dictionary of song name to Cloudinary link
    songs = {
        "Anu Vidhaitha Boomiyele": "https://res.cloudinary.com/dafvnczuy/video/upload/v1754584117/Vishwaroopam_-_Anu_Vidhaiththa_Boomiyile_Video_Kamal_Haasan_klyebj.mp3",
       "Tamil Kuthu songs Playlist 1":"https://res.cloudinary.com/dafvnczuy/video/upload/v1754584832/tamil_kuthu_dance_item_songs_spmh_spstrength_qB1lXRBXmZA_hlliz1.webm"
    }

    return render_template('tamil_player.html', songs=songs, lang='tamil')

@app.route('/kannada')
def kannada():
    kannada_folder = os.path.join(BASE_MUSIC_FOLDER, 'kannada')
    songs = [f for f in os.listdir(kannada_folder) if f.endswith('.webm')]
    return render_template('simple.html', songs=songs, lang='kannada')

@app.route('/play/<lang>/<filename>')
def play(lang, filename):
    return send_from_directory(os.path.join(BASE_MUSIC_FOLDER, lang), filename)

if __name__ == '__main__':
    app.run(debug=True)
