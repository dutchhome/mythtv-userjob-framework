#!/usr/bin/env python

"""
Provides user job base class to be used to build user job scripts.
db = MythDB()
j = Job(2353)
Recorded((j.get('chanid'),j.get('starttime')))
"""

from MythTV import MythDB
from MythTV import Job
from MythTV import Recorded
from argparse import ArgumentParser


class UserJob(object):
    """
    When subclassing, always call super(SubClassName,self).method() early in any overridden methods.
    
    Subclasses must provide: 
        <something>
            <purpose of something>
        <something2>
            <purpose of something2>

    Subclasses may provide:
        <something_else>
            <purpose of something_else>
        <something_else2>
            <purpose of something_else2>

    """
    
    def __init__(self):
        """
        Initializes the UserJob object
        """
        super(UserJob, self).__init__()
        self.jobid = None
        self.job = None
        self.recorded = None
        self.init_parser()
        self.build_action_map()
        
    def init_parser(self):
        """
        Initializes the ArgumentParser
        """
        self.parser = ArgumentParser()
        self.parser.add_argument("jobid", type=int, help="MythTV user job identifier (%%JOBID%%)")
        
    def parse_args(self):
        """
        """
        self.args = self.parser.parse_args()
        self.jobid = self.args.jobid
        self.job = Job(self.jobid)
        self.verify_job()
        self.recorded = Recorded((self.job.chanid,self.job.starttime))
        
    def verify_job(self):
        """
        """
        if not(self.job.type & Job.USERJOB):
            print "not a user job"
    
    def perform(self):
        """
        """
        self.parse_args()
            
    def start(self):
        """
        """
        self.job.setStatus(Job.STARTING)
        
    def run(self):
        """
        """
        self.start()
        self.job.setStatus(Job.RUNNING)
        
    def pause(self):
        """
        """
        self.job.setStatus(Job.PAUSED)
        
    def resume(self):
        """
        """
        self.job.setStatus(Job.RUNNING)
        
    def stop(self):
        """
        """
        self.job.setStatus(Job.STOPPING)

    def restart(self):
        """
        """
        self.stop()
        self.run()
        
    def build_action_map(self):
        """
        """
        self.action_map = {
            Job.RUN:self.run,
            Job.PAUSE:self.pause,
            Job.RESUME:self.resume,
            Job.STOP:self.stop,
            Job.RESTART:self.restart }
    
if __name__ == "__main__":
    UserJob().perform()
