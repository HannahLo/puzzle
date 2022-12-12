#!/usr/bin/python

from pathlib import Path

import os
import string
import sys

if __name__ == "__main__":
    day = sys.argv[1]

    dir_ = Path(os.path.dirname(__file__))
    template_dir = dir_ / 'template'
    file = template_dir / 'day_n.py'
    test_file = template_dir / 'test_day_n.py'

    with open(file) as t:
        template = string.Template(t.read())
        final_output = template.substitute(number=day)
        with open(f"day_{day}.py", "w") as output:
            output.write(final_output)

    with open(test_file) as t:
        template = string.Template(t.read())
        final_output = template.substitute(number=day)
        with open(f"test/test_day_{day}.py", "w") as output:
            output.write(final_output)
