import argparse
import pathlib
import shutil
from datetime import timedelta

import asyncio
from utils4audio.duration import get_duration

DURATION_MINUTES_MIN = 1
DURATION_MINUTES_MAX = 480
DURATION_MINUTES_DEFAULT = 39

DELTA_SECONDS_MIN = 0
DELTA_SECONDS_MAX = 900
DELTA_SECONDS_DEFAULT = 5

SET_MAGIC_TAIL_DEFAULT = True

GOLDEN_RATIO = 1.618

THRESHOLD_DURATION_MINUTES_MIN = 13
THRESHOLD_DURATION_MINUTES_MAX = 512
THRESHOLD_DURATION_MINUTES_DEFAULT = 101


def time_format(seconds):
    if not isinstance(seconds, int):
        print('🛑 time_format(): Variable is not int')
        return '00:00:00'
    if seconds < 0:
        print('🛑 time_format(): Variable is < 0 ')
        return '00:00:00'

    return '{:0>8}'.format(str(timedelta(seconds=int(seconds))))


def get_split_audio_scheme(
        source_audio_length: int,
        duration_seconds: int,
        delta_seconds: int,
        magic_tail: bool = True,
        threshold_seconds: int = THRESHOLD_DURATION_MINUTES_DEFAULT
):
    source_audio_length = int(source_audio_length)
    duration_seconds = int(duration_seconds)
    delta_seconds = int(delta_seconds)
    threshold_seconds = int(threshold_seconds)

    scheme = []
    time = 0
    if source_audio_length < threshold_seconds:
        scheme = [[0, source_audio_length + 1]]
        return scheme

    while time < source_audio_length:
        if time == 0:
            scheme.append([time, time + duration_seconds + delta_seconds])
        elif time + duration_seconds > source_audio_length:
            # Golden ration
            if magic_tail:
                ratio = duration_seconds / (source_audio_length - time + delta_seconds)
                if ratio > GOLDEN_RATIO:
                    scheme[-1][1] = source_audio_length
                else:
                    # Add one second to add all
                    scheme.append([time - delta_seconds, source_audio_length + 1])
            else:
                scheme.append([time - delta_seconds, source_audio_length + 1])
        else:
            scheme.append([time - delta_seconds, time + duration_seconds + delta_seconds])
        time += duration_seconds

    return scheme

async def run_command(cmd):
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()
    return stdout, stderr


async def run_cmds(cmds_list):
    tasks = [run_command(cmd) for cmd in cmds_list]
    await asyncio.gather(*tasks)

async def make_split_audio(
        audio_path: pathlib.Path,
        audio_duration: int = 0,
        output_folder: pathlib.Path = pathlib.Path('.'),
        scheme=None
):
    if scheme is None:
        scheme = []

    audios = []
    if not scheme:
        print('🟥 Unexpected Error in construction parts.')
        return audios
    if len(scheme) == 1:
        solo_audio = output_folder.joinpath(audio_path.name)
        if not solo_audio.exists():
            shutil.copy2(audio_path, solo_audio)
        audios = [{
            'path': solo_audio,
            'duration': audio_duration,
            'start': 0,
            'end': audio_duration
        }]
    else:
        cmds_list = []
        for idx, part in enumerate(scheme, start=1):
            output_file = output_folder.joinpath(audio_path.name).with_stem(f'{audio_path.stem}-p{idx}-of{len(scheme)}')
            print('💜', output_file)
            audios.append({
                'path': output_file,
                'duration': part[1] - part[0],
                'start': part[0],
                'end': part[1]
            })
            #   https://www.youtube.com/watch?v=HlwTLyfB3QU
            cmd = (f'ffmpeg -i {audio_path.as_posix()} -ss {time_format(part[0])} -to {time_format(part[1])} '
                   f'-c copy -y {output_file.as_posix()}')
            print(cmd)
            cmds_list.append(cmd.split(' '))

        await run_cmds(cmds_list)

        print("🟢 All Done! Lets see .m4a files and their length")

    return audios

