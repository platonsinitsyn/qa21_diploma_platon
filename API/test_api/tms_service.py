from API.test_api.base_service import BaseService

DOMAIN = "http://localhost:8000"


class TmsService(BaseService):

    def __init__(self):
        self.token = None

    def login(self, email, password):
        url = f"{DOMAIN}/auth/login"
        body = {"email": email, "password": password}
        response = self.post(url, token=None, body=body, code=200)
        self.token = response["access_token"]
        return response

    def register_admin(self, username, email, password, code=None):
        url = f"{DOMAIN}/auth/register-admin"
        body = {"username": username, "email": email, "password": password}
        response = self.post(url, token=None, body=body, code=code)
        return response

    def create_board(self, title, description, public):
        url = f"{DOMAIN}/boards/"
        body = {"title": title, "description": description, "public": public}
        response = self.post(url, token=None, body=body, code=201)
        return response

    def create_task(self, board_id, title, description, status, priority):
        url = f"{DOMAIN}/boards/{board_id}/tasks"
        body = {"title": title, "description": description, "status": status, "priority": priority}
        response = self.post(url, token=None, body=body, code=201)
        return response

    def get_users(self, skip, limit, code=200):
        url = f"{DOMAIN}/users/?skip={skip}&limit={limit}"
        response = self.get(url, code=code)
        return response

    def add_user_board(self, board_id, user_id, code=201):
        url = f"{DOMAIN}/boards/{board_id}/members/{user_id}"
        response = self.post(url, token=None, body=None, code=code)
        return response

    def get_board_members(self, board_id, code=201):
        url = f"{DOMAIN}/boards/{board_id}/members"
        response = self.get(url, code=code)
        return response

    def get_board_stats(self, board_id, code=200):
        url = f"{DOMAIN}/boards/{board_id}/stats"
        response = self.get(url, code=code)
        return response

    def get_me_tasks(self, code=200):
        url = f"{DOMAIN}/users/me/tasks"
        response = self.get(url, code=code)
        return response

    def search_tasks(self, q: str, code=200):
        url = f"{DOMAIN}/tasks/search?q={q}"
        response = self.get(url, code=code)
        return response

    def change_task_status(self, task_id):
        url = f"{DOMAIN}/tasks/{task_id}/next-status"
        response = self.put(url, body=None, code=None)
        return response

    def change_task_priority(self, task_id, new_priority):
        url = f"{DOMAIN}/tasks/{task_id}/priority/{new_priority}"
        response = self.put(url, body=None, code=None)
        return response

    def move_task_to_board(self, board_id, task_id, target_board_id):
        url = f"{DOMAIN}/boards/{board_id}/tasks/{task_id}/move-to/{target_board_id}"
        response = self.put(url, body=None, code=None)
        return response

    def archive_board(self, board_id):
        url = f"{DOMAIN}/boards/{board_id}/archive"
        response = self.put(url, body=None, code=None)
        return response

    def board_tasks_bulk_update(self, board_id, all_tasks, bulk_status):
        url = f"{DOMAIN}/boards/{board_id}/tasks/bulk/status"
        body = {"task_ids": all_tasks, "new_status": bulk_status}
        response = self.put(url, body=body, code=None)
        return response
