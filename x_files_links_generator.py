def main():
    # See more about all seasons https://en.wikipedia.org/wiki/The_X-Files
    series = [24, 25, 24, 24, 20, 22, 22, 21, 20, 6, 10]
    season = get_int(1, len(series) + 1, 'What\'s season? ')
    for episode in episodes(series[season - 1]):
        print(f"episode {episode}:", get_hyperlink(season, episode))


def episodes(n):
    for i in range(1, n + 1):
        yield i


def get_hyperlink(season, episode):
    """
    Gets direct hyperlink to a video file.
    """
    return f'https://xf.mp4club.top/X-Files.s{season:0>2}e{episode:0>2}.XFilesSerial.club.mp4'


def get_int(start, end, prompt):
    """
    Gets integer value from user input in range [start, end).
    """
    while True:
        try:
            value = int(input(prompt))
            assert start <= value < end
            return value
        except ValueError:
            print('Value should be an integer')
        except AssertionError:
            print(f'Value should be an integer in range [{start}, {end})')


if __name__ == "__main__":
    main()