async def split_audio(
        path: pathlib.Path,
        output_folder: pathlib.Path = pathlib.Path('.'),
        duration_minutes: int = DURATION_MINUTES_DEFAULT,
        delta_seconds: int = DELTA_SECONDS_DEFAULT,
        magic_tail: bool = SET_MAGIC_TAIL_DEFAULT,
        threshold_minutes: int = THRESHOLD_DURATION_MINUTES_DEFAULT,

):
    audio_duration = get_duration(path)
    scheme = get_split_audio_scheme(
        source_audio_length=audio_duration,
        duration_seconds=duration_minutes * 60,
        delta_seconds=delta_seconds,
        magic_tail=magic_tail,
        threshold_seconds=threshold_minutes * 60
    )
    audio_parts = await make_split_audio(
        audio_path=path,
        audio_duration=audio_duration,
        output_folder=output_folder,
        scheme=scheme
    )
    return audio_parts


async def main():
    parser = argparse.ArgumentParser(description='🪓 Audio split into parts')
    parser.add_argument('path',
                        type=pathlib.Path,
                        help='Input audio path')
    parser.add_argument('--folder',
                        type=pathlib.Path,
                        help='Output folder (default is . )',
                        default=pathlib.Path('.'))
    parser.add_argument('--magictail',
                        type=int, help='1=True (default), 0=False',
                        default=1)
    parser.add_argument('--duration',
                        type=int,
                        help='Split duration audio in MINUTES (default is 39 minutes)',
                        default=DURATION_MINUTES_DEFAULT)
    parser.add_argument('--delta',
                        type=int,
                        help='Delta in SECONDS which add intersections (default is 5 seconds)',
                        default=DELTA_SECONDS_DEFAULT)
    parser.add_argument('--threshold',
                        type=int,
                        help='Threshold duration MINUTES (default is 101 = 1h41m) ',
                        default=THRESHOLD_DURATION_MINUTES_DEFAULT)

    args = parser.parse_args()

    path = pathlib.Path(args.path)
    if not path.exists():
        print(f'🟥 Input audio path doesn t exist. '
              f'Check it and send me the command again.')
        return

    if args.duration < DURATION_MINUTES_MIN or args.duration > DURATION_MINUTES_MAX:
        print(f'🟥 Your split duration is: {args.duration}. '
              f'It is not in [{DURATION_MINUTES_MIN, DURATION_MINUTES_MAX}]. '
              f'Check it and send me the command again.')
        return

    if args.delta < DELTA_SECONDS_MIN or args.delta > DELTA_SECONDS_MAX:
        print(f'🟥 Your delta duration is: {args.delta}. '
              f'It is not in [{DELTA_SECONDS_MIN, DELTA_SECONDS_MAX}]. '
              f'Check it and send me the command again.')
        return

    if args.threshold < THRESHOLD_DURATION_MINUTES_MIN or args.threshold > THRESHOLD_DURATION_MINUTES_MAX:
        print(f'🟥 Your threshold duration is: {args.threshold}. '
              f'It is not in [{THRESHOLD_DURATION_MINUTES_MIN, THRESHOLD_DURATION_MINUTES_MAX}]. '
              f'Check it and send me the command again.')
        return

    magic_tail = True
    if args.magictail == 0:
        magic_tail = False
    elif args.magictail == 1:
        magic_tail = True
    else:
        print(f'🟥 Magic tail value is not 0 or 1. '
              f'Check it and send me the command again.')
        return

    folder = pathlib.Path(args.folder)
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)

    audios = await split_audio(
        path=path,
        duration_minutes=args.duration,
        delta_seconds=args.delta,
        magic_tail=magic_tail,
        output_folder=folder,
        threshold_minutes=args.threshold
    )
    print(audios)


if __name__ == "__main__":
    asyncio.run(main())
