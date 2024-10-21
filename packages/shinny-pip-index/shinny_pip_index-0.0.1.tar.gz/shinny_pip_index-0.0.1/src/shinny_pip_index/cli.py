import argparse
import subprocess
import sys

from .server import run


def app():
    parser = argparse.ArgumentParser(
        prog='shinny-pip',
        description='simple pip index for shinny-cd private package',
        add_help=False,
    )
    parser.add_argument('install')  # positional argument
    parser.add_argument('-i', '--index-url')
    install, args = parser.parse_known_intermixed_args()
    assert install.install == "install", f"unsupported command: {install}"
    port = run()
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install"] + args + ["--index-url", f"http://localhost:{port}"])
