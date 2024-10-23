import glob
import json
import logging
import os
import re
from abc import ABC, abstractmethod
from subprocess import PIPE, Popen

import pysnooper
from kaya_module_sdk.src.exceptions.files_not_found import \
    FilesNotFoundException
from kaya_module_sdk.src.exceptions.kit_failure import KITFailureException
from kaya_module_sdk.src.exceptions.tests_not_found import \
    TestsNotFoundException
from kaya_module_sdk.src.testing.kit_executer import KITE
from kaya_module_sdk.src.testing.kit_reporter import KITR

log = logging.getLogger(__name__)


class KIT:
    """[ KIT(H)arness ]: Responsibilities -

    * Parses and validates JSON integration test files
        * [ NOTE ]: If a directory is specified, looks for all *.json files
    * Runs KIT(E) with test file data
    * Runs KIT(R) with KIT(E) data
    * Maintains a stable interface for KIT's backend
    """

    tests: list
    _required_keys: dict
    _optional_keys: dict
    _filename_convention: dict
    _webserver_host: str
    _webserver_port: int

    def __init__(self, *args, **kwargs) -> None:
        self.tests = list(args) or []
        self._required_keys = {
            "test_file": ["TESTS"],
            "test_case": ["name", "expected", "package", "module"],
            "case_expected": ["return", "errors"],
        }
        self._optional_keys = {
            "test_file": ["RESULT"],
            "test_case": [
                "result",
                "errors",
                "return",
                "path",
                "args",
                "package_version",
                "module_version",
            ],
        }
        self._filename_convention = {"prefix": "test_", "suffix": ".json"}
        self._webserver_host = kwargs.get("webserver_host", "127.0.0.1")
        self._webserver_port = kwargs.get("webserver_port", 8080)

    # @pysnooper.snoop()
    def _search_test_files_in_dir(self, dir_path: str) -> list:
        test_files = []
        for root, _, files in os.walk(dir_path):
            for fl in files:
                if fl.startswith(self._filename_convention["prefix"]) and fl.endswith(
                    self._filename_convention["suffix"]
                ):
                    test_files.append(os.path.join(root, fl))
        return test_files

    # @pysnooper.snoop()
    def _load_tests(self, test_files: str) -> list:
        for file_path in test_files:
            with open(file_path, encoding="utf-8") as file:
                data = json.load(file)
            self.tests += data["TESTS"]
        return self.tests

    # @pysnooper.snoop()
    def _validate_test_file(self, test_file: str) -> bool:
        try:
            with open(test_file, encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError, OSError):
            return False
        if not isinstance(data, dict):
            return False
        check_test_file = all(key in data for key in self._required_keys["test_file"])
        if not check_test_file:
            return False
        for test_case in data["TESTS"]:
            for key in test_case.keys():
                if (
                    key not in self._required_keys["test_case"]
                    and key not in self._optional_keys["test_case"]
                ):
                    return False
            check_test_case = all(
                key in test_case for key in self._required_keys["test_case"]
            )
            check_case_expected = all(
                key in test_case["expected"]
                for key in self._required_keys["case_expected"]
            )
            if not check_test_case or not check_case_expected:
                return False
        return True

    # @pysnooper.snoop()
    def _validate_test_files(self, test_files: list) -> dict:
        result = {"ok": [], "nok": []}
        for file_path in test_files:
            if not self._validate_test_file(file_path):
                result["nok"].append(file_path)
                continue
            result["ok"].append(file_path)
        return result

    # @pysnooper.snoop()
    def run(self, test_path: str, dump_report: bool = False) -> str:
        test_path = test_path or "."
        test_files = (
            self._search_test_files_in_dir(test_path)
            if os.path.isdir(test_path)
            else [test_path]
        )
        if not self.tests:
            if not test_files:
                err_msg = (
                    f"No KIT JSON test files found in {test_path}"
                    if os.path.isdir(test_path)
                    else f"Not a KIT JSON test file: {test_path}"
                )
                raise FilesNotFoundException(err_msg)
            test_validation = self._validate_test_files(test_files)
            if not test_validation.get("ok"):
                raise TestsNotFoundException("No valid KIT JSON test files found!")
            load = self._load_tests(test_validation["ok"])
        try:
            execution_results = KITE(**self.__dict__).run(*self.tests)
            report = KITR(**self.__dict__).generate_report(
                execution_results, dump=dump_report
            )
        except Exception as e:
            raise KITFailureException("Test execution failed! Details: " + str(e))
        return report


# CODE DUMP

#   if __name__ == '__main__':
#       test_report = KIT().run('./python-packages/KayaModuleExample/kaya_module_example/tst/integration/')

#   >>> from kaya_module_sdk.sdk import KIT

#   >>> test_report = KIT().run('./tst/integration')
#   >>> test_report
#   {
#       "TESTS": [
#           {
#               "name": "GoodWeather",
#               "package": "kaya_core_modules",
#               "package_version": "1.0.0"
#               "module": "ADD",
#               "module_version": "1.0.0",
################"path": "./tst/integration/test_module.json",
#               "args": {
#                   "first_no": {
#                       "value": [12],
#                       "type": "List[int]",
#                       "meta": {}
#                   },
#                   "second_no": {
#                       "value": [34],
#                       "type": "List[int]",
#                       "meta": {}
#                   }
#               },
#               "return": {
#                   "Sum": {
#                       "value": 12.34,
#                       "type": "float",
#                       "meta": {}
#                   }
#               },
#               "errors": [],
#               "expected": {
#                   "return": {
#                       "Sum": 12.34,
#                       "type": "float",
#                       "meta": {}
#                   },
#                   "errors": []
#               },
#               "result": "OK"
#           },
#           {
#               "name": "BadWeather",
#               "module": "dummy",
#               "version": "0.1.0"
#               "path": "./tst/integration/test_module.json",
#               "args": {
#                   "first_no": {
#                       "value": "Yo",
#                       "type": "str",
#                       "meta": {}
#                   },
#                   "second_no": {
#                       "value": ["sexeey B-)"],
#                       "type": "List[str]",
#                       "meta": {}
#                   }
#               },
#               "return": {},
#               "errors": ["TypeError"],
#               "expected": {
#                   "return": {},
#                   "errors": ["TypeError"]
#               },
#               "result": "OK"
#           }
#       ],
#       "RESULT": "OK"
#   }
