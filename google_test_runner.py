import os

from salsa_webqa.salsa_runner import SalsaRunner
from salsa_webqa.library.support.jira_zephyr_api import ZAPI
from datetime import datetime


class GoogleRunner(SalsaRunner):
    """ Dedicated project runner, extends general SalsaRunner """
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        SalsaRunner.__init__(self, self.project_root)

runner = GoogleRunner()
zapi = ZAPI()
auth=(os.environ.get("jira_username"), os.environ.get("jira_password"))
CYCLE_ID = zapi.create_new_test_cycle("Simple test cycle "+datetime.today().strftime("%d-%m-%y"), "Metros Testing", "First release", auth)
runner.run_tests()

# # Simpler case, possible if nothing needs to be overridden:
#
# project_root = os.path.dirname(os.path.abspath(__file__))

# runner = SalsaRunner(project_root)
# runner.run_tests()