import json
import os
from unittest.mock import MagicMock, mock_open, patch

import pytest

from whiteduck.tasks.app import TasksModule
from whiteduck.tasks.model.tasks import PoeTask, VSCodeTask


@pytest.fixture
def tasks_module():
    return TasksModule()


def test_sync_tasks_menu(tasks_module):
    with patch(
        "whiteduck.tasks.app.TasksModule.sync_poe_to_vscode"
    ) as mock_sync, patch(
        "whiteduck.tasks.app.TasksModule.display_task_dependency"
    ) as mock_display, patch(
        "whiteduck.tasks.app.TasksModule.edit_vscode_task"
    ) as mock_edit, patch(
        "whiteduck.tasks.app.TasksModule.create_new_task"
    ) as mock_create, patch("questionary.select") as mock_select:
        mock_select.return_value.ask.side_effect = [
            "Sync Poe tasks to VSCode tasks",
            "View current tasks",
            "Edit existing task",
            "Create new task",
            "Exit",
        ]

        tasks_module.sync_tasks_menu("dummy_vscode.json", "dummy_poe.toml")

        mock_sync.assert_called_once()
        mock_display.assert_called_once()
        mock_edit.assert_called_once()
        mock_create.assert_called_once()


def test_find_task_files(tasks_module):
    with patch("os.walk") as mock_walk:
        mock_walk.return_value = [
            ("/root", [], ["pyproject.toml", "tasks.json", "other.txt"]),
            ("/root/sub", [], ["tasks.json"]),
        ]
        result = tasks_module.find_task_files()

        assert len(result) == 3
        assert os.path.join("/root", "pyproject.toml") in result
        assert os.path.join("/root", "tasks.json") in result
        assert os.path.join("/root/sub", "tasks.json") in result


def test_parse_vscode_tasks(tasks_module):
    mock_json = """
    {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Run Test",
                "type": "process",
                "command": "uv",
                "args": ["run", "poe", "run_test"],
                "group": {"kind": "test", "isDefault": true},
                "problemMatcher": "$python",
                "presentation": {"echo": true, "reveal": "always"}
            }
        ]
    }
    """
    with patch("builtins.open", mock_open(read_data=mock_json)):
        tasks = tasks_module.parse_vscode_tasks("dummy_path")

        assert len(tasks) == 1
        assert isinstance(tasks[0], VSCodeTask)
        assert tasks[0].label == "Run Test"
        assert tasks[0].command == "uv"
        assert tasks[0].args == ["run", "poe", "run_test"]


def test_parse_poe_tasks(tasks_module):
    mock_toml = """
    [tool.poe.tasks]
    run_test = "uv run --extra test-pytest pytest --cov=src/whiteduck tests/ --verbose"
    docker_run = ["docker_build", "docker_start"]
    """
    with patch("builtins.open", mock_open(read_data=mock_toml)):
        tasks = tasks_module.parse_poe_tasks("dummy_path")

        assert len(tasks) == 2
        assert isinstance(tasks["run_test"], PoeTask)
        assert tasks["run_test"].name == "run_test"
        assert (
            tasks["run_test"].command
            == "uv run --extra test-pytest pytest --cov=src/whiteduck tests/ --verbose"
        )


def test_display_task_dependency(tasks_module, capsys):
    vscode_tasks = [
        VSCodeTask(
            "Run Test",
            "process",
            "uv",
            ["run", "poe", "run_test"],
            {"kind": "test", "isDefault": True},
            "$python",
            {"echo": True, "reveal": "always"},
        )
    ]
    poe_tasks = {
        "run_test": PoeTask(
            "run_test",
            "uv run --extra test-pytest pytest --cov=src/whiteduck tests/ --verbose",
        )
    }

    with patch.object(
        TasksModule, "parse_vscode_tasks", return_value=vscode_tasks
    ), patch.object(TasksModule, "parse_poe_tasks", return_value=poe_tasks):
        tasks_module.display_task_dependency("dummy_vscode.json", "dummy_poe.toml")
        captured = capsys.readouterr()

        assert "Task Dependency" in captured.out
        assert "VSCode Tasks" in captured.out
        assert "Poe Tasks" in captured.out
        assert "Run Test" in captured.out
        assert "run_test" in captured.out


