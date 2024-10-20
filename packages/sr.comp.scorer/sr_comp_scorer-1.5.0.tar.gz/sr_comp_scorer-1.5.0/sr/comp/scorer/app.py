from __future__ import annotations

import collections
import contextlib
import io
import itertools
import os
from datetime import datetime

import dateutil.tz
import flask
import jinja2

from sr.comp.raw_compstate import RawCompstate
from sr.comp.scorer.converter import load_converter
from sr.comp.validation import validate

app = flask.Flask('sr.comp.scorer')
app.debug = True


class CompstateTemplateLoader:
    def __init__(self, app: flask.Flask) -> None:
        self.app = app
        self._loader: jinja2.BaseLoader | None = None

    @property
    def loader(self) -> jinja2.BaseLoader:
        if self._loader is None:
            self._loader = jinja2.FileSystemLoader(os.path.join(
                os.path.realpath(app.config['COMPSTATE']),
                'scoring',
            ))
        return self._loader

    def get_source(self, environment, template):
        return self.loader.get_source(environment, template)

    def list_templates(self):
        return self.loader.list_templates()


app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    CompstateTemplateLoader(app),
])


@app.template_global()
def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks.

    >>> grouper('ABCDEFG', 3, 'x')
    ['ABC', 'DEF', 'Gxx']
    """
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


@app.template_filter()
def empty_if_none(string):
    return string if string is not None else ''


@app.template_global()
def parse_hex_colour(string):
    string = string.strip('#')
    return int(string[:2], 16), int(string[2:4], 16), int(string[4:], 16)


def group_list_dict(matches, keys):
    """
    Group a list of dictionaries into a dictionary of lists.

    This will convert
        [{'A': a, 'B': b}, {'A': a2, 'B': b2}]
    into
        {'A': [a, a2], 'B': [b, b2]}
    """
    target = collections.OrderedDict((key, []) for key in keys)
    for entry in matches:
        if entry is None:
            continue
        for key, value in entry.items():
            target[key].append(value)
    return target


@app.template_global()
def is_match_done(match):
    path = flask.g.compstate.get_score_path(match)
    return os.path.exists(path)


def update_and_validate(compstate, match, score, force):
    compstate.save_score(match, score)

    path = compstate.get_score_path(match)
    compstate.stage(path)

    try:
        comp = compstate.load()
    except Exception as e:
        # SRComp sometimes throws generic Exceptions. We have to reset the repo
        # because if SRComp fails to instantiate, it would break everything!
        compstate.reset_hard()
        raise RuntimeError(e)
    else:
        if not force:
            # TODO Update SRComp to return the error messages.
            with contextlib.redirect_stderr(io.StringIO()) as new_stderr:
                num_errors = validate(comp)

            if num_errors:
                raise RuntimeError(new_stderr.getvalue())


def commit_and_push(compstate, match):
    commit_msg = "Update {} scores for match {} in arena {}".format(
        match.type.value,
        match.num,
        match.arena,
    )

    compstate.commit_and_push(commit_msg, allow_empty=True)


@app.before_request
def before_request():
    cs_path = os.path.realpath(app.config['COMPSTATE'])
    local_only = app.config['COMPSTATE_LOCAL']
    flask.g.compstate = RawCompstate(cs_path, local_only)

    try:
        correct_username = app.config['AUTH_USERNAME']
        correct_password = app.config['AUTH_PASSWORD']
    except KeyError:
        return  # no authentication configured

    auth = flask.request.authorization
    if (
        auth is None or
        correct_username != auth.username or
        correct_password != auth.password
    ):
        return flask.Response('Authentication failed.', 401, {
            'WWW-Authenticate': 'Basic realm="Authentication required."',
        })


@app.route('/')
def index():
    comp = flask.g.compstate.load()
    all_matches = group_list_dict(comp.schedule.matches, comp.arenas.keys())
    now = datetime.now(dateutil.tz.tzlocal())
    current_matches = {
        match.arena: match
        for match in comp.schedule.matches_at(now)
    }
    return flask.render_template(
        'index.html',
        all_matches=all_matches,
        current_matches=current_matches,
        arenas=comp.arenas.values(),
    )


@app.route('/<arena>/<int:num>', methods=['GET', 'POST'])
def update(arena, num):
    compstate = flask.g.compstate
    comp = compstate.load()

    converter = load_converter(comp.root)()

    try:
        match = comp.schedule.matches[num][arena]
    except (IndexError, KeyError):
        flask.abort(404)

    template_settings = {
        'match': match,
        'arenas': comp.arenas,
        'corners': comp.corners,
        'teams': comp.teams,
    }

    if flask.request.method == 'GET':
        try:
            score = compstate.load_score(match)
        except OSError:
            flask.request.form = converter.match_to_form(match)
        else:
            flask.request.form = converter.score_to_form(score)
    elif flask.request.method == 'POST':
        try:
            score = converter.form_to_score(match, flask.request.form)
        except ValueError as e:
            return flask.render_template(
                'update.html',
                error=str(e),
                **template_settings,
            )

        try:
            force = bool(flask.request.form.get('force'))
            compstate.reset_and_fast_forward()
            update_and_validate(compstate, match, score, force)
            commit_and_push(compstate, match)
        except RuntimeError as e:
            return flask.render_template(
                'update.html',
                error=str(e) or repr(e),
                **template_settings,
            )
        else:
            url = flask.url_for('update', arena=arena, num=num) + '?done'
            return flask.redirect(url)

    return flask.render_template(
        'update.html',
        done='done' in flask.request.args,
        **template_settings,
    )


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
