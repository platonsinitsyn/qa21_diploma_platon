import enum

BASE = "https://opensource-demo.orangehrmlive.com/web/index.php"


class URLS(enum.StrEnum):
    LOGIN = f"{BASE}/auth/login"
    MAIN_PAGE = "https://www.orangehrm.com/"
    ADMIN = f"{BASE}/admin/viewSystemUsers"
    PIM = f"{BASE}/pim/viewEmployeeList"
    LEAVE = f"{BASE}/leave/viewLeaveList"
    TIME = f"{BASE}/time/viewEmployeeTimesheet"
    RECRUITMENT = f"{BASE}/recruitment/viewCandidates"
    MY_INFO = f"{BASE}/pim/viewPersonalDetails/empNumber/7"
    PERFORMANCE = f"{BASE}/performance/searchEvaluatePerformanceReview"
    DASHBOARD = f"{BASE}/dashboard/index"
    ASSIGN_LEAVE = f"{BASE}/leave/assignLeave"
    DIRECTORY = f"{BASE}/directory/viewDirectory"
    MAINTENANCE = f"{BASE}/maintenance/purgeEmployee"
    CLAIM = f"{BASE}/claim/viewAssignClaim"
    BUZZ = f"{BASE}/buzz/viewBuzz"
    APPLY_LEAVE = f"{BASE}/leave/applyLeave"
    MY_LEAVE_LIST = f"{BASE}/leave/viewMyLeaveList"
    MY_TIME_TIMESHEET = f"{BASE}/time/viewMyTimesheet"
    SUPPORT = f"{BASE}/help/support"
    CHANGE_PASSWORD = f"{BASE}/pim/updatePassword"
    UPGRADE = "https://orangehrm.com/open-source/upgrade-to-advanced"
