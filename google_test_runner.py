import os

from salsa_webqa.salsa_runner import SalsaRunner


class GoogleRunner(SalsaRunner):
    """ Dedicated project runner, extends general SalsaRunner """
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        SalsaRunner.__init__(self, self.project_root)

runner = GoogleRunner()
runner.run_tests()

# # Simpler case, possible if nothing needs to be overridden:
#
# project_root = os.path.dirname(os.path.abspath(__file__))

# runner = SalsaRunner(project_root)
# runner.run_tests()