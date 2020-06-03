# encoding:utf-8
'''
shortcall包括入会、发起录制、发起共享、停止共享、停止录制、退会
'''

import common.logPrintClass
from CloudVideoClass import conferenceControlClass,create_meetingClass,recordingVodsClass




class shortcall:
    def __init__(self):
        self.log = common.logPrintClass.Log()

