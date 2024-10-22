from typing import Optional

from spotipyio.logic.consts.spotify_consts import NAME, ARTISTS
from spotipyio.tools.extractors.entity_extractor_interface import IEntityExtractor


class PrimaryArtistEntityExtractor(IEntityExtractor):
    def extract(self, entity: dict) -> Optional[str]:
        items = entity.get(ARTISTS)

        if items:
            primary_artist = items[0]
            return primary_artist.get(NAME)

    @property
    def name(self) -> str:
        return "artist"