def test_edit_poe_task(tasks_module):
    mock_poe_file = """
    [tool.poe.tasks]
    run_test = "uv run --extra test-pytest pytest --cov=src/whiteduck tests/ --verbose"
    """

    with patch("builtins.open", mock_open(read_data=mock_poe_file)), patch(
        "questionary.select",
        return_value=MagicMock(ask=MagicMock(return_value="run_test")),
    ), patch(
        "questionary.text",
        side_effect=[
            MagicMock(ask=MagicMock(return_value="new_test")),
            MagicMock(ask=MagicMock(return_value="pytest --cov=src/whiteduck tests/")),
        ],
    ), patch(
        "toml.load",
        return_value={
            "tool": {
                "poe": {
                    "tasks": {
                        "run_test": "uv run --extra test-pytest pytest --cov=src/whiteduck tests/ --verbose"
                    }
                }
            }
        },
    ), patch("toml.dump") as mock_toml_dump:
        tasks_module.edit_poe_task("dummy_poe.toml")

        mock_toml_dump.assert_called_once()
        dumped_content = mock_toml_dump.call_args[0][0]

        assert (
            dumped_content["tool"]["poe"]["tasks"]["new_test"]
            == "pytest --cov=src/whiteduck tests/"
        )


def test_create_new_task(tasks_module):
    mock_vscode_file = '{"version": "2.0.0", "tasks": []}'
    mock_poe_file = "[tool.poe.tasks]"

    with patch("builtins.open", mock_open()), patch(
        "questionary.select",
        side_effect=[
            MagicMock(ask=MagicMock(return_value="VSCode")),
            MagicMock(ask=MagicMock(return_value="Poe")),
        ],
    ), patch(
        "questionary.text",
        side_effect=[
            MagicMock(ask=MagicMock(return_value="new_vscode_task")),
            MagicMock(ask=MagicMock(return_value="python -m pytest")),
            MagicMock(ask=MagicMock(return_value="new_poe_task")),
            MagicMock(ask=MagicMock(return_value="pytest --cov=src/whiteduck tests/")),
        ],
    ), patch("json.load", return_value={"version": "2.0.0", "tasks": []}), patch(
        "json.dump"
    ) as mock_json_dump, patch(
        "toml.load", return_value={"tool": {"poe": {"tasks": {}}}}
    ), patch("toml.dump") as mock_toml_dump:
        # Test creating a new VSCode task
        tasks_module.create_new_task("dummy_vscode.json", "dummy_poe.toml")
        mock_json_dump.assert_called()
        dumped_json = mock_json_dump.call_args[0][0]
        assert any(task["label"] == "new_vscode_task" for task in dumped_json["tasks"])

        # Test creating a new Poe task
        tasks_module.create_new_task("dummy_vscode.json", "dummy_poe.toml")
        mock_toml_dump.assert_called()
        dumped_toml = mock_toml_dump.call_args[0][0]
        assert (
            dumped_toml["tool"]["poe"]["tasks"]["new_poe_task"]
            == "pytest --cov=src/whiteduck tests/"
        )


# Additional test cases for TasksModule


def test_run_no_task_files(tasks_module, capsys):
    with patch.object(TasksModule, "find_task_files", return_value=[]):
        tasks_module.run()
        captured = capsys.readouterr()
        assert "No task files found." in captured.out


def test_sync_poe_to_vscode_no_new_tasks(tasks_module):
    mock_vscode_file = '{"version": "2.0.0", "tasks": []}'
    mock_poe_file = "[tool.poe.tasks]"

    with patch("builtins.open", mock_open(read_data=mock_vscode_file)), patch(
        "toml.load", return_value={"tool": {"poe": {"tasks": {}}}}
    ), patch("json.dump") as mock_json_dump:
        tasks_module.sync_poe_to_vscode("dummy_vscode.json", "dummy_poe.toml")
        mock_json_dump.assert_not_called()


def test_edit_vscode_task_invalid_selection(tasks_module):
    mock_vscode_file = '{"version": "2.0.0", "tasks": []}'
    mock_poe_file = """
    [tool.poe.tasks]
    """

    with patch("builtins.open", mock_open(read_data=mock_vscode_file)), patch(
        "questionary.select",
        return_value=MagicMock(ask=MagicMock(return_value="invalid_task")),
    ), patch("toml.load", return_value={"tool": {"poe": {"tasks": {}}}}), patch(
        "json.dump"
    ) as mock_json_dump:
        tasks_module.edit_vscode_task("dummy_vscode.json", "dummy_poe.toml")
        mock_json_dump.assert_not_called()
