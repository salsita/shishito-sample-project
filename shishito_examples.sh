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

# DEKSTOP COMBINATIONS - non selenium tests
python ${shishito_test_project}/google_test_runner.py --platform generic --environment local --test_directory non_selenium_tests
python ${shishito_test_project}/google_test_runner.py --platform generic --environment local --test_directory non_selenium_tests --smoke

# DESKTOP COMBINATIONS - local browser
python ${shishito_test_project}/google_test_runner.py --platform web --environment local --test_directory tests
python ${shishito_test_project}/google_test_runner.py --platform web --environment local --test_directory tests --smoke

# DESKTOP COMBINATIONS - browserstack
python ${shishito_test_project}/google_test_runner.py --platform web --environment browserstack --browserstack ${browserstack_user}:${browserstack_pass} --test_directory tests
python ${shishito_test_project}/google_test_runner.py --platform web --environment browserstack --browserstack ${browserstack_user}:${browserstack_pass} --test_directory tests --smoke

# MOBILE APPS - local appium server
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --test_directory appium_tests
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --test_directory appium_tests --smoke

# MOBILE APPS - using saucelabs
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --saucelabs ${saucelabs_user}:${saucelabs_pass} --test_directory appium_tests
python ${shishito_test_project}/google_test_runner.py --platform mobile --environment appium --saucelabs ${saucelabs_user}:${saucelabs_pass} --test_directory appium_tests --smoke
