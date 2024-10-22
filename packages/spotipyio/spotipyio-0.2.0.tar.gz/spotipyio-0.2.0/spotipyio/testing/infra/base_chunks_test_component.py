from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from pytest_httpserver import HTTPServer, RequestHandler

from spotipyio.logic.consts.spotify_consts import IDS
from spotipyio.logic.consts.typing_consts import Json
from spotipyio.logic.internal_models import ChunkSize
from spotipyio.testing.infra import BaseTestComponent
from spotipyio.logic.internal_tools import DataChunksGenerator


class BaseChunksTestComponent(BaseTestComponent, ABC):
    def __init__(
        self, server: HTTPServer, headers: Dict[str, str], chunks_generator: DataChunksGenerator = DataChunksGenerator()
    ):
        super().__init__(server=server, headers=headers)
        self._chunks_generator = chunks_generator

    def expect(self, ids: List[str]) -> List[RequestHandler]:
        return self._expect_chunks(route=self._route, ids=ids, chunk_size=self._chunk_size.value)

    def expect_failure(
        self, ids: List[str], status: Optional[int] = None, response_json: Optional[Json] = None
    ) -> None:
        status, response_json = self._create_invalid_response(status=status, response_json=response_json)
        handlers = self._expect_chunks(route=self._route, ids=ids, chunk_size=self._chunk_size.value)

        for handler in handlers:
            handler.respond_with_json(status=status, response_json=response_json)

    def expect_success(self, ids: List[str], responses_json: Optional[List[Json]] = None) -> None:
        handlers = self._expect_chunks(route=self._route, ids=ids, chunk_size=self._chunk_size.value)
        handlers_number = len(handlers)
        responses = responses_json or [self._random_valid_response() for _ in range(handlers_number)]
        responses_number = len(responses)

        if responses_number != handlers_number:
            raise ValueError(
                f"Number of provided responses ({responses_number}) didn't match number of handlers ({handlers_number})"
            )

        for handler, response_json in zip(handlers, responses):
            handler.respond_with_json(status=200, response_json=response_json)

    def _expect_chunks(self, route: str, ids: List[str], chunk_size: int) -> List[RequestHandler]:
        chunks = self._chunks_generator.generate_data_chunks(lst=ids, chunk_size=chunk_size)
        request_handlers = []

        for chunk in chunks:
            chunk_handler = self._expect_get_request(route=route, params={IDS: ",".join(chunk)})
            request_handlers.append(chunk_handler)

        return request_handlers

    @property
    @abstractmethod
    def _chunk_size(self) -> ChunkSize:
        raise NotImplementedError

    @property
    @abstractmethod
    def _route(self) -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _random_valid_response() -> Json:
        raise NotImplementedError
