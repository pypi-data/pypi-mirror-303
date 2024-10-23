# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from .states import (
    StatesResource,
    AsyncStatesResource,
    StatesResourceWithRawResponse,
    AsyncStatesResourceWithRawResponse,
    StatesResourceWithStreamingResponse,
    AsyncStatesResourceWithStreamingResponse,
)
from .leagues import (
    LeaguesResource,
    AsyncLeaguesResource,
    LeaguesResourceWithRawResponse,
    AsyncLeaguesResourceWithRawResponse,
    LeaguesResourceWithStreamingResponse,
    AsyncLeaguesResourceWithStreamingResponse,
)
from .players import (
    PlayersResource,
    AsyncPlayersResource,
    PlayersResourceWithRawResponse,
    AsyncPlayersResourceWithRawResponse,
    PlayersResourceWithStreamingResponse,
    AsyncPlayersResourceWithStreamingResponse,
)
from .seasons import (
    SeasonsResource,
    AsyncSeasonsResource,
    SeasonsResourceWithRawResponse,
    AsyncSeasonsResourceWithRawResponse,
    SeasonsResourceWithStreamingResponse,
    AsyncSeasonsResourceWithStreamingResponse,
)
from .fixtures import (
    FixturesResource,
    AsyncFixturesResource,
    FixturesResourceWithRawResponse,
    AsyncFixturesResourceWithRawResponse,
    FixturesResourceWithStreamingResponse,
    AsyncFixturesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .standings import (
    StandingsResource,
    AsyncStandingsResource,
    StandingsResourceWithRawResponse,
    AsyncStandingsResourceWithRawResponse,
    StandingsResourceWithStreamingResponse,
    AsyncStandingsResourceWithStreamingResponse,
)
from .livescores import (
    LivescoresResource,
    AsyncLivescoresResource,
    LivescoresResourceWithRawResponse,
    AsyncLivescoresResourceWithRawResponse,
    LivescoresResourceWithStreamingResponse,
    AsyncLivescoresResourceWithStreamingResponse,
)
from .topscorers import (
    TopscorersResource,
    AsyncTopscorersResource,
    TopscorersResourceWithRawResponse,
    AsyncTopscorersResourceWithRawResponse,
    TopscorersResourceWithStreamingResponse,
    AsyncTopscorersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .standings.standings import StandingsResource, AsyncStandingsResource

__all__ = ["FootballResource", "AsyncFootballResource"]


class FootballResource(SyncAPIResource):
    @cached_property
    def leagues(self) -> LeaguesResource:
        return LeaguesResource(self._client)

    @cached_property
    def fixtures(self) -> FixturesResource:
        return FixturesResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def standings(self) -> StandingsResource:
        return StandingsResource(self._client)

    @cached_property
    def players(self) -> PlayersResource:
        return PlayersResource(self._client)

    @cached_property
    def livescores(self) -> LivescoresResource:
        return LivescoresResource(self._client)

    @cached_property
    def seasons(self) -> SeasonsResource:
        return SeasonsResource(self._client)

    @cached_property
    def topscorers(self) -> TopscorersResource:
        return TopscorersResource(self._client)

    @cached_property
    def states(self) -> StatesResource:
        return StatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FootballResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FootballResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FootballResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return FootballResourceWithStreamingResponse(self)


class AsyncFootballResource(AsyncAPIResource):
    @cached_property
    def leagues(self) -> AsyncLeaguesResource:
        return AsyncLeaguesResource(self._client)

    @cached_property
    def fixtures(self) -> AsyncFixturesResource:
        return AsyncFixturesResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def standings(self) -> AsyncStandingsResource:
        return AsyncStandingsResource(self._client)

    @cached_property
    def players(self) -> AsyncPlayersResource:
        return AsyncPlayersResource(self._client)

    @cached_property
    def livescores(self) -> AsyncLivescoresResource:
        return AsyncLivescoresResource(self._client)

    @cached_property
    def seasons(self) -> AsyncSeasonsResource:
        return AsyncSeasonsResource(self._client)

    @cached_property
    def topscorers(self) -> AsyncTopscorersResource:
        return AsyncTopscorersResource(self._client)

    @cached_property
    def states(self) -> AsyncStatesResource:
        return AsyncStatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFootballResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFootballResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFootballResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncFootballResourceWithStreamingResponse(self)


class FootballResourceWithRawResponse:
    def __init__(self, football: FootballResource) -> None:
        self._football = football

    @cached_property
    def leagues(self) -> LeaguesResourceWithRawResponse:
        return LeaguesResourceWithRawResponse(self._football.leagues)

    @cached_property
    def fixtures(self) -> FixturesResourceWithRawResponse:
        return FixturesResourceWithRawResponse(self._football.fixtures)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._football.teams)

    @cached_property
    def standings(self) -> StandingsResourceWithRawResponse:
        return StandingsResourceWithRawResponse(self._football.standings)

    @cached_property
    def players(self) -> PlayersResourceWithRawResponse:
        return PlayersResourceWithRawResponse(self._football.players)

    @cached_property
    def livescores(self) -> LivescoresResourceWithRawResponse:
        return LivescoresResourceWithRawResponse(self._football.livescores)

    @cached_property
    def seasons(self) -> SeasonsResourceWithRawResponse:
        return SeasonsResourceWithRawResponse(self._football.seasons)

    @cached_property
    def topscorers(self) -> TopscorersResourceWithRawResponse:
        return TopscorersResourceWithRawResponse(self._football.topscorers)

    @cached_property
    def states(self) -> StatesResourceWithRawResponse:
        return StatesResourceWithRawResponse(self._football.states)


class AsyncFootballResourceWithRawResponse:
    def __init__(self, football: AsyncFootballResource) -> None:
        self._football = football

    @cached_property
    def leagues(self) -> AsyncLeaguesResourceWithRawResponse:
        return AsyncLeaguesResourceWithRawResponse(self._football.leagues)

    @cached_property
    def fixtures(self) -> AsyncFixturesResourceWithRawResponse:
        return AsyncFixturesResourceWithRawResponse(self._football.fixtures)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._football.teams)

    @cached_property
    def standings(self) -> AsyncStandingsResourceWithRawResponse:
        return AsyncStandingsResourceWithRawResponse(self._football.standings)

    @cached_property
    def players(self) -> AsyncPlayersResourceWithRawResponse:
        return AsyncPlayersResourceWithRawResponse(self._football.players)

    @cached_property
    def livescores(self) -> AsyncLivescoresResourceWithRawResponse:
        return AsyncLivescoresResourceWithRawResponse(self._football.livescores)

    @cached_property
    def seasons(self) -> AsyncSeasonsResourceWithRawResponse:
        return AsyncSeasonsResourceWithRawResponse(self._football.seasons)

    @cached_property
    def topscorers(self) -> AsyncTopscorersResourceWithRawResponse:
        return AsyncTopscorersResourceWithRawResponse(self._football.topscorers)

    @cached_property
    def states(self) -> AsyncStatesResourceWithRawResponse:
        return AsyncStatesResourceWithRawResponse(self._football.states)


