import datetime
import json
import logging
import os

import pysnooper
from kaya_module_sdk.src.exceptions.malformed_results import \
    MalformedResultsException
from kaya_module_sdk.src.exceptions.write_failure import WriteFailureException

log = logging.getLogger(__name__)


class KITR:
    """[ KIT(R)eporter ]: Responsibilities -

    * Processes and formats results received from KIT(E)
    * Generates JSON report dump file if specified
    """

    report: dict
    context: dict
    dump_file_path: str

    def __init__(self, dump_file=None, **kwargs) -> None:
        self.report = {}
        self.context = kwargs
        self.dump_file_path = dump_file or "kit.report"

    # @pysnooper.snoop()
    def _check_dump_file_path(self) -> bool:
        directory = os.path.dirname(self.dump_file_path)
        if not directory:
            directory = "."
        # Check if the directory is indeed a directory
        if (
            not os.path.exists(directory)
            or not os.path.isdir(directory)
            or not os.access(directory, os.W_OK)
        ):
            raise WriteFailureException(
                "KIT(R)eporter dump file {self.dump_file_path} has an unexistent "
                "parent directory or location restricts write permissions."
            )
        return True

    # @pysnooper.snoop()
    def _check_test_result_structure(self, result: dict) -> bool:
        if not len(result["ok"]) and not len(result["nok"]):
            raise MalformedResultsException(
                "KIT test execution results are malformed! Details: {result}"
            )
        return True

    # @pysnooper.snoop()
    def check_preconditions(self, *results: dict, dump: bool = False) -> bool:
        check_results, preconditions = {}, {
            "general": {
                "dump_file_path": self._check_dump_file_path,
            },
            "test_specific": {
                "test_result_structure": self._check_test_result_structure,
            },
        }
        for check in preconditions["general"]:
            if check == "dump_file_path" and not dump:
                continue
            check_results.update({check: preconditions["general"][check]()})
        for result in results:
            for check in preconditions["test_specific"]:
                check_results.update(
                    {check: preconditions["test_specific"][check](result)}
                )

    # @pysnooper.snoop()
    def _dump_test_results_report_json(self, formatted_results, file_path):
        try:
            with open(file_path, "a") as json_file:
                json.dump(formatted_results, json_file, indent=4)
            print(f"[ INFO ]: KIT(R) test reports dumped to: {file_path}")
        except Exception as e:
            raise WriteFailureException(
                f"An error occurred while writing to the file: {e}"
            )
        return True

    # @pysnooper.snoop()
    def _format_test_execution_report(self, *results):
        formatted, nok_flag = {}, False
        for test_result in results:
            if test_result["nok"] and not nok_flag:
                nok_flag = True
            for conclusion in ("ok", "nok"):
                for test_name in test_result[conclusion].keys():
                    formatted.update(
                        {test_name: test_result[conclusion][test_name]["definition"]}
                    )
                    formatted[test_name].update(
                        {
                            "return": test_result[conclusion][test_name]["result"][
                                "response"
                            ],
                            "errors": test_result[conclusion][test_name]["result"][
                                "errors"
                            ],
                            "result": test_result[conclusion][test_name]["definition"][
                                "result"
                            ]
                            or "NOK",
                        }
                    )
        return {
            "TESTS": formatted,
            "TIMESTAMP": str(datetime.datetime.now()),
            "RESULT": "NOK" if nok_flag else "OK",
        }

    # @pysnooper.snoop()
    def generate_report(self, *results: dict, dump: bool = False):
        check = self.check_preconditions(*results, dump=dump)
        formatted = self._format_test_execution_report(*results)
        if dump:
            dump_report = self._dump_test_results_report_json(
                formatted, self.dump_file_path
            )
        return formatted
