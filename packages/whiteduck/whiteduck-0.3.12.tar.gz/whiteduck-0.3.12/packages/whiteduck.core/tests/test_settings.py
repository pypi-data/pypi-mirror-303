import os
import pytest
from whiteduck.core.modules.settings import Settings

@pytest.fixture
def settings():
    test_filename = 'test_settings.json'
    default_settings = {'key1': 'value1', 'key2': 'value2'}
    settings = Settings(filename=test_filename, default_settings=default_settings)
    yield settings
    if os.path.exists(test_filename):
        os.remove(test_filename)

def test_load_default_settings(settings):
    assert settings.settings == {'key1': 'value1', 'key2': 'value2'}

def test_save_and_load_settings(settings):
    settings.set('key1', 'new_value1')
    settings.save_settings()
    new_settings = Settings(filename='test_settings.json')
    assert new_settings.get('key1') == 'new_value1'

def test_get_default_value(settings):
    assert settings.get('key3', 'default_value') == 'default_value'

def test_set_and_get_setting(settings):
    settings.set('key3', 'value3')
    assert settings.get('key3') == 'value3'
