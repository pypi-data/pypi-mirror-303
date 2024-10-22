from models.song import Song
from utils import get_soup

def get_songs_from_table(table):
    table_rows = table.find_all("tr")

    songs: list[Song] = []

    for tr in table_rows:
        tds = tr.find_all("td")
        idx = tds[0].text.strip()
        link = tds[1].find("a")["href"]
        name = tds[1].find("a").text.strip()
        artist = tds[2].text.strip()

        songs.append(Song(idx, name, link, artist))

    return songs

class ParolesNet:
    def __init__(self):
        self.base_url = "https://www.paroles.net/"

    def get_songs_by_table_id(self, table_idx):
        soup = get_soup(self.base_url)
        tables = soup.find_all("table")
        table = tables[table_idx]
        songs = get_songs_from_table(table)
        return songs

    def get_new_songs(self):
        return self.get_songs_by_table_id(0)

    def get_best_songs(self):
        return self.get_songs_by_table_id(1)