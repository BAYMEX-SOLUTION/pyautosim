import json
import sys


class NotSupported(Exception):
    pass


class ActionIssue(Exception):
    pass


class PackIssue(Exception):
    pass


class Support():
    def __init__(self):
        self.minimum_version = (3, 4)
        self.returnStatement_prefix = 'SYSTEM::RETURN::--SPLIT--::'

    def versionCheck(self):
        if sys.version_info.major < self.minimum_version[0]:
            raise NotSupported('Minimum Python version : {}.{}'.format(
                self.minimum_version[0], self.minimum_version[1]))
        if sys.version_info.minor < self.minimum_version[1]:
            raise NotSupported('Minimum Python version : {}.{}'.format(
                self.minimum_version[0], self.minimum_version[1]))

    def unpackParameters(self):
        parameters = json.loads(sys.argv[-1])
        return parameters

    def returnStatement(self, data):
        toPrint = "{}{}".format(self.returnStatement_prefix, json.dumps(data))
        print(toPrint)
        sys.exit()
