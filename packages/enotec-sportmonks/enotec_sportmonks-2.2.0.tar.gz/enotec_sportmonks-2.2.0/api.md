# Shared Types

```python
from sportmonks.types import Pagination, RateLimit, Subscription, Timezone
```

# Core

## Continents

Types:

```python
from sportmonks.types.core import ContinentRetrieveResponse, ContinentListResponse
```

Methods:

- <code title="get /{version}/core/continents/{continentId}">client.core.continents.<a href="./src/sportmonks/resources/core/continents.py">retrieve</a>(continent_id, \*, version) -> <a href="./src/sportmonks/types/core/continent_retrieve_response.py">ContinentRetrieveResponse</a></code>
- <code title="get /{version}/core/continents">client.core.continents.<a href="./src/sportmonks/resources/core/continents.py">list</a>(version, \*\*<a href="src/sportmonks/types/core/continent_list_params.py">params</a>) -> <a href="./src/sportmonks/types/core/continent_list_response.py">SyncPaginatedAPICall[ContinentListResponse]</a></code>

## Countries

Types:

```python
from sportmonks.types.core import (
    CountryRetrieveResponse,
    CountryListResponse,
    CountrySearchResponse,
)
```

Methods:

- <code title="get /{version}/core/countries/{countryId}">client.core.countries.<a href="./src/sportmonks/resources/core/countries.py">retrieve</a>(country_id, \*, version) -> <a href="./src/sportmonks/types/core/country_retrieve_response.py">CountryRetrieveResponse</a></code>
- <code title="get /{version}/core/countries">client.core.countries.<a href="./src/sportmonks/resources/core/countries.py">list</a>(version, \*\*<a href="src/sportmonks/types/core/country_list_params.py">params</a>) -> <a href="./src/sportmonks/types/core/country_list_response.py">SyncPaginatedAPICall[CountryListResponse]</a></code>
- <code title="get /{version}/core/countries/search/{name}">client.core.countries.<a href="./src/sportmonks/resources/core/countries.py">search</a>(name, \*, version) -> <a href="./src/sportmonks/types/core/country_search_response.py">CountrySearchResponse</a></code>

## Regions

Types:

```python
from sportmonks.types.core import RegionRetrieveResponse, RegionListResponse, RegionSearchResponse
```

Methods:

- <code title="get /{version}/core/regions/{regionId}">client.core.regions.<a href="./src/sportmonks/resources/core/regions.py">retrieve</a>(region_id, \*, version) -> <a href="./src/sportmonks/types/core/region_retrieve_response.py">RegionRetrieveResponse</a></code>
- <code title="get /{version}/core/regions">client.core.regions.<a href="./src/sportmonks/resources/core/regions.py">list</a>(version, \*\*<a href="src/sportmonks/types/core/region_list_params.py">params</a>) -> <a href="./src/sportmonks/types/core/region_list_response.py">SyncPaginatedAPICall[RegionListResponse]</a></code>
- <code title="get /{version}/core/regions/search/{name}">client.core.regions.<a href="./src/sportmonks/resources/core/regions.py">search</a>(name, \*, version) -> <a href="./src/sportmonks/types/core/region_search_response.py">RegionSearchResponse</a></code>

## Types

Types:

```python
from sportmonks.types.core import TypeRetrieveResponse, TypeListResponse
```

Methods:

- <code title="get /{version}/core/types/{typeId}">client.core.types.<a href="./src/sportmonks/resources/core/types.py">retrieve</a>(type_id, \*, version) -> <a href="./src/sportmonks/types/core/type_retrieve_response.py">TypeRetrieveResponse</a></code>
- <code title="get /{version}/core/types">client.core.types.<a href="./src/sportmonks/resources/core/types.py">list</a>(version, \*\*<a href="src/sportmonks/types/core/type_list_params.py">params</a>) -> <a href="./src/sportmonks/types/core/type_list_response.py">SyncPaginatedAPICall[TypeListResponse]</a></code>

## Timezones

Types:

```python
from sportmonks.types.core import TimezoneListResponse
```

