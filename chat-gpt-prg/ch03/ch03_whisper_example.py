# 터미널 창에 pip install openai==0.28 실행 필수

import openai

# API 키 입력
openai.api_key = "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"

# 녹음 파일 읽어오기
audio_file = open("output.mp3", "rb")

# whisper 모델에 음원 파일 전달하기
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# 결과 보기
print(transcript['text'])