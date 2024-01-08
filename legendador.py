# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import moviepy.editor
import assemblyai as aai
from deep_translator import GoogleTranslator

print("### Python Subtitle Generator")

lang_from="ja"
lang_to="pt"

print("Converting MP4 -> MP3 ...")
###     MP4-MP3 converter
video = moviepy.editor.VideoFileClip("video.mp4")
video.audio.write_audiofile("audio.mp3")

print("Transcribing...")
###     Transcribring
aai.settings.api_key = "f1cee072b30e4e98af78d0773bee0017"

# Adicionar o código do idioma
config = aai.TranscriptionConfig(language_code=lang_from)

transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe("./audio.mp3")

#print(transcript.export_subtitles_srt())

with open("legenda-ja.srt", "w") as f:
    f.write(transcript.export_subtitles_srt())
f.close()
print("Translating...")
###     Translating
legenda = transcript.export_subtitles_srt().splitlines()


i = 2
while (i <= len(legenda)):    
    legenda[i] = GoogleTranslator(source=lang_from, target=lang_to).translate(legenda[i])
    i += 4

with open("legenda-pt.srt", "w") as f2:
    for i in legenda:
        f2.write(i)
        f2.write("\n")


print("Done!")
#translated = GoogleTranslator(source=lang_from, target=lang_to).translate_file('./legenda-{}.srt'.format(lang_from))

