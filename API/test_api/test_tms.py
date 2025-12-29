from datetime import datetime
import pytest
from API.test_api.logger import logger
from API.test_api.tms_service import TmsService


@pytest.fixture
def tms_service():
    return TmsService()


@pytest.fixture
def token(tms_service):
    # Очищаем pytest.token перед логином
    pytest.token = None
    response_json = tms_service.login("user@example.com", "admin123")
    assert response_json["access_token"]
    pytest.token = response_json["access_token"]
    return pytest.token


@pytest.mark.only
def test_create_second_admin(tms_service):
    pytest.token = None
    response_json = tms_service.register_admin("admin2", "admin2@example.com", "qwerty123!", code=403)

    assert response_json["detail"] == "Admin already exists. Registration is disabled."
    logger.info(response_json)


@pytest.mark.only
def test_create_board(token, tms_service):
    response_json = tms_service.create_board("test_board", "just a test board for testing", False)

    logger.info(response_json)
    assert response_json["id"]
    assert response_json["archived"] is False
    assert response_json["created_by"]
    assert response_json["title"] == "test_board"
    assert response_json["description"] == "just a test board for testing"
    assert response_json["public"] is False

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


@pytest.mark.only
def test_create_task(token, tms_service):
    board_response = tms_service.create_board("string", "string", False)
    logger.info(board_response)
    board_id = board_response["id"]

    response_json = tms_service.create_task(board_id, "Моя вторая задача", "Описание задачи", "todo", "high")

    assert response_json["id"]
    assert response_json["created_by"]
    assert response_json["title"] == "Моя вторая задача"
    assert response_json["status"] == "todo"
    assert response_json["priority"] == "high"

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)
    assert response_json["updated_at"].startswith(current_date)


@pytest.mark.only
def test_get_users(token, tms_service):
    response_json = tms_service.get_users(skip=0, limit=100)

    logger.info(response_json)
    assert response_json[0]["id"] == 1
    assert response_json[0]["username"] == "string"
    assert response_json[0]["email"] == "user@example.com"
    assert response_json[0]["role"] == "admin"
    assert response_json[0]["avatar_url"] is None


@pytest.mark.only
def test_get_users_without_token(tms_service):
    pytest.token = None
    response_json = tms_service.get_users(skip=0, limit=100, code=403)

    logger.info(response_json)
    assert response_json["detail"] == "Not authenticated"


# HOMEWORK HERE:
@pytest.mark.only
def test_add_board_members(token, tms_service):
    board_response = tms_service.create_board("new board", "test", False)
    board_id = board_response["id"]
    logger.info(board_response)

    response_json = tms_service.add_user_board(board_id, 1, 201)

    logger.info(response_json)
    assert response_json["message"] == "User added to board"


@pytest.mark.only
def test_get_board_members(token, tms_service):
    response_json = tms_service.get_board_members(6, 200)

    logger.info(response_json)
    assert response_json[0]["username"] == "user1"
    assert response_json[0]["email"] == "me_user@example.com"


@pytest.mark.only
def test_get_board_stats(token, tms_service):
    response_json = tms_service.get_board_stats(6, 200)

    logger.info(response_json)
    expected_keys = {"total", "todo", "in_progress", "done"}
    assert set(response_json.keys()) == expected_keys


@pytest.mark.only
def test_search_tasks(token, tms_service):
    board_response = tms_service.create_board("search board", "test", False)
    logger.info(board_response)
    board_id = board_response["id"]

    created_task = tms_service.create_task(board_id, "Platon task 1", "Test", "todo", "high")
    created_task_2 = tms_service.create_task(board_id, "Platon task 2", "Test", "todo", "high")
    all_tasks = [created_task["id"], created_task_2["id"]]

    response_json = tms_service.search_tasks("Platon")

    logger.info(response_json)
    tasks_found = [t for t in response_json if t["id"] in all_tasks]
    assert len(tasks_found) == 2


@pytest.mark.only
def test_move_task_next_status(token, tms_service):
    board_id = 6
    task_response = tms_service.create_task(board_id, "Task 1", "Test", "todo", "high")
    task_id = task_response["id"]
    logger.info(task_response)

    response_json = tms_service.change_task_status(task_id)

    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["title"] == task_response["title"]
    assert response_json["description"] == task_response["description"]
    assert response_json["priority"] == task_response["priority"]
    assert response_json["status"] == "in_progress"


@pytest.mark.only
def test_set_new_task_priority(token, tms_service):
    board_id = 6
    task_response = tms_service.create_task(board_id, "Task 1", "Test", "todo", "medium")
    task_id = task_response["id"]
    logger.info(task_response)

    response_json = tms_service.change_task_priority(task_id, "high")

    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["title"] == task_response["title"]
    assert response_json["description"] == task_response["description"]
    assert response_json["status"] == task_response["status"]
    assert response_json["priority"] == "high"


@pytest.mark.only
def test_move_task_to_board(token, tms_service):
    board_id = 6
    target_board_id = 2
    task_response = tms_service.create_task(board_id, "Task 1", "Test", "todo", "medium")
    task_id = task_response["id"]
    logger.info(task_response)

    response_json = tms_service.move_task_to_board(board_id, task_id, target_board_id)

    logger.info(response_json)
    assert response_json["id"] == task_id
    assert response_json["title"] == task_response["title"]
    assert response_json["description"] == task_response["description"]
    assert response_json["board_id"] == target_board_id


@pytest.mark.only
def test_archive_board(token, tms_service):
    board_response = tms_service.create_board("archive board", "test", False)
    board_id = board_response["id"]
    logger.info(board_response)

    response_json = tms_service.archive_board(board_id)

    logger.info(response_json)
    assert response_json["id"] == board_id
    assert response_json["title"] == board_response["title"]
    assert response_json["description"] == board_response["description"]
    assert response_json["archived"] is True


@pytest.mark.only
def test_bulk_update_tasks(token, tms_service):
    board_id = 1
    task_response = tms_service.create_task(board_id, "Task 1", "Test", "todo", "medium")
    task_response_2 = tms_service.create_task(board_id, "Task 1", "Test", "todo", "medium")
    task_id = task_response["id"]
    task_id_2 = task_response_2["id"]
    all_tasks = [task_id, task_id_2]
    logger.info(task_response, task_response_2)

    response_json = tms_service.board_tasks_bulk_update(1, all_tasks, "in_progress")

    logger.info(response_json)
    assert response_json["updated"] == 2
    assert response_json["message"] == "Updated 2 tasks to status 'in_progress'"


@pytest.mark.only
def test_get_me_tasks(tms_service):
    pytest.token = None
    login_response = tms_service.login("me_user@example.com", "me123456")
    assert login_response["access_token"]
    pytest.token = login_response["access_token"]

    board_response = tms_service.create_board("archive board", "test", False)
    board_id = board_response["id"]
    logger.info(board_response)

    tms_service.create_task(board_id, "Me task 1", "Test", "todo", "medium")
    tms_service.create_task(board_id, "Me task 2", "Test", "todo", "high")
    tms_service.create_task(board_id, "Me task 2", "Test", "todo", "low")

    response_json = tms_service.get_me_tasks(200)

    logger.info(response_json)
    my_tasks = [t for t in response_json if t["board_id"] == board_id]
    assert len(my_tasks) == 3
