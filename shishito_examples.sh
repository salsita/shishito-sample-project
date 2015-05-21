#!/bin/sh
# -----------------
#    VARIABLES
# -----------------

# Define Shishito & Sample Project paths
shishito_test_project=~/shishito-sample-project
shishito_framework=~/shishito

# Define BrowserStack credentials
browserstack_user=
browserstack_pass=

saucelabs_user=
saucelabs_pass=

# Shishito to PYTHONPATH
export PYTHONPATH=${PYTHONPATH}:/${shishito_framework}

# -----------------
#      TESTS
# -----------------

# DESKTOP COMBINATIONS - local browser
python ${shishito_test_project}/google_test_runner.py --platform web --environment local
python ${shishito_test_project}/google_test_runner.py --platform web --environment local --smoke

# DESKTOP COMBINATIONS - browserstack
python ${shishito_test_project}/google_test_runner.py --platform web --environment browserstack --browserstack ${browserstack_user}:${browserstack_pass}
python ${shishito_test_project}/google_test_runner.py --platform web --environment browserstack --browserstack ${browserstack_user}:${browserstack_pass} --smoke

# MOBILE APPS - local appium server
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --smoke

# MOBILE APPS - using saucelabs
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --saucelabs ${saucelabs_user}:${saucelabs_pass}
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --saucelabs ${saucelabs_user}:${saucelabs_pass} --smoke
