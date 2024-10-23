import logging
from subprocess import PIPE, Popen

log = logging.getLogger("KayaPythonModuleSDK")


def shell_cmd(command: list, user=None):
    log.debug("")
    log.debug("Issuing system command: ({})".format(command))
    command = " ".join(command)
    if user:
        command = "su {} -c '{}'".format(user, command)
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    output, errors = process.communicate()
    log.debug("Output: ({}), Errors: ({})".format(output, errors))
    return str(output).rstrip("\n"), str(errors).rstrip("\n"), process.returncode
