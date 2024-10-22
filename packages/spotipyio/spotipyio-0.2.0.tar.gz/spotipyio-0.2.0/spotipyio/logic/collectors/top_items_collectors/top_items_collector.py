from spotipyio.logic.consts.spotify_consts import TIME_RANGE, LIMIT
from spotipyio.logic.contract import ISpotifyComponent
from spotipyio.logic.collectors.top_items_collectors.items_type import ItemsType
from spotipyio.logic.collectors.top_items_collectors.time_range import TimeRange


class TopItemsCollector(ISpotifyComponent):
    async def run(self, items_type: ItemsType, time_range: TimeRange, limit: int = 50) -> dict:
        url = self._url_format.format(items_type=items_type.value)
        params = {TIME_RANGE: time_range.value, LIMIT: limit}
        return await self._session.get(url=url, params=params)

    @property
    def _url_format(self) -> str:
        return f"{self._base_url}/me/top/{{items_type}}"
