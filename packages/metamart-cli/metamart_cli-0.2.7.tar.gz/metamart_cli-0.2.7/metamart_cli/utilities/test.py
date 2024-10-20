import subprocess

from metamart_cli.settings.config import BasicAuthSettings, ServerSettingsV1


def prep_test_auth():
    """ """
    from metamart_cli.settings.config import config

    config.server = ServerSettingsV1(url="http://localhost:8000", workspace="default/default")
    config.auth = BasicAuthSettings(username="null@metamart.io", password="super_secret")


def disable_telemetry():
    """ """
    subprocess.run(["metamart", "--no-telemetry"])


def prep_tests():
    """ """
    prep_test_auth()
    disable_telemetry()
