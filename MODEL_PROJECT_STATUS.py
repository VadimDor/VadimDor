#!/usr/bin/env python
# pylint: disable=invalid-name

"""
MODEL_PROJECT_STATUS.py
Information about this projects use as a model project
"""
# pylint: enable=invalid-name
# Start of script
from asyncio import sleep

# modelProjectStatus
def modelProjectStatus():
    print('Model project status: This is a model project')
    print(
        "This is one of @vadimdor's Model projects. \
        It is certified as a project ready for use as a first impression \
        into vadimdor and his works"
    )
    sleep(1)

# main
def main():
    # print ("Model project status: This is a model project")
    # print ("This is one of @vadimdor's Model projects.
    #  It is certified as a project ready for use as a first impression into
    # vadimdor and his works")
    # sleep(1)
    # noMore = input("Press [ENTER] key to exit")
    # print("The program should now be closed. If you are not using Python
    # in a terminal, and the program is still open, try manually closing it with the close button.
    # If that doesn't work, try ending the process with a process/task manager.")
    return modelProjectStatus()


# End of script
