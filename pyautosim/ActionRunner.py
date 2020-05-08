import os
import sys
import subprocess
import json
from .Support import Support, PackIssue, ActionIssue


class ActionRunner():
    def __init__(self, config, pack_details):
        self.pack_details = pack_details
        self.config = config

    def runnerType_python(self, venvFolder, cur_pack_name):
        return os.path.join(venvFolder,
                            cur_pack_name,
                            'Scripts',
                            "python.exe")

    def run(self, pack_action_array, parameters):
        # check if pack is registered
        if pack_action_array[0] not in self.pack_details:
            raise PackIssue("Pack not found in registry")
        cur_pack = self.pack_details[pack_action_array[0]]
        cur_pack['name'] = pack_action_array[0]

        # check if action in pack is registered
        if pack_action_array[1] not in cur_pack['action_list']:
            raise ActionIssue("Pack not found in registry")
        cur_action = cur_pack['action_list'][pack_action_array[1]]
        # get action path
        cur_action['path'] = os.path.join(
            cur_pack['path'], pack_action_array[1])
        cur_action['name'] = pack_action_array[1]

        if cur_action['runner'] == 'python':
            # run entrypoint using venv python
            exe = self.runnerType_python(
                self.config['venvFolder'], cur_pack['name'])
        else:
            raise PackIssue("no runner defined for '{}'".format(cur_action['runner']))

        # change directory to action's folder
        original_cwd = os.getcwd()
        os.chdir(cur_action['path'])
        ret = subprocess.run([exe, cur_action['entrypoint'],
                              json.dumps(parameters)], shell=True, capture_output=True)
        os.chdir(original_cwd)

        # standardize return output
        stdout = ret.stdout.decode('utf-8').split('\r\n')
        stderr = ret.stderr.decode('utf-8').split('\r\n')

        result = {}
        # manipulate SYSTEM::
        for i in range(0, len(stdout)):
            each = stdout[i]

            # trim stdout. remove SYSTEM::
            if each.startswith(Support().returnStatement_prefix):
                temp = each.split(Support().returnStatement_prefix)[-1]
                result = json.loads(temp)
                stdout = stdout[0:i]
                break

        return {'stdout': stdout, 'stderr': stderr, 'returncode': ret.returncode, 'result': result}
