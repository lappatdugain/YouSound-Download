import logging
import tempfile
from flask import Flask, render_template, request, send_file
from pytube import YouTube
from moviepy.editor import *
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def url():
    date = datetime.today().strftime("%Y-%m-%d %H:%M")
    logging.basicConfig(filename='LogsDownload.log', level=logging.WARNING)
    if request.method == 'POST':
        url_video = request.form['url']

        def progression(stream, chunk, bytes_remaining):
            bytes_downloaded = stream.filesize - bytes_remaining
            percent = bytes_downloaded * 100 / stream.filesize
            print(int(percent))

        conversion_type = request.form['conversion_type']
        print(f"URL submitted: {url_video}")
        yt = YouTube(url_video)
        yt.register_on_progress_callback(progression)
        title = yt.title
        # Gere les erreurs liées aux noms blizzard de video
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
                    # Téléchargement du fichier sur le serveur 
                    logging.info(f"Download completed for URL: {url_video} made on : {date} types : audio")
                    flux = yt.streams.get_audio_only()
                    flux.download(output_path=tmp_file, filename=f'{title}.mp4')

                    # Création du chemin d'accès pour le fichier
                    mp3 = os.path.join(tmp_file, f'{title}.mp3')
                    with AudioFileClip(os.path.join(tmp_file, f'{title}.mp4')) as video:
                        video.write_audiofile(mp3)
                    """progression(flux)"""
                    # as_attachment donner l'info au navigateur que le fichier est comme une pièce jointe téléchargeable
                    return send_file(mp3, as_attachment=True)

                elif conversion_type == 'mp4':
                    # Téléchargement du fichier sur le serveur 
                    logging.info(f"Download completed for URL: {url_video} made on : {date} types : video")
                    flux = yt.streams.get_highest_resolution()
                    flux.download(output_path=tmp_file, filename=f'{title}.mp4')

                    # Création du chemin d'accès pour le fichier
                    mp4 = os.path.join(tmp_file, f'{title}.mp4')

                    # as_attachment donner l'info au navigateur que le fichier est comme une pièce jointe téléchargeable
                    return send_file(mp4, as_attachment=True)


            else:
                logging.warning(f"No flux found for URL: {url_video}")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
