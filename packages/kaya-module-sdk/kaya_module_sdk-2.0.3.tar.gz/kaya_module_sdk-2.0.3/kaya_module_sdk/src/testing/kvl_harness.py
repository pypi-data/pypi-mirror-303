import glob
import importlib
import inspect
import json
import logging
import os
import re
from abc import ABC, abstractmethod
from subprocess import PIPE, Popen

import pysnooper
from kaya_module_sdk.src.exceptions.files_not_found import \
    FilesNotFoundException
from kaya_module_sdk.src.exceptions.kvl_failure import KVLFailureException
from kaya_module_sdk.src.exceptions.tests_not_found import \
    TestsNotFoundException
from kaya_module_sdk.src.testing.kvl_executer import KVLE
from kaya_module_sdk.src.testing.kvl_reporter import KVLR

log = logging.getLogger(__name__)


class KVL:
    """[ KVL(H)arness ]: Responsibilities -

    * Searches Python3 source code files
        [ NOTE ]: If a directory is specified, looks for all *.py files
    * Runs KVL(E) with source file paths and/or module names depending on action
        When validating source code files it will receive the paths of the given files as strings
        When validating module input data at runtime it will receive the module name.
    * Runs KVL(R) with KVL(E) data
    * Maintains a stable interface for KVL's backend
    """

    _python_files: dict
    _python_module: str
    _filename_convention: dict
    _module_package: dict
    _kvl: dict

    def __init__(self, *args, **kwargs) -> None:
        self._filename_convention = {"suffix": ".py"}
        self._module_package = {
            "name": kwargs.get("module_name"),
            "instance": None,
        }
        self._python_files = {fl_path: [] for fl_path in args}
        self._kvl = {
            "executer": None,
            "reporter": None,
        }

    # UTILS

    #   #@pysnooper.snoop()
    def _search_python_files_in_dir(self, dir_path: str) -> list:
        python_files = []
        for root, _, files in os.walk(dir_path):
            for fl in files:
                if fl.endswith(self._filename_convention["suffix"]):
                    python_files.append(os.path.join(root, fl))
        return python_files

    #   #@pysnooper.snoop()
    def _import_package(self, package_name: str):
        pkg = importlib.import_module(package_name)
        return pkg

    #   #@pysnooper.snoop()
    def _load_python_files(self, target_files: str) -> dict:
        for file_path in target_files:
            with open(file_path, encoding="utf-8") as fl:
                data = fl.readlines()
            self._python_files.update({file_path: data})
        return self._python_files

    #   #@pysnooper.snoop()
    def _load_module_package(self, module_name: str) -> dict:
        loaded_pkg = self._import_package(f'{module_name.replace("-", "_")}.module')
        class_ = getattr(loaded_pkg, "KayaStrategyModule")
        instance = class_()
        self._module_package.update({"name": module_name, "instance": instance})
        return self._module_package

    #   #@pysnooper.snoop()
    def _get_kvl_executer(self, **kwargs: dict):
        if not self._kvl["executer"]:
            self._kvl["executer"] = KVLE(**kwargs)
        return self._kvl["executer"]

    #   #@pysnooper.snoop()
    def _get_kvl_reporter(self, **kwargs: dict):
        if not self._kvl["reporter"]:
            self._kvl["reporter"] = KVLR(**kwargs)
        return self._kvl["reporter"]

    # ACTIONS

    # @pysnooper.snoop()
    def check_rules(
        self,
        module: str = None,
        report: bool = True,
        dump_report: bool = False,
        **kwargs,
    ) -> dict:
        """[ NOTE ]: KVL(H) entry point for module constraints
        verifications."""
        if not module:
            raise KVLFailureException("No module package name specified!")
        module_data = self._load_module_package(module)
        try:
            verification_results = self._get_kvl_executer(**self.__dict__).check_rules(
                module_data
            )
            report = self._get_kvl_reporter(**self.__dict__).generate_report(
                {"rules": verification_results}, dump=dump_report
            )
        except Exception as e:
            raise KVLFailureException(
                "Module metadata verification failed! Details: " + str(e)
            )
        return report

    # @pysnooper.snoop()
    def check_meta(
        self,
        module: str = None,
        report: bool = True,
        dump_report: bool = False,
        **kwargs,
    ) -> dict:
        """[ NOTE ]: KVL(H) entry point for module metadata verifications."""
        if not module:
            raise KVLFailureException("No module package name specified!")
        module_data = self._load_module_package(module)
        try:
            verification_results = self._get_kvl_executer(**self.__dict__).check_meta(
                module_data
            )
            report = self._get_kvl_reporter(**self.__dict__).generate_report(
                {"meta": verification_results}, dump=dump_report
            )
        except Exception as e:
            raise KVLFailureException(
                "Module metadata verification failed! Details: " + str(e)
            )
        return report

    # @pysnooper.snoop()
    def check_source(
        self,
        file_path: str = None,
        report: bool = True,
        dump_report: bool = False,
        **kwargs: dict,
    ) -> dict:
        """[ NOTE ]: KVL(H) entry point for source code verifications."""
        target_path = file_path or "."
        python_file_paths = (
            self._search_python_files_in_dir(target_path)
            if os.path.isdir(target_path)
            else [target_path]
        )
        loaded_files = self._load_python_files(python_file_paths)
        try:
            verification_results = self._get_kvl_executer(**self.__dict__).check_source(
                loaded_files
            )
            report = self._get_kvl_reporter(**self.__dict__).generate_report(
                {"source": verification_results}, dump=dump_report
            )
        except Exception as e:
            raise KVLFailureException(
                "Source file verification failed! Details: " + str(e)
            )
        return report

    # @pysnooper.snoop()
    def check(self, *targets: str, **kwargs: dict) -> dict:
        """[ INPUT ]:

            * Positional arguments:

            - *targets - type string, options (meta|source|rules|all)

            * Keyword arguments:

            - report= - type bool, format and display verification results
            - dump_report= - type bool, implies <report=True> - dumps report to file
            - module= - type str, implies <(meta|rules|all) in *targets> - module package name
            - file_path= - type str, implies <(source|all) in *targets> - python file or directory to check recursively

        [ RETURN ]: KVL(R) report - type dict

        [ NOTE ]: Main KVL(H) entry point/interface for all verification types.
        """
        checkers = {
            "meta": self.check_meta,
            "source": self.check_source,
            "rules": self.check_rules,
        }
        to_check = checkers.keys() if "all" in targets else list(targets)
        if not to_check:
            print(f"[ ERROR ]: No verification targets specified!")
            return False
        check_results = {target: checkers[target](**kwargs) for target in to_check}
        return check_results


# CODE DUMP
