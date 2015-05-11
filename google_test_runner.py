import os

from shishito.salsa_runner import ShishitoRunner


class GoogleRunner(ShishitoRunner):
    """ Dedicated project runner, extends general SalsaRunner """

    def __init__(self):
        project_root = os.path.dirname(os.path.abspath(__file__))
        super(GoogleRunner, self).__init__(project_root)


runner = GoogleRunner()
runner.run_tests()
