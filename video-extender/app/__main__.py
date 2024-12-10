import argparse
from math import ceil
from moviepy import VideoFileClip
# from moviepy.video.fx.MirrorX import MirrorX
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips


HOUR_IN_SECS = 3600


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()


def main():
    args = _get_args()
    clip = VideoFileClip(f'./uploads/{args.filename}')
    # clip = clip.with_effects([MirrorX()])
    # clip.write_videofile(f'./results/flipped_{args.filename}')
    number_of_clips = ceil(HOUR_IN_SECS / clip.duration)
    final = concatenate_videoclips([clip for _ in range(number_of_clips)])
    final.write_videofile(f'./results/{args.filename}', fps=30)



if __name__ == '__main__':
    main()
