import scanner


def main():
    # See more about all seasons https://en.wikipedia.org/wiki/The_X-Files
    series = [24, 25, 24, 24, 20, 22, 22, 21, 20, 6, 10]
    season = scanner.get_int(1, len(series), "What's season? ")
    for episode in episodes(series[season - 1]):
        print(f"episode {episode}:", get_hyperlink(season, episode))


def episodes(n):
    """
    Generates a sequence of episodes in range [1, n].
    """
    for i in range(1, n + 1):
        yield i


def get_hyperlink(season, episode):
    """
    Gets direct hyperlink to a video file.
    """
    return f"https://xf.mp4club.top/X-Files.s{season:0>2}e{episode:0>2}.XFilesSerial.club.mp4"


if __name__ == "__main__":
    main()
