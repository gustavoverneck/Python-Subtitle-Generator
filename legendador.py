# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import moviepy.editor
import assemblyai as aai
from deep_translator import GoogleTranslator

print("### Python Subtitle Generator")

lang_from=input("\n Por favor insira o código da língua de origem: ")
lang_to=input("\n Por favor insira o código da língua que deseja: ")
video_name = input("\n Insira o nome do arquivo de vídeo com a extensão: ")

print("Converting MP4 -> MP3 ...")
###     MP4-MP3 converter
video = moviepy.editor.VideoFileClip(video_name)
video.audio.write_audiofile("audio.mp3")

print("Transcribing...")
###     Transcribring
aai.settings.api_key = "INSERT HERE YOUT ASSEMBLYAI SEED"

# Adicionar o código do idioma
config = aai.TranscriptionConfig(language_code=lang_from)

transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe("./audio.mp3")

#print(transcript.export_subtitles_srt())

with open("legenda-{}}.srt".format(lang_from), "w") as f:
    f.write(transcript.export_subtitles_srt())
f.close()

print("Translating...")
###     Translating
legenda = transcript.export_subtitles_srt().splitlines()


i = 2
while (i <= len(legenda)):    
    legenda[i] = GoogleTranslator(source=lang_from, target=lang_to).translate(legenda[i])
    i += 4

with open("legenda-{}.srt".format(lang_to), "w") as f2:
    for i in legenda:
        f2.write(i)
        f2.write("\n")

print("Done!")

