import os
import json


class Pack():
    def __init__(self, config):
        self.config = config
        self.pack_list = os.listdir(self.config['packFolder'])
        self.pack_details = {}

    def scan(self):
        for each in self.pack_list:
            self.pack_details[each] = {}
            scope = self.pack_details[each]
            pack_root = os.path.join(self.config['packFolder'], each)

            # set pack info
            pack_info = json.load(open(os.path.join(pack_root, "pack.json")))
            scope.update(pack_info)
            scope['action_list'] = {}
            scope['path'] = pack_root

            # scan for action folders
            folder_list = os.listdir(pack_root)
            for f in folder_list:
                if os.path.isfile(os.path.join(pack_root, f)):
                    continue
                # check if action.json file is available
                if os.path.isfile(os.path.join(pack_root, f, 'action.json')):
                    # get action details
                    action_details = json.load(
                        open(os.path.join(pack_root, f, 'action.json')))
                    scope['action_list'][f] = action_details

        return self.pack_details
