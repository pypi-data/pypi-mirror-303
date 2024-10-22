from paroles_net import ParolesNet

if __name__ == '__main__':
    pn = ParolesNet()
    songs = pn.get_best_songs()

    song = songs[0]
    print(song)
    print(song.get_lyrics(and_save=True))