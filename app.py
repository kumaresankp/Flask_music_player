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
       "Tamil Kuthu songs Playlist 1":"https://res.cloudinary.com/dafvnczuy/video/upload/v1754584832/tamil_kuthu_dance_item_songs_spmh_spstrength_qB1lXRBXmZA_hlliz1.webm",
       "Prabakaran Pera solli":"https://res.cloudinary.com/dafvnczuy/video/upload/v1754585939/Prabhakaran_Peyarai_Solli_C-2g0QfQAAg_aa8gvs.webm",
       "Desame Prabakaran":"https://res.cloudinary.com/dafvnczuy/video/upload/v1754585934/%E0%AE%A4%E0%AF%87%E0%AE%9A%E0%AE%AE%E0%AF%87_%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AA%E0%AE%BE%E0%AE%95%E0%AE%B0%E0%AE%A9%E0%AF%8D_-_%E0%AE%AA%E0%AE%BE%E0%AE%9F%E0%AE%B2%E0%AF%8D_%E0%AE%87%E0%AE%AF%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D_%E0%AE%9A_%E0%AE%AE%E0%AF%81%E0%AE%B0%E0%AE%B3%E0%AE%BF_%E0%AE%AE%E0%AE%A9%E0%AF%8B%E0%AE%95%E0%AE%B0%E0%AF%8D_%E0%AE%87%E0%AE%9A%E0%AF%88_%E0%AE%9A._%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AA%E0%AE%BE%E0%AE%95%E0%AE%B0%E0%AE%A9%E0%AF%8D_lgt5_mhwyiY_txd35r.webm",
       "Karum Puli Veeran":"https://res.cloudinary.com/dafvnczuy/video/upload/v1754585934/%E0%AE%95%E0%AE%B0%E0%AF%81%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AF%81%E0%AE%B2%E0%AE%BF_%E0%AE%B5%E0%AF%80%E0%AE%B0%E0%AE%A9%E0%AF%8D_%E0%AE%B5%E0%AE%B0%E0%AE%BE%E0%AE%B0%E0%AF%81_Song_I_Karumpuli_Veeran_Vararu_Song_Seeman_I_Maam_Tamilar_Katchi_Song_I_NTK_VtBazWPGuo4_ixwko7.webm",
       "Theemai dhan vellum": "https://res.cloudinary.com/dafvnczuy/video/upload/v1754585930/Thani_Oruvan_-_Theemai_Dhaan_Vellum_Lyric_Jayam_Ravi_Nayanthara_Hiphop_Tamizha_tkql_yvuSK0_makgpx.webm"
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
