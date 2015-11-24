# # -*- coding: utf-8 -*-

import pandas as pd


class Document(object):
    _FILE_PATH_TEMPLATE = 'data/{taskID}.txt'

    def __init__(self, taskID):
        print("Process the taskID %d." % (taskID))
        self.taskID = taskID
        self.data = self._load_file(taskID)
        # print(self.data)  # Just for a debug

    def check(self):
        """ ErrorとWarningをチェックして戻す

        """
        return "Not Implemented Yet!"

    def _load_file(self, taskID):
        return pd.DataFrame.from_csv(
            self._FILE_PATH_TEMPLATE.format(taskID=taskID))

    def _check_eachline(self, i, line):
        error_flag = False
        warning_flag = False

        if error_flag is True:
            return (i, "Error Message")

        if warning_flag is True:
            return (i, "Warning Message")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process task information.')
    parser.add_argument('taskID', metavar='taskID', type=int, default=1,
                        help='id of the task')

    args = parser.parse_args(['1'])

    document = Document(args.taskID)
    print document.check()
