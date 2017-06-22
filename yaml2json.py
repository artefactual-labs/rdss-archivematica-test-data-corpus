#!/usr/bin/env python3

# convert yaml to json
# pip3 install pyyaml
# http://pyyaml.org/wiki/PyYAMLDocumentation
# py3 yaml2json.py < ~/code/manpow/homeland/heartland/puphpet/config.yaml
# gist https://gist.github.com/noahcoad/51934724e0896184a2340217b383af73

import yaml, json, sys, uuid

doc = yaml.load(sys.stdin)
doc['messageHeader']['messageId'] = str(uuid.uuid4())

sys.stdout.write(json.dumps(doc, sort_keys=True, indent=4))
