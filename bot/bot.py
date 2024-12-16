from pyrogram import Client
from shazamio import Shazam, exceptions, FactoryArtist, FactoryTrack

shazam = Shazam()

class Bot(Client):
    def __init__(self, name, api_id, api_hash):
        super().__init__(
            name,
            api_id=api_id,
            api_hash=api_hash,
            workers=16,
            workdir="./",
        )

    async def start(self):
        await super().start()
        print("Bot başladı.")

    async def stop(self, *args):
        await super().stop()
        print("Bot dayandı.")

    async def recognize(self, path):
        return await shazam.recognize_song(path)

    async def related(self, track_id):
        try:
            return (await shazam.related_tracks(track_id=track_id, limit=50, start_from=2))['tracks']
        except exceptions.FailedDecodeJson:
            return None
    
    async def get_artist(self, query: str):
        artists = await shazam.search_artist(query=query, limit=50)
        hits = []
        try:
            for artist in artists['artists']['hits']:
                hits.append(FactoryArtist(artist).serializer())
            return hits
        except KeyError:
            return None
        
    async def get_artist_tracks(self, artist_id: int):
        tracks = []
        tem = (await shazam.artist_top_tracks(artist_id=artist_id, limit=50))['tracks']
        try:
            for track in tem:
                tracks.append(FactoryTrack(data=track).serializer())
            return tracks
        except KeyError:
            return None

# API ID ve API HASH bilgilerini buraya manuel olarak girin
api_id = 23782247
api_hash = "3858cc2587c4e260a2e9ef3763cbcf9f"

# Botu başlatın
bot = Bot("bot_name", api_id, api_hash)

bot.run()
