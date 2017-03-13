from mutagen.easyid3 import EasyID3
from mutagen import File
from flask import render_template


def change_artwork(file):
    file = File(file)  # mutagen can automatically detect format and type of tags
    artwork = file.tags['APIC:'].data  # access APIC frame and grab the image
    print artwork

def view_tags(file):
    audio = EasyID3(file)
    return audio
    #audio.save()

def fix_song(file):
    try:
        data = view_tags(file)
    except Exception as error:
        return "file is not a mp3 file"
    return render_template("song_template.html",
                           title_name=data['title'], author=data['artist'],
                           album=data['album'])
