from os import path
from configparser import ConfigParser
from pyrogram import Client
from shazamio import Shazam, exceptions

shazam = Shazam()

class bot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = {'root': path.join(__package__, 'plugins')}
        api_id = config.get('pyrogram', 'api_id')
        api_hash = config.get('pyrogram', 'api_hash')
        super().__init__(
            name,
            api_id=api_id,
            api_hash=api_hash,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
        )

    async def start(self):
        await super().start()
        print("Bot başladı. Salam.")

    async def stop(self, *args):
        await super().stop()
        print("Bot dayandı. Gülə-gülə.")

    async def recognize(self, path):
        try:
            result = await shazam.recognize_song(path)
            return result
        except exceptions.FailedDecodeJson:
            return "Şarkı tanınamadı!"

    async def related(self, track_id):
        try:
            related_tracks = await shazam.related_tracks(track_id=track_id, limit=50, start_from=2)
            return related_tracks['tracks']
        except exceptions.FailedDecodeJson:
            return None

    async def get_artist(self, query: str):
        try:
            artists = await shazam.search_artist(query=query, limit=50)
            hits = []
            for artist in artists['artists']['hits']:
                hits.append(artist)  # 'FactoryArtist' kaldırıldı
            return hits
        except KeyError:
            return None

    async def get_artist_tracks(self, artist_id: int):
        try:
            tracks = await shazam.artist_top_tracks(artist_id=artist_id, limit=50)
            top_tracks = []
            for track in tracks['tracks']:
                top_tracks.append(track)  # 'FactoryTrack' kaldırıldı
            return top_tracks
        except KeyError:
            return None
