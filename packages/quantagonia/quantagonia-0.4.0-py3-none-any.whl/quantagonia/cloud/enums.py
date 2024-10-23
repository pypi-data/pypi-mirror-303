# ruff: noqa: PIE796 Enum contains duplicate value: `"/job"`
from enum import Enum


class Endpoints(str, Enum):
    checkjob = "/checkjob"
    getcurstatus = "/getcurstatus"
    getcursolution = "/getcursolution"
    getcurlog = "/getcurlog"
    getresults = "/getresults"
    getjobs = "/jobs"
    interruptjob = "/job"
    job = "/job"
    s3 = "/s3"


class JobStatus(str, Enum):
    created = "CREATED"
    running = "RUNNING"
    finished = "FINISHED"
    terminated = "TERMINATED"
    timeout = "TIMEOUT"
