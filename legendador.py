# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import moviepy.editor
import assemblyai as aai
from deep_translator import GoogleTranslator

###     MP4-MP3 converter
video = moviepy.editor.VideoFileClip("ep1.mkv")
video.audio.write_audiofile("ep1-audio.mp3")

###     Transcribring

aai.settings.api_key = "f1cee072b30e4e98af78d0773bee0017"

#config = aai.TranscriptionConfig(language_detection=True)
config = aai.TranscriptionConfig(language_code="ja")

transcriber = aai.Transcriber(config=config)

transcript = transcriber.transcribe("./ep1-audio.mp3")

print(transcript.export_subtitles_srt())

with open("legenda-ep1.srt", "w") as f:
    f.write(transcript.export_subtitles_srt())

###     Translating
translated = GoogleTranslator(source='ja', target='pt').translate_file('./legenda-ep1.srt')