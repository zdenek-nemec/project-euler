#!/usr/bin/env python

"""
Create Sphinx documentation for Project Euler
---------------------------------------------

Name: create_documentation.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.1 (2018-02-23)

Synopsis:
    ``create_documentation.py``

Examples:
    ``create_documentation.py``

Description:
    Create RST files for Sphinx documentation of Project Euler.
"""


import os


MODULES_PATH = "./_modules"


# Main ########################################################################

def main():
    if (not(os.path.exists(MODULES_PATH))):
        os.makedirs(MODULES_PATH)

    projects = []
    for subdir in next(os.walk("."))[1]:
        if (subdir[0:5] == "pe000"):
            continue
        elif (subdir[0:2] == "pe"):
            projects.append(subdir[0:5])

    for subdir in next(os.walk("."))[1]:
        if (subdir[0:5] == "pe000"):
            continue
        if (subdir[0:2] == "pe"):
            open_flag = False
            with open("." + "/" + subdir + "/" + subdir[0:5] + ".py", "r") as f:
                while (1):
                    line = f.readline()
                    if (line == ""):
                        break
                    elif (line[0:10] == "Version: 0"):
                        open_flag = True
                        break
                    elif (line[0:8] == "Version:"):
                        break
            filename = ""
            if (open_flag):
                filename += "open_"
            filename += subdir[0:5] + ".rst"
            anchor = ".. _pe%03d: \n\n" % (int(subdir[2:5]))

            subdir_str = "pe%03d" % (int(subdir[2:5]) - 1)
            if (subdir_str in projects):
                link_previous = ":ref:`Previous <pe%03d>`" % (int(subdir[2:5]) - 1)
            else:
                link_previous = "Previous"

            subdir_str = "pe%03d" % (int(subdir[2:5]) + 1)
            if (subdir_str in projects):
                link_next = ":ref:`Next <pe%03d>`" % (int(subdir[2:5]) + 1)
            else:
                link_next = "Next"

            content = anchor \
                + link_previous + " | :ref:`Index <index>` | " + link_next + "\n\n" \
                + ".. automodule:: " + subdir[0:5] + "\n" \
                + "    :members:\n" \
                + "    :undoc-members:\n" \
                + "    :private-members:\n\n" \
                + link_previous + " | :ref:`Index <index>` | " + link_next + "\n"
            with open(MODULES_PATH + "/" + filename, "w") as f:
                f.write(content)

    return 0


if __name__ == "__main__":
    main()
