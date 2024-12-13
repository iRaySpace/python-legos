import argparse
from math import ceil
from moviepy import AudioFileClip, ImageClip
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips


HOUR_IN_SECS = 3600


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()


def main():
    args = _get_args()

    audio_filename = args.filename
    audio_clip = AudioFileClip(f'./uploads/{audio_filename}')

    image_filename = audio_filename.replace('mp3', 'png')
    clip = ImageClip(f'./uploads/{image_filename}').with_duration(audio_clip.duration).with_audio(audio_clip)

    number_of_clips = ceil(HOUR_IN_SECS / clip.duration)
    final = concatenate_videoclips([clip for _ in range(number_of_clips)])

    video_filename = audio_filename.replace('mp3', 'mp4')
    final.write_videofile(f'./results/{video_filename}', fps=30)


if __name__ == '__main__':
    main()
