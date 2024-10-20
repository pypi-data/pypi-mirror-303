from __future__ import annotations

import copy
import runpy
import sys
from pathlib import Path
from typing import cast, NewType, Type, Union

from sr.comp.match_period import Match
from sr.comp.types import ScoreArenaZonesData, ScoreData, ScoreTeamData, TLA

ZoneId = int
Zone = Union[int, str]
InputForm = NewType('InputForm', dict[str, str])
OutputForm = NewType('OutputForm', dict[str, Union[str, bool, int, None]])


def render_int(value: int | None) -> int | None:
    """
    Process a maybe missing integer value towards a canonical display form.
    """
    if not value:
        # Display zeros as empty inputs
        return None
    return value


def parse_int(value: str | None) -> int:
    """
    Parse a maybe missing integer value towards an integer.
    """
    if value is None or value == '':
        return 0
    return int(value)


class Converter:
    """
    Base class for converting between representations of a match's score.
    """

    def form_team_to_score(self, form: InputForm, zone_id: ZoneId) -> ScoreTeamData:
        """
        Prepare a team's scoring data for saving in a score dict.

        This is given a zone as form data is all keyed by zone.
        """
        return {
            'zone': zone_id,
            'disqualified':
                form.get(f'disqualified_{zone_id}', None) is not None,
            'present':
                form.get(f'present_{zone_id}', None) is not None,
        }

    def form_zone_to_score(self, form: InputForm, zone: Zone) -> ScoreArenaZonesData:
        """
        Prepare a zone's scoring data for saving in a score dict.

        This is data which relates to the state of the zone itself.
        """
        return ScoreArenaZonesData({
            'tokens': form.get(f'tokens_{zone}', ''),
        })

    def form_to_score(self, match: Match, form: InputForm) -> ScoreData:
        """
        Prepare a score dict for the given match and form dict.

        This method is used to convert the submitted information for storage as
        YAML in the compstate.
        """
        zone_ids = range(len(match.teams))

        teams = {}
        for zone_id in zone_ids:
            tla = form.get(f'tla_{zone_id}', None)
            if tla:
                teams[TLA(tla)] = self.form_team_to_score(form, zone_id)

        zones = list(zone_ids) + ['other']
        arena = ScoreArenaZonesData({
            zone: self.form_zone_to_score(form, zone)
            for zone in zones
        })

        return ScoreData({
            'arena_id': match.arena,
            'match_number': match.num,
            'teams': teams,
            'arena_zones': arena,
        })

    def score_team_to_form(self, tla: TLA, info: ScoreTeamData) -> OutputForm:
        zone_id = info['zone']
        return OutputForm({
            f'tla_{zone_id}': tla,
            f'disqualified_{zone_id}': info.get('disqualified', False),
            f'present_{zone_id}': info.get('present', True),
        })

    def score_zone_to_form(self, zone: int | str, zone_info: ScoreArenaZonesData) -> OutputForm:
        # TODO: use generics to avoid this cast?
        info = cast(dict[str, str], zone_info)
        return OutputForm({
            f'tokens_{zone}': info['tokens'].upper(),
        })

    def score_to_form(self, score: ScoreData) -> OutputForm:
        """
        Prepare a form dict for the given score dict.

        This method is used when there is an existing score for a match.
        """
        form = OutputForm({})

        for tla, team_info in score['teams'].items():
            form.update(self.score_team_to_form(tla, team_info))

        # arena_zones isn't usefully typed; see https://github.com/PeterJCLaw/srcomp/issues/28
        for zone, zone_info in score.get('arena_zones', {}).items():  # type: ignore[union-attr]
            form.update(self.score_zone_to_form(zone, zone_info))

        return form

    def match_to_form(self, match: Match) -> OutputForm:
        """
        Prepare a fresh form dict for the given match.

        This method is used when there is no existing score for a match.
        """

        form = OutputForm({})

        for zone_id, tla in enumerate(match.teams):
            if tla:
                form[f'tla_{zone_id}'] = tla
                form[f'disqualified_{zone_id}'] = False
                form[f'present_{zone_id}'] = False

            form[f'tokens_{zone_id}'] = ''

        form['tokens_other'] = ''

        return form


def load_converter(root: Path) -> type[Converter]:
    """
    Load the score converter module from Compstate repo.

    :param Path root: The path to the compstate repo.
    """

    # Deep path hacks
    score_directory = root / 'scoring'
    converter_source = score_directory / 'converter.py'

    saved_path = copy.copy(sys.path)
    sys.path.insert(0, str(score_directory))

    try:
        converter = runpy.run_path(str(converter_source))
    finally:
        sys.path = saved_path

    return cast(Type[Converter], converter['Converter'])
