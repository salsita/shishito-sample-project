import os

from shishito.salsa_runner import ShishitoRunner

# from shishito.library.support.jira_zephyr_api import ZAPI


class GoogleRunner(ShishitoRunner):
    """ Dedicated project runner, extends general SalsaRunner """
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        ShishitoRunner.__init__(self)

runner = GoogleRunner()