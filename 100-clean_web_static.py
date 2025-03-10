#!/usr/bin/python3
""" Function that deletes out-of-date archives """
from fabric.api import *

env.hosts = ["34.204.95.241", "52.87.230.196"]
env.user = "ubuntu"


def do_clean(number=0):
    """CLEANS"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "~/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
