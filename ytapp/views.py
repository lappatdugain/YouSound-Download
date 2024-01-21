import os 
import logging
import tempfile
from flask import Flask, render_template, request, send_file, redirect, url_for
from pytube import YouTube
from moviepy.editor import * 
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])



def url():
    date=datetime.today().strftime("%Y-%m-%d %H:%M")
    logging.basicConfig(filename='LogsDownload.log', level=logging.WARNING)
    if request.method == 'POST':
        url = request.form['url']
        
        def progression(stream, chunk, bytes_remaining):
            bytes_dowloaded = stream.filesize - bytes_remaining
            percent= bytes_dowloaded * 100 / stream.filesize
            print(int(percent))
            
        conversion_type = request.form['conversion_type']
        print(f"URL submitted: {url}")
        yt = YouTube(url)
        yt.register_on_progress_callback(progression)
        title = yt.title
        # Gere les erreurs lié aux noms bizzard de video
        caracteres_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%','『』','「」']
        for caractere_special in caracteres_speciaux:
            title = title.replace(caractere_special, '_')
        logging.warn(f"Changing was effected on \n Original title : {yt.title} \n New title : {title}")        
        
        # Créatin d'un répertoire tmp
        with tempfile.TemporaryDirectory() as tmp_file:
            # Recuperation de l'url youtube
            flux = yt.streams
            
            if flux:
                if conversion_type == 'mp3':
                    # Telechargment du fichier sur le serveur 
                    logging.warn(f"Download completed for URL: {url} made on : {date} types : audio")
                    flux = yt.streams.get_audio_only()
                    flux.download(output_path=tmp_file, filename=f'{title}.mp4')
                    
                    # Création du chemain d'acces pour le fichier
                    mp3 = os.path.join(tmp_file, f'{title}.mp3')
                    with AudioFileClip(os.path.join(tmp_file, f'{title}.mp4')) as video:
                        video.write_audiofile(mp3)
                    
                    # as_attachment donner l'info au navigateur que le fichier est comme une pièce jointe telechargable
                    return send_file(mp3, as_attachment=True)
                
                elif conversion_type == 'mp4':
                    # Telechargment du fichier sur le serveur 
                    logging.warn(f"Download completed for URL: {url} made on : {date} types : video")
                    flux = yt.streams.get_highest_resolution()
                    flux.download(output_path=tmp_file, filename=f'{title}.mp4')
                    
                    # Création du chemain d'acces pour le fichier
                    mp4 = os.path.join(tmp_file, f'{title}.mp4')
                    
                    # as_attachment donner l'info au navigateur que le fichier est comme une pièce jointe telechargable
                    return send_file(mp4, as_attachment=True)
                
                
            else: logging.warning(f"No flux found for URL: {url}")  
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

