import os

from .app import start_application, start_test_application

###
# Depending on the env variable TEST_MODE, we run different actions
# This is to avoid running db setup actions in test mode
#
test_mode = os.environ.get("TEST_MODE")
if test_mode:
    app = start_test_application()
else:
    app = start_application()
