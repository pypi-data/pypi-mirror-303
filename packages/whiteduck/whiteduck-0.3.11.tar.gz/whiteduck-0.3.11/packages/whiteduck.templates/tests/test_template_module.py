import os
from unittest.mock import MagicMock, patch

import pytest
from rich.table import Table

from whiteduck.templates.app import TemplateModule
from whiteduck.templates.config import TEMPLATES_DIR
from whiteduck.templates.model.template import Template


@pytest.fixture
def template_module():
    return TemplateModule()


def test_get_name():
    assert TemplateModule.get_name() == "Templates"


def test_get_description():
    assert TemplateModule.get_description() == "Get your project started! 🧩"


@patch("whiteduck.templates.app.list_yaml_files")
def test_run_no_yaml_files(mock_list_yaml_files, template_module, capsys):
    mock_list_yaml_files.return_value = []
    template_module.run()
    captured = capsys.readouterr()
    assert "No YAML files found in" in captured.out


@patch("whiteduck.templates.app.list_yaml_files")
@patch("whiteduck.templates.app.TemplateModule.load_and_display_templates")
@patch("whiteduck.templates.app.TemplateModule.display_template_details")
@patch("whiteduck.templates.app.TemplateModule.execute_template")
def test_run_with_template(
    mock_execute, mock_display, mock_load, mock_list_yaml_files, template_module
):
    mock_list_yaml_files.return_value = ["template1.yaml"]
    mock_template = MagicMock(spec=Template)
    mock_load.return_value = mock_template
    mock_display.return_value = True

    template_module.run()

    mock_load.assert_called_once()
    mock_display.assert_called_once_with(mock_template)
    mock_execute.assert_called_once_with(mock_template)


def test_create_dependency_groups_table(template_module):
    mock_template = MagicMock()
    mock_group1 = MagicMock()
    mock_group1.name = "Group1"
    mock_group1.environment = "Env1"
    mock_group1.description = "Desc1"
    mock_group1.is_mandatory = True
    mock_group1.dependencies = []

    mock_group2 = MagicMock()
    mock_group2.name = "Group2"
    mock_group2.environment = "Env2"
    mock_group2.description = "Desc2"
    mock_group2.is_mandatory = False
    mock_group2.dependencies = []

    mock_template.dependency_groups = [mock_group1, mock_group2]

    table = template_module.create_dependency_groups_table(mock_template)
    assert isinstance(table, Table)
    assert len(table.rows) == 2


@patch("whiteduck.templates.app.questionary.select")
@patch("whiteduck.templates.app.Template.load_template")
def test_load_and_display_templates(mock_load_template, mock_select, template_module):
    mock_template = MagicMock(spec=Template)
    mock_template.template = "Test Template"
    mock_load_template.return_value = mock_template
    mock_select.return_value.ask.return_value = "Test Template\n"

    result = template_module.load_and_display_templates(["template1.yaml"])

    mock_load_template.assert_called_once_with(
        os.path.join(TEMPLATES_DIR, "template1.yaml")
    )
    assert result == mock_template


@patch("whiteduck.templates.app.questionary.select")
def test_display_template_details(mock_select, template_module):
    mock_template = MagicMock(spec=Template)
    mock_template.template = "Test Template"
    mock_template.description = "Test Description"
    mock_template.dependency_groups = []
    mock_select.return_value.ask.return_value = "Yes"

    result = template_module.display_template_details(mock_template)

    assert result is True
    mock_select.assert_called_once()


@patch("whiteduck.templates.app.TemplateExecutor.execute_template")
def test_execute_template(mock_execute, template_module):
    mock_template = MagicMock(spec=Template)
    template_module.execute_template(mock_template)
    mock_execute.assert_called_once_with(mock_template)


# Additional test cases for TemplateModule


@patch("whiteduck.templates.app.list_yaml_files")
def test_run_with_invalid_template(mock_list_yaml_files, template_module, capsys):
    mock_list_yaml_files.return_value = ["invalid_template.yaml"]
    with patch(
        "whiteduck.templates.app.Template.load_template",
        side_effect=ValueError("Invalid template"),
    ):
        with pytest.raises(ValueError, match="Invalid template"):
            template_module.run()


@patch("whiteduck.templates.app.Template.load_template")
def test_load_and_display_templates_no_selection(mock_load_template, template_module):
    mock_template = MagicMock(spec=Template)
    mock_template.template = "Test Template"
    mock_load_template.return_value = mock_template

    with patch(
        "whiteduck.templates.app.questionary.select",
        return_value=MagicMock(ask=MagicMock(return_value=None)),
    ):
        result = template_module.load_and_display_templates(["template1.yaml"])
        assert result is None


@patch("whiteduck.templates.app.questionary.select")
@patch("whiteduck.templates.app.questionary.text")
def test_display_template_details_show_readme(mock_text, mock_select, template_module):
    mock_template = MagicMock(spec=Template)
    mock_template.template = "Test Template"
    mock_template.description = "Test Description"
    mock_template.dependency_groups = []
    mock_select.return_value.ask.side_effect = ["Show Readme", "Yes"]
    mock_text.return_value.ask.return_value = ""

    result = template_module.display_template_details(mock_template)

    assert result is True
    assert mock_select.call_count == 2
