#!/usr/bin/env python3

class Database:

    def __init__(self, path):

        with open(path, "r") as handle:
            #import json
            #self.data = json.load(handle)

            #import yaml
            #self.data = yaml.safe_load(handle)

            import xmltodict
            self.data = xmltodict.parse(handle.read())["root"]


    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None
