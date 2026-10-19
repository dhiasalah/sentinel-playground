# Test file for the cluster webhook check (9.6 C). Intentionally unsafe: do not merge.
import subprocess


def ping(host):
    # Command injection: host comes from the user and goes into a shell.
    return subprocess.run("ping -c 1 " + host, shell=True, capture_output=True).stdout
