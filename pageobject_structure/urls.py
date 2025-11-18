import enum


class URLS(enum.StrEnum):
    BASE = "https://opensource-demo.orangehrmlive.com/"
    LOGIN = "web/index.php/auth/login"
    DASHBOARD = "web/index.php/dashboard/index"
    ASSIGN_LEAVE = "web/index.php/leave/assignLeave"
    LEAVE_LIST = "web/index.php/leave/viewLeaveList"
    TIME_TIMESHEET = "web/index.php/time/viewEmployeeTimesheet"
    APPLY_LEAVE = "web/index.php/leave/applyLeave"
    MY_LEAVE_LIST = "web/index.php/leave/viewMyLeaveList"
    MY_TIME_TIMESHEET = "web/index.php/time/viewMyTimesheet"