class FootballResourceWithStreamingResponse:
    def __init__(self, football: FootballResource) -> None:
        self._football = football

    @cached_property
    def leagues(self) -> LeaguesResourceWithStreamingResponse:
        return LeaguesResourceWithStreamingResponse(self._football.leagues)

    @cached_property
    def fixtures(self) -> FixturesResourceWithStreamingResponse:
        return FixturesResourceWithStreamingResponse(self._football.fixtures)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._football.teams)

    @cached_property
    def standings(self) -> StandingsResourceWithStreamingResponse:
        return StandingsResourceWithStreamingResponse(self._football.standings)

    @cached_property
    def players(self) -> PlayersResourceWithStreamingResponse:
        return PlayersResourceWithStreamingResponse(self._football.players)

    @cached_property
    def livescores(self) -> LivescoresResourceWithStreamingResponse:
        return LivescoresResourceWithStreamingResponse(self._football.livescores)

    @cached_property
    def seasons(self) -> SeasonsResourceWithStreamingResponse:
        return SeasonsResourceWithStreamingResponse(self._football.seasons)

    @cached_property
    def topscorers(self) -> TopscorersResourceWithStreamingResponse:
        return TopscorersResourceWithStreamingResponse(self._football.topscorers)

    @cached_property
    def states(self) -> StatesResourceWithStreamingResponse:
        return StatesResourceWithStreamingResponse(self._football.states)


class AsyncFootballResourceWithStreamingResponse:
    def __init__(self, football: AsyncFootballResource) -> None:
        self._football = football

    @cached_property
    def leagues(self) -> AsyncLeaguesResourceWithStreamingResponse:
        return AsyncLeaguesResourceWithStreamingResponse(self._football.leagues)

    @cached_property
    def fixtures(self) -> AsyncFixturesResourceWithStreamingResponse:
        return AsyncFixturesResourceWithStreamingResponse(self._football.fixtures)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._football.teams)

    @cached_property
    def standings(self) -> AsyncStandingsResourceWithStreamingResponse:
        return AsyncStandingsResourceWithStreamingResponse(self._football.standings)

    @cached_property
    def players(self) -> AsyncPlayersResourceWithStreamingResponse:
        return AsyncPlayersResourceWithStreamingResponse(self._football.players)

    @cached_property
    def livescores(self) -> AsyncLivescoresResourceWithStreamingResponse:
        return AsyncLivescoresResourceWithStreamingResponse(self._football.livescores)

    @cached_property
    def seasons(self) -> AsyncSeasonsResourceWithStreamingResponse:
        return AsyncSeasonsResourceWithStreamingResponse(self._football.seasons)

    @cached_property
    def topscorers(self) -> AsyncTopscorersResourceWithStreamingResponse:
        return AsyncTopscorersResourceWithStreamingResponse(self._football.topscorers)

    @cached_property
    def states(self) -> AsyncStatesResourceWithStreamingResponse:
        return AsyncStatesResourceWithStreamingResponse(self._football.states)