Methods:

- <code title="get /{version}/core/timezones">client.core.timezones.<a href="./src/sportmonks/resources/core/timezones.py">list</a>(version, \*\*<a href="src/sportmonks/types/core/timezone_list_params.py">params</a>) -> <a href="./src/sportmonks/types/core/timezone_list_response.py">SyncPaginatedAPICall[TimezoneListResponse]</a></code>

# Football

## Leagues

Types:

```python
from sportmonks.types.football import (
    League,
    LeagueRetrieveResponse,
    LeagueLiveResponse,
    LeagueSearchResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/leagues/{leagueId}">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">retrieve</a>(league_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/league_retrieve_response.py">LeagueRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/leagues">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/league_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/league.py">SyncPaginatedAPICall[League]</a></code>
- <code title="get /{version}/{sport}/leagues/countries/{countryId}">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">list_by_country</a>(country_id, \*, version, sport, \*\*<a href="src/sportmonks/types/football/league_list_by_country_params.py">params</a>) -> <a href="./src/sportmonks/types/football/league.py">SyncPaginatedAPICall[League]</a></code>
- <code title="get /{version}/{sport}/leagues/date/{date}">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">list_by_date</a>(date, \*, version, sport, \*\*<a href="src/sportmonks/types/football/league_list_by_date_params.py">params</a>) -> <a href="./src/sportmonks/types/football/league.py">SyncPaginatedAPICall[League]</a></code>
- <code title="get /{version}/{sport}/leagues/live">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">live</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/league_live_response.py">LeagueLiveResponse</a></code>
- <code title="get /{version}/{sport}/leagues/search/{name}">client.football.leagues.<a href="./src/sportmonks/resources/football/leagues.py">search</a>(name, \*, version, sport) -> <a href="./src/sportmonks/types/football/league_search_response.py">LeagueSearchResponse</a></code>

## Fixtures

Types:

```python
from sportmonks.types.football import (
    Fixture,
    FixtureRetrieveResponse,
    FixtureHeadToHeadResponse,
    FixtureLatestResponse,
    FixtureListByIDsResponse,
    FixtureSearchResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/fixtures/{fixtureId}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">retrieve</a>(fixture_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/fixture_retrieve_response.py">FixtureRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/fixtures">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/fixture_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/fixture.py">SyncPaginatedAPICall[Fixture]</a></code>
- <code title="get /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">head_to_head</a>(second_team, \*, version, sport, first_team, \*\*<a href="src/sportmonks/types/football/fixture_head_to_head_params.py">params</a>) -> <a href="./src/sportmonks/types/football/fixture_head_to_head_response.py">FixtureHeadToHeadResponse</a></code>
- <code title="get /{version}/{sport}/fixtures/latest">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">latest</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/fixture_latest_response.py">FixtureLatestResponse</a></code>
- <code title="get /{version}/{sport}/fixtures/between/{startDate}/{endDate}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">list_between_dates</a>(end_date, \*, version, sport, start_date, \*\*<a href="src/sportmonks/types/football/fixture_list_between_dates_params.py">params</a>) -> <a href="./src/sportmonks/types/football/fixture.py">SyncPaginatedAPICall[Fixture]</a></code>
- <code title="get /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">list_between_dates_for_team</a>(team_id, \*, version, sport, start_date, end_date, \*\*<a href="src/sportmonks/types/football/fixture_list_between_dates_for_team_params.py">params</a>) -> <a href="./src/sportmonks/types/football/fixture.py">SyncPaginatedAPICall[Fixture]</a></code>
- <code title="get /{version}/{sport}/fixtures/date/{date}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">list_by_date</a>(date, \*, version, sport, \*\*<a href="src/sportmonks/types/football/fixture_list_by_date_params.py">params</a>) -> <a href="./src/sportmonks/types/football/fixture.py">SyncPaginatedAPICall[Fixture]</a></code>
- <code title="get /{version}/{sport}/fixtures/multi/{fixtureIds}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">list_by_ids</a>(fixture_ids, \*, version, sport) -> <a href="./src/sportmonks/types/football/fixture_list_by_ids_response.py">FixtureListByIDsResponse</a></code>
- <code title="get /{version}/{sport}/fixtures/search/{name}">client.football.fixtures.<a href="./src/sportmonks/resources/football/fixtures.py">search</a>(name, \*, version, sport) -> <a href="./src/sportmonks/types/football/fixture_search_response.py">FixtureSearchResponse</a></code>

## Teams

Types:

```python
from sportmonks.types.football import (
    Team,
    TeamRetrieveResponse,
    TeamListBySeasonResponse,
    TeamSearchResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/teams/{teamId}">client.football.teams.<a href="./src/sportmonks/resources/football/teams.py">retrieve</a>(team_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/team_retrieve_response.py">TeamRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/teams">client.football.teams.<a href="./src/sportmonks/resources/football/teams.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/team_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/team.py">SyncPaginatedAPICall[Team]</a></code>
- <code title="get /{version}/{sport}/teams/countries/{countryId}">client.football.teams.<a href="./src/sportmonks/resources/football/teams.py">list_by_country</a>(country_id, \*, version, sport, \*\*<a href="src/sportmonks/types/football/team_list_by_country_params.py">params</a>) -> <a href="./src/sportmonks/types/football/team.py">SyncPaginatedAPICall[Team]</a></code>
- <code title="get /{version}/{sport}/teams/seasons/{seasonId}">client.football.teams.<a href="./src/sportmonks/resources/football/teams.py">list_by_season</a>(season_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/team_list_by_season_response.py">TeamListBySeasonResponse</a></code>
- <code title="get /{version}/{sport}/teams/search/{name}">client.football.teams.<a href="./src/sportmonks/resources/football/teams.py">search</a>(name, \*, version, sport) -> <a href="./src/sportmonks/types/football/team_search_response.py">TeamSearchResponse</a></code>

## Standings

Types:

```python
from sportmonks.types.football import StandingListResponse, StandingListBySeasonResponse
```

Methods:

- <code title="get /{version}/{sport}/standings">client.football.standings.<a href="./src/sportmonks/resources/football/standings/standings.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/standing_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/standing_list_response.py">SyncPaginatedAPICall[StandingListResponse]</a></code>
- <code title="get /{version}/{sport}/standings/seasons/{seasonId}">client.football.standings.<a href="./src/sportmonks/resources/football/standings/standings.py">list_by_season</a>(season_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/standing_list_by_season_response.py">StandingListBySeasonResponse</a></code>

### Corrections

Types:

```python
from sportmonks.types.football.standings import CorrectionListBySeasonResponse
```

Methods:

- <code title="get /{version}/{sport}/standings/corrections/seasons/{seasonId}">client.football.standings.corrections.<a href="./src/sportmonks/resources/football/standings/corrections.py">list_by_season</a>(season_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/standings/correction_list_by_season_response.py">CorrectionListBySeasonResponse</a></code>

### Live

Types:

```python
from sportmonks.types.football.standings import LiveListByLeagueResponse
```

Methods:

- <code title="get /{version}/{sport}/standings/live/leagues/{leagueId}">client.football.standings.live.<a href="./src/sportmonks/resources/football/standings/live.py">list_by_league</a>(league_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/standings/live_list_by_league_response.py">LiveListByLeagueResponse</a></code>

## Players

Types:

```python
from sportmonks.types.football import (
    Player,
    PlayerRetrieveResponse,
    PlayerLatestResponse,
    PlayerSearchResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/players/{playerId}">client.football.players.<a href="./src/sportmonks/resources/football/players.py">retrieve</a>(player_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/player_retrieve_response.py">PlayerRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/players">client.football.players.<a href="./src/sportmonks/resources/football/players.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/player_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/player.py">SyncPaginatedAPICall[Player]</a></code>
- <code title="get /{version}/{sport}/players/latest">client.football.players.<a href="./src/sportmonks/resources/football/players.py">latest</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/player_latest_response.py">PlayerLatestResponse</a></code>
- <code title="get /{version}/{sport}/players/countries/{countryId}">client.football.players.<a href="./src/sportmonks/resources/football/players.py">list_by_country</a>(country_id, \*, version, sport, \*\*<a href="src/sportmonks/types/football/player_list_by_country_params.py">params</a>) -> <a href="./src/sportmonks/types/football/player.py">SyncPaginatedAPICall[Player]</a></code>
- <code title="get /{version}/{sport}/players/search/{name}">client.football.players.<a href="./src/sportmonks/resources/football/players.py">search</a>(name, \*, version, sport) -> <a href="./src/sportmonks/types/football/player_search_response.py">PlayerSearchResponse</a></code>

## Livescores

Types:

```python
from sportmonks.types.football import (
    Livescore,
    LivescoreListResponse,
    LivescoreInplayResponse,
    LivescoreLatestResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/livescores">client.football.livescores.<a href="./src/sportmonks/resources/football/livescores.py">list</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/livescore_list_response.py">LivescoreListResponse</a></code>
- <code title="get /{version}/{sport}/livescores/inplay">client.football.livescores.<a href="./src/sportmonks/resources/football/livescores.py">inplay</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/livescore_inplay_response.py">LivescoreInplayResponse</a></code>
- <code title="get /{version}/{sport}/livescores/latest">client.football.livescores.<a href="./src/sportmonks/resources/football/livescores.py">latest</a>(sport, \*, version) -> <a href="./src/sportmonks/types/football/livescore_latest_response.py">LivescoreLatestResponse</a></code>

## Seasons

Types:

```python
from sportmonks.types.football import (
    Season,
    SeasonRetrieveResponse,
    SeasonListByTeamResponse,
    SeasonSearchResponse,
)
```

Methods:

- <code title="get /{version}/{sport}/seasons/{seasonId}">client.football.seasons.<a href="./src/sportmonks/resources/football/seasons.py">retrieve</a>(season_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/season_retrieve_response.py">SeasonRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/seasons">client.football.seasons.<a href="./src/sportmonks/resources/football/seasons.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/season_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/season.py">SyncPaginatedAPICall[Season]</a></code>
- <code title="get /{version}/{sport}/seasons/teams/{teamId}">client.football.seasons.<a href="./src/sportmonks/resources/football/seasons.py">list_by_team</a>(team_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/season_list_by_team_response.py">SeasonListByTeamResponse</a></code>
- <code title="get /{version}/{sport}/seasons/search/{name}">client.football.seasons.<a href="./src/sportmonks/resources/football/seasons.py">search</a>(name, \*, version, sport) -> <a href="./src/sportmonks/types/football/season_search_response.py">SeasonSearchResponse</a></code>

## Topscorers

Types:

```python
from sportmonks.types.football import TopscorerListBySeasonResponse
```

Methods:

- <code title="get /{version}/{sport}/topscorers/seasons/{seasonId}">client.football.topscorers.<a href="./src/sportmonks/resources/football/topscorers.py">list_by_season</a>(season_id, \*, version, sport, \*\*<a href="src/sportmonks/types/football/topscorer_list_by_season_params.py">params</a>) -> <a href="./src/sportmonks/types/football/topscorer_list_by_season_response.py">SyncPaginatedAPICall[TopscorerListBySeasonResponse]</a></code>

## States

Types:

```python
from sportmonks.types.football import StateRetrieveResponse, StateListResponse
```

Methods:

- <code title="get /{version}/{sport}/states/{stateId}">client.football.states.<a href="./src/sportmonks/resources/football/states.py">retrieve</a>(state_id, \*, version, sport) -> <a href="./src/sportmonks/types/football/state_retrieve_response.py">StateRetrieveResponse</a></code>
- <code title="get /{version}/{sport}/states">client.football.states.<a href="./src/sportmonks/resources/football/states.py">list</a>(sport, \*, version, \*\*<a href="src/sportmonks/types/football/state_list_params.py">params</a>) -> <a href="./src/sportmonks/types/football/state_list_response.py">SyncPaginatedAPICall[StateListResponse]</a></code>
