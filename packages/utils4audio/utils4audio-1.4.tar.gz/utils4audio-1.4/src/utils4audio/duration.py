import pathlib
from mutagen.mp4 import MP4
from pydub import AudioSegment


def get_duration_light(path: pathlib.Path):
    path = pathlib.Path(path)
    if not path.exists():
        print('🟥 Path not exists.')
        return

    if path.suffix not in ['.m4a']:
        print('🟥 Suffix is no .m4a')
        return

    try:
        audio = MP4(path.as_posix())
    except Exception as e:
        return str(e)

    duration_seconds = None
    if audio.info.length:
        duration_seconds = int(audio.info.length)

    return duration_seconds


def get_duration_heavy(path: pathlib.Path):
    path = pathlib.Path(path)
    if not path.exists():
        print('🟥 Path not exists.')
        return

    if path.suffix not in ['.m4a']:
        print('🟥 Suffix is no .m4a')
        return

    try:
        audio = AudioSegment.from_file(path.as_posix(), format="m4a")
        duration_ms = len(audio)
    except Exception as e:
        return str(e)

    ds = duration_ms / 1000.0

    return int(ds) + (not ds.is_integer())


def get_duration(path: pathlib.Path):
    path = pathlib.Path(path)
    if not path.exists():
        print('🟥 Path not exists.')
        return

    if path.suffix not in ['.m4a']:
        print('🟥 Suffix is no .m4a')
        return

    duration = get_duration_light(path)
    if not isinstance(duration, str) or duration is None:
        return duration

    #duration = get_duration_heavy(path)
    #if not isinstance(duration, str) or duration is None:
    #    return duration

    print('🟥 Cant get utils4audio light and heavy audio. Sorry.')
    return


async def get_duration_asynced(path: pathlib.Path):
    path = pathlib.Path(path)
    if not path.exists():
        print('🟥 Path not exists.')
        return

    if path.suffix not in ['.m4a']:
        print('🟥 Suffix is no .m4a')
        return

    duration = get_duration_light(path)
    if not isinstance(duration, str) or duration is None:
        return duration

    #duration = get_duration_heavy(path)
    #if not isinstance(duration, str) or duration is None:
    #    return duration

    print('🟥 Cant get utils4audio light and heavy audio. Sorry.')
    return
