import importlib


def test_ingestion_package_imports():
    assert importlib.import_module("ingestion").__doc__
