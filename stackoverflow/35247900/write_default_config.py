#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()

config.add_section('section')
config['section']['setting_1'] = "hello"
config['section']['setting_2'] = "goodbye"

with open("default_config.ini", 'w') as f:
    config.write(f)
