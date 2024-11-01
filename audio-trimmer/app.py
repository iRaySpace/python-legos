from pydub import AudioSegment


def run():
    audio = AudioSegment.from_mp3('sample.mp3')
    five_to_ten_audio = audio[5_000:10_000]
    five_to_ten_audio.export('exported.mp3', format='mp3')


if __name__ == '__main__':
    run()
