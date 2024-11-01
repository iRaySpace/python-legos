

class SubtitleLine:
    idx: int
    start: int
    end: int
    text: str

    def __init__(self, **kwargs):
        self.idx = kwargs.get('idx')
        self.start = kwargs.get('start')
        self.end = kwargs.get('end')
        self.text = kwargs.get('text')

    def __str__(self):
        return f'[{self.start}:{self.end}]\n{self.text}'


def _parse_srt_timestamp(srt_timestamp):
    hours, minutes, seconds = srt_timestamp.split(":")
    seconds, milliseconds = seconds.split(",")
    return (
        int(hours) * 60 * 60 * 1000 +
        int(minutes) * 60 * 1000 +
        int(seconds) * 1000 +
        int(milliseconds)
    )


def _make_subtitle_line(entry):
    lines = entry.splitlines()
    idx = lines.pop(0)
    srt_timestamp = lines.pop(0)
    start, end = srt_timestamp.split(' --> ')
    start = _parse_srt_timestamp(start)
    end = _parse_srt_timestamp(end)
    text = "\n".join(lines)
    return SubtitleLine(
        idx=idx,
        start=start,
        end=end,
        text=text,
    )


def run():
    data = None

    file_path = 'test.srt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().strip()

    subtitle_lines = []

    entries = data.split('\n\n')
    for entry in entries:
        subtitle_lines.append(_make_subtitle_line(entry))

    print("Total - Subtitle Lines:", len(subtitle_lines))


if __name__ == "__main__":
    run()
