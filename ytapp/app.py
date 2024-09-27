import logging
import tempfile
from venv import logging

from flask import Flask, render_template, flash, request, url_for, redirect, send_file
from flask_meld import Meld

from pytubefix import YouTube
from moviepy.editor import *
from datetime import datetime
import time

app = Flask(__name__)

# Initialize logging

@app.route("/", methods=['POST', 'GET'])
def url():
    logging.basicConfig(filename='LogsDownload.log', level=logging.INFO)

    def progression(stream, chunk, bytes_remaining):
        bytes_downloaded = stream.filesize - bytes_remaining
        percent = bytes_downloaded * 100 / stream.filesize
        print(f"Download progress: {int(percent)}%")

    try:
        if request.method == 'POST':
            date = datetime.today().strftime("%Y-%m-%d %H:%M")

            url_video = request.form['url']
            conversion_type = request.form['conversion_type']
            print(f"URL submitted: {url_video}")
            logging.info(f"URL submitted: {url_video}")

            yt = YouTube(url_video)
            yt.register_on_progress_callback(progression)
            title = yt.title

            # Handle special characters in the video title
            caractere_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%', '『』', '「」']
            for caractereSpecial in caractere_speciaux:
                title = title.replace(caractereSpecial, '_')
            logging.info(f"Changing was effected on \n Original title : {yt.title} \n New title : {title}")

            # Création d'un répertoire tmp
            with tempfile.TemporaryDirectory() as tmp_file:
                # Recuperation de l'URL youtube
                flux = yt.streams

                if flux:
                    if conversion_type == 'mp3':
                        logging.info(f"Download completed for URL: {url_video} made on : {date} types : audio")
                        flux = yt.streams.get_audio_only()
                        flux.download(output_path=tmp_file, filename=f'{title}.mp4')

                        # Convert MP4 to MP3
                        mp3 = os.path.join(tmp_file, f'{title}.mp3')
                        with AudioFileClip(os.path.join(tmp_file, f'{title}.mp4')) as video:
                            video.write_audiofile(mp3)
                        """progression(flux)"""
                        
                        logging.info(f"MP3 download complete: {mp3}")

                        # Send the MP3 file to the user
                        return send_file(mp3, as_attachment=True)


                    if conversion_type == 'mp4':
                        logging.info(f"Download completed for URL: {url_video} made on : {date} types : video")
                        flux = yt.streams.get_highest_resolution()
                        flux.download(output_path=tmp_file, filename=f'{title}.mp4')

                        # Création du chemin d'accès pour le fichier
                        mp4 = os.path.join(tmp_file, f'{title}.mp4')

                        logging.info(f"MP4 download complete: {mp4}")

                        # Send the MP3 file to the user
                        return send_file(mp4, as_attachment=True)

                else:
                    logging.warning(f"No flux found for URL: {url_video}")

        return render_template("index.html")

    except Exception as e:
        return render_template("error.html")





if __name__ == "__main__":
    app.run(debug=True,port=5500)
