# coding: utf-8


def test_contains_normal(dictator_inst, key_value):
    key, _ = key_value
    assert key in dictator_inst


def test_contains_missing(dictator_inst):
    assert 'test-missing' not in dictator_inst
