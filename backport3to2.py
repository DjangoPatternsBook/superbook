from __future__ import print_function
import os
import fileinput
import re
import sys


def show_warning():
    print("""************** WARNING *********************8

backport3to2.py performs an in-place modification of the SuperBook
project so that it works in Python 2.7. Hence, it will NOT WORK
correctly for Python 3.4 anymore. Please note that this is one-way
conversion and cannot be reversed.

Please confirm by pressing 'y' or 'Y' if you are sure that you would
like to continue with this conversion to Python 2.7. Press any other
key to abort: """, end="")
    real_raw_input = vars(__builtins__).get('raw_input', input)
    choice = real_raw_input().lower()
    if choice != 'y':
        sys.exit(-1)
    if 'raw_input' not in vars(__builtins__):
        print("""\nLooks like your are already on Python 3. This script
is for Python 2 users. Are you sure you want to continue?
(Y/N): """, end="")
        choice = real_raw_input().lower()
        if choice != 'y':
            sys.exit(-1)
    return


def backport(rootdir="."):
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            src_filename = os.path.join(folder, filename)
            # Skip non python files
            if not src_filename.endswith(".py"):
                continue
            if (__file__ and os.path.basename(src_filename) ==
                    os.path.basename(__file__)):
                continue
            print(src_filename)
            last_class = ""
            for line in fileinput.input(src_filename, inplace=True):
                if fileinput.filelineno() == 1:
                    if line.startswith("#!"):
                        print(line, end="")
                        print("from __future__ import unicode_literals")
                    else:
                        print("from __future__ import unicode_literals")
                        print(line, end="")
                    continue
                if line.strip().startswith("class"):
                    last_class = line.strip().split()[1]
                    last_class = re.match(r'([a-zA-Z0-9]+)',
                                          last_class).group(1)
                if "__str__(" in line:
                    line = line.replace("__str__(", "__unicode__(")
                if "super()" in line:
                    old_super = "super({}, self)".format(last_class)
                    line = line.replace("super()", old_super)
                print(line, end="")

show_warning()
backport()
