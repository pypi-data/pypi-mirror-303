from spotipyio.logic.consts.spotify_consts import TRACKS, RANGE_START, INSERT_BEFORE, SNAPSHOT_ID, RANGE_LENGTH
from spotipyio.logic.consts.typing_consts import Json
from spotipyio.logic.contract import BasePlaylistsUpdater


class PlaylistItemsReorder(BasePlaylistsUpdater):
    async def run(
        self, playlist_id: str, range_start: int, range_length: int, insert_before: int, snapshot_id: str
    ) -> Json:
        url = self._build_url(playlist_id)
        payload = {
            RANGE_START: range_start,
            INSERT_BEFORE: insert_before,
            SNAPSHOT_ID: snapshot_id,
            RANGE_LENGTH: range_length,
        }

        return await self._session.put(url=url, payload=payload)

    @property
    def _route(self) -> str:
        return TRACKS
