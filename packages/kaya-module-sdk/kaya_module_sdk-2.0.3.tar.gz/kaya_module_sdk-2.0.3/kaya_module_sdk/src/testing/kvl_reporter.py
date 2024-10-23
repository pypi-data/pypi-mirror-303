import json
import logging
import os

import pysnooper
from kaya_module_sdk.src.exceptions.malformed_results import \
    MalformedResultsException
from kaya_module_sdk.src.exceptions.write_failure import WriteFailureException

log = logging.getLogger(__name__)


class KVLR:
    """[ KVL(R)eporter ]: Responsibilities -

    * Processes and formats results received from KVL(E)
    * Generates JSON report dump file if specified
    """

    report: dict
    context: dict
    dump_file_path: str

    def __init__(self, dump_file: str = None, **kwargs: dict) -> None:
        self.report = {}
        self.context = kwargs
        self.dump_file_path = dump_file or "kvl.report"

    # UTILS

    #   #@pysnooper.snoop()
    def _check_dump_file_path(self, *args, **kwargs) -> bool:
        directory = os.path.dirname(self.dump_file_path)
        if not directory:
            directory = "."
        if (
            not os.path.exists(directory)
            or not os.path.isdir(directory)
            or not os.access(directory, os.W_OK)
        ):
            raise WriteFailureException(
                "KVL(R)eporter dump file {self.dump_file_path} has an unexistent "
                "parent directory or location restricts write permissions."
            )
        return True

    #   #@pysnooper.snoop()
    def _check_kvle_results(self, *results, **kwargs):
        if not results:
            raise MalformedResultsException(
                "KVL(R)eporter received malformed results to process!"
            )
        for result in results:
            if (
                not "source" in result
                and not "meta" in result
                and not "rules" in result
            ):
                raise MalformedResultsException(
                    "KVL(R)eporter received malformed results to process!"
                )
        return True

    #   #@pysnooper.snoop()
    def check_preconditions(self, *results: dict, dump: bool = False) -> bool:
        check_results, preconditions = {}, {
            "dump_file_path": self._check_dump_file_path,
            "kvle_results": self._check_kvle_results,
        }
        for check in preconditions:
            if check == "dump_file_path" and not dump:
                continue
            check_results.update({check: preconditions[check](*results)})
        return True

    #   #@pysnooper.snoop()
    def _dump_test_results_report_json(self, formatted_results, file_path):
        try:
            with open(file_path, "a") as json_file:
                json.dump(formatted_results, json_file, indent=4)
            print(f"[ INFO ]: KVL(R) test reports dumped to: {file_path}")
        except Exception as e:
            raise WriteFailureException(
                f"An error occurred while writing to the file: {e}"
            )
        return True

    # FORMATTERS

    def _format_validation_result(self, result: dict) -> list:
        builder = []
        for k in result:
            validation_report = {}
            if k not in ("source", "rules", "meta"):
                continue
            if k == "source":
                validation_report = {
                    "Source File Check": {
                        "FILES": result[k]["ok"] + result[k]["nok"],
                        "RESULT": "NOK" if result[k]["nok"] else "OK",
                    }
                }
            elif k == "meta":
                validation_report = {
                    "Module Metadata Check": {
                        "MODULES": result[k]["ok"] + result[k]["nok"],
                        "RESULT": "NOK" if result[k]["nok"] else "OK",
                    }
                }
            elif k == "rules":
                validation_report = {
                    "Module Constraint Rules Check": {
                        "MODULES": result[k]["ok"] + result[k]["nok"],
                        "RESULT": "NOK" if result[k]["nok"] else "OK",
                    }
                }
            builder.append(validation_report)
        return builder

    def _format_validation_report(self, *results: list) -> list:
        builder = []
        for result_dict in results:
            builder += self._format_validation_result(result_dict)
        return builder

    # ACTIONS

    #   #@pysnooper.snoop()
    def generate_report(self, *results: dict, dump: bool = False):
        """[ INPUT ]:

        [ RETURN ]:
        """
        check = self.check_preconditions(*results, dump=dump)
        formatted = self._format_validation_report(*results)
        if dump:
            dump_report = self._dump_test_results_report_json(
                formatted, self.dump_file_path
            )
        return formatted


# CODE DUMP

#           'Source File Check': {
#               "FILES": [
#                   {
#                       "path": "./src/modules/mymodule.py",
#                       "errors": [],
#                       "result": "OK"
#                   },
#                   {
#                       "path": "./src/modules/myothermoduleIforgotabout.py",
#                       "errors": [
#                           {
#                               "line": 13,
#                               "msg": "We don't do that here",
#                               "code": "KVL-11"
#                           }
#                       ]
#                       "result": "NOK",
#                   }
#               ],
#               "RESULT": "NOK",
#           },

#           'Module Metadata': {
#               "MODULES": {
#                   "Dummy1": {
#                       "package": 'dummy_module',
#                       "meta": {
#                           "VERSION": {
#                               "required": true,
#                               "set": true,
#                               "valid": true,
#                               "value": "1.0.1"
#                           },
#                           "CATEGORY": {
#                               "required": true,
#                               "set": true,
#                               "valid": true,
#                               "value": "INDICATOR"
#                           },
#                           "TYPE": {
#                               "required": true,
#                               "set": true,
#                               "valid": false,
#                               "value": "NotAValidType"
#                           }
#                       },
#                       "errors": ["TYPE"],
#                       "result": "NOK"
#                   }
#               },
#               "RESULT": "NOK"
#           },

#           'Module Constraint Rules Check': {
#               "MODULES": {
#                   "Dummy1": {
#                       "package": 'dummy_module',
#                       "function": "main",
#                       "rules": [
#                           {
#                               "name": "Large Window Rule",
#                               "verb": "gte",
#                               "args": ["window", "data.length"]
#                           },
#                           {
#                               "name": "Single Data Point",
#                               "verb": "eq",
#                               "rule": ["window", 1]
#                           }
#                       ],
#                       "errors": [],
#                       "result": "OK"
#                   }
#               },
#               "RESULT": "OK"
#           },
#       }


#           - *results: [{
#               'meta': {
#                   'ok': [{
#                       'package': 'dummy_package',
#                       'module': 'Dummy1',
#                       'version': {
#                           'required': True,
#                           'set': True,
#                           'valid': True,
#                           'value': '1.0.1',
#                       },
#                       'category': {
#                           'required': True,
#                           'set': True,
#                           'valid': True,
#                           'value': 'INDICATOR',
#                       },
#                       'type': {
#                           'required': True,
#                           'set': True,
#                           'valid': False,
#                           'value': 'NotAValidType'
#                       },
#                   }],
#                   'nok': {}

#               'source': [{
#                   'path': './src',
#                   'errors': [],
#                   'result': 'OK',
#               }],

#               'rules': [{
#                   'package': 'dummy_package',
#                   'module': 'Dummy1',
#                   'functions': {
#                       'main': [{
#                           'name': 'Large Window Rule',
#                           'verb': 'gte',
#                           'rule': ['window', 'data.length']
#                       },
#                       {
#                           'name': 'Single Data Point',
#                           'verb': 'eq',
#                           'rule': ['single_window', 1],
#                       }],
#                   },
#               }],
#               }]
