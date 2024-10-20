import os.path
import unittest

from flask.testing import FlaskClient

from sr.comp.scorer import app

COMPSTATE = os.path.join(os.path.dirname(__file__), 'dummy')
app.config['COMPSTATE'] = COMPSTATE
app.config['COMPSTATE_LOCAL'] = True


class ViewSmokeTests(unittest.TestCase):
    def assertServerGet(self, endpoint: str, *, status_code: int = 200) -> None:
        response = self.client.get(endpoint)
        code = int(response.status.split(' ')[0])
        self.assertEqual(status_code, code)

    def setUp(self) -> None:
        super().setUp()
        self.client = FlaskClient(app)

    def test_index(self) -> None:
        self.assertServerGet('/')

    def test_update(self) -> None:
        self.assertServerGet('/A/0')
