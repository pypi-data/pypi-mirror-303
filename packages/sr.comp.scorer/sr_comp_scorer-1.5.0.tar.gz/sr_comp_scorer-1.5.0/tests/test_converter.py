from __future__ import annotations

import datetime
import unittest
from typing import Sequence, Union

from sr.comp.match_period import Match, MatchType
from sr.comp.scorer.converter import Converter
from sr.comp.types import ArenaName, MatchNumber, TLA

UTC = datetime.timezone.utc


# Copied from srcomp's factories.
def build_match(
    num: int = 0,
    arena: str = 'main',
    teams: Sequence[TLA | None] = (),
    start_time: datetime.datetime = datetime.datetime(2020, 1, 25, 11, 0, tzinfo=UTC),
    end_time: datetime.datetime = datetime.datetime(2020, 1, 25, 11, 5, tzinfo=UTC),
    type_: MatchType = MatchType.league,
    use_resolved_ranking: bool = False,
) -> Match:
    return Match(
        MatchNumber(num),
        f"Match {num}",
        ArenaName(arena),
        list(teams),
        start_time,
        end_time,
        type_,
        use_resolved_ranking,
    )


def htmlify(form: dict[str, Union[str, int, bool, None]]) -> dict[str, str]:
    # Approximation of what happens to a form which round trips.
    # Definitely not canonical!

    return {
        k: str(v)
        for k, v in form.items()
        if v not in (False, None)
    }


class ConverterSmokeTests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.match = build_match(teams=[
            TLA('ABC'),
            TLA('DEF'),
            TLA('GHI'),
            TLA('JKL'),
        ])

    def test_round_trip(self) -> None:
        converter = Converter()
        initial_form = converter.match_to_form(self.match)

        score = converter.form_to_score(
            self.match,
            htmlify(initial_form),
        )

        reloaded_form = converter.score_to_form(score)

        self.assertEqual(initial_form, reloaded_form)
