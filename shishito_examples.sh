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

# Shishito to PYTHONPATH
export PYTHONPATH=${PYTHONPATH}:/${shishito_framework}

# -----------------
#      TESTS
# -----------------

# COMBINATIONS UNSUPPORTED by Shishito
# --mobile yes & --tests smoke

# INVALID COMBINATIONS (will not fail but do not make sense)
# --env direct & --tests smoke

# DESKTOP COMBINATIONS
export BROWSERSTACK='{"test_suite": [{"browser": "Firefox", "browser_version": "33.0","os": "Windows", "os_version": "7", "resolution": "1024x768"},{"browser": "Chrome", "browser_version": "38.0", "os": "Windows","os_version": "7", "resolution": "1024x768"}]}'

python ${shishito_test_project}/google_test_runner.py --browserstack ${browserstack_user}:${browserstack_pass}

python ${shishito_test_project}/google_test_runner.py --mobile yes --browserstack ${browserstack_user}:${browserstack_pass}

python ${shishito_test_project}/google_test_runner.py --tests smoke --browserstack ${browserstack_user}:${browserstack_pass}

# UNSUPPORTED
#python ${shishito_test_project}/google_test_runner.py --mobile yes --tests smoke

python ${shishito_test_project}/google_test_runner.py --env direct --browserstack ${browserstack_user}:${browserstack_pass}

# INVALID
#python ${shishito_test_project}/google_test_runner.py --env direct --tests smoke --browserstack ${browserstack_user}:${browserstack_pass}

# MOBILE COMBINATIONS
export BROWSERSTACK='{"test_suite": [{"browserName": "iPad", "platform": "MAC","device": "iPad Air", "deviceOrientation": "landscape"},{"browserName": "android", "platform": "ANDROID", "device": "Samsung Galaxy Tab 4 10.1","deviceOrientation": "landscape"}]}'
python ${shishito_test_project}/google_test_runner.py --env direct --mobile yes --browserstack ${browserstack_user}:${browserstack_pass}

# UNSUPPORTED
# python ${shishito_test_project}/google_test_runner.py --env direct --mobile yes --tests smoke --browserstack ${browserstack_user}:${browserstack_pass}