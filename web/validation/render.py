#!/usr/bin/env python3

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('.', 'templates'))

template = env.get_template('hej.html')
print(template.render(the='variables', go='here'))
