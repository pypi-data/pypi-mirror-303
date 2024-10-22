
from qgate_sln_mlrun.output import Output
from qgate_sln_mlrun.setup import Setup
from enum import Enum
import mlrun
import os
import json
import logging


class TSState(Enum):
    NoExecution = 1
    DONE = 2
    ERR = 3

class TSType(Enum):
    OnLine = 1
    OffLine = 2
    Both = OnLine + OffLine

class TSBase:
    """
    Base class for all test scenarios
    """

    def __init__(self, solution, name: str):
        self._solution=solution
        self._name=name
        self._state = TSState.NoExecution
        self._logger = logging.getLogger("mlrun")

    @property
    def projects(self) -> list:
        return self._solution.projects

    @property
    def project_descs(self) -> dict:
        return self._solution._project_descs

    @property
    def project_specs(self) -> dict:
        return self._solution.project_specs

#region TEST_SETTING

    @property
    def test_setting(self) -> dict:
        return self._solution.test_setting

    @property
    def test_setting_vector(self) -> dict:
        return self._solution.test_setting["vector"]

#endregion

    @property
    def setup(self) -> Setup:
        return self._solution.setup

    @property
    def output(self) -> Output:
        return self._solution.output

    def handler_testcase(func):
        """Error handler for test case, mandatory arguments 'ts' and 'name'"""
        def wrapper(self, testcase_name: str, *args, **kwargs):

            try:
                self.testcase_new(testcase_name)
                ret=func(self, testcase_name, *args, **kwargs)
                self.testcase_state()
                return ret
            except Exception as ex:
                self.state = TSState.ERR
                self.testcase_detail(f"{type(ex).__name__}: {str(ex)}")
                self.testcase_state("ERR")
                return False
        return wrapper

    # region INTERNAL

    def get_project_target(self, project_spec, target):
        if project_spec:
            targets=project_spec.get("targets", None)
            if targets:
                return targets.get(target, None)
            return None

    def get_targets(self, project_spec):
        return project_spec.get("targets", {})

    def get_featuresets(self, project_spec):
        return project_spec.get("feature-sets",[])

    def get_featurevectors(self, project_spec):
        return project_spec.get("feature-vectors",[])

    def get_mlmodel(self, project_spec):
        return project_spec.get("ml-models", [])

    @staticmethod
    def get_json_header(json_content):
        """ Get common header

        :param json_content:    json content
        :return:                name, description, labeled, kind, parent from header
        """
        name = json_content['name']
        desc = json_content['description']
        kind = json_content['kind']

        # optional labels
        lbls = None if json_content.get('labels') is None else json_content.get('labels')
        return name, desc, lbls, kind

    @staticmethod
    def get_json_header_full(json_content):
        """ Get common header

        :param json_content:    json content
        :return:                name, description, labels, kind and parent from header
        """
        name = json_content['name']
        desc = json_content['description']
        kind = json_content['kind']
        parent = json_content.get('parent', None)

        # optional labels
        lbls = None if json_content.get('labels') is None else json_content.get('labels')
        return name, desc, lbls, kind, parent

    @staticmethod
    def get_model_info(model_definition):
        file = os.path.join(os.getcwd(),
                            model_definition,
                            "01-model",
                            "model.json")
        with open(file, "r") as json_file:
            json_content = json.load(json_file)
            name, desc, lbls, kind = TSBase.get_json_header(json_content)
            return json_content['spec']['version']
        return "n/a"

    def project_switch(self, project_name):
        # switch to proper project if the current project is different
        if mlrun.get_current_project().name != project_name:
            mlrun.load_project(name=project_name, context=os.path.join(self.setup.model_output,project_name), user_project=False)

    # endregion

    @property
    def desc(self):
        raise NotImplemented()

    @property
    def long_desc(self):
        raise NotImplemented()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, a):
        self._state = a

    @property
    def name(self):
        return self._name

    def before(self):
        """One call BEFORE exec all projects for specific TS. It is relevant for data preparation, etc."""
        pass

    def prj_exec(self, project_name):
        """Execution of TS for each project."""
        pass

    def exec(self):
        """Execution of TS."""
        pass

    def after(self):
        """One call AFTER execute all projects for specific TS. It is relevant for data cleaning, etc."""
        pass

    # region TEST_SCENARIOS
    def testscenario_new(self):
        self._logger.info(f"!! {self.name}: {self.desc} ...")
        self.output.testscenario_new(self.name, self.desc)

    def testcase_new(self, name):
        self._logger.info(f"  '{name}' ...")
        self.output.testcase_new(name)

    def testcase_detail(self, detail):
        self.output.testcase_detail(detail)

    def testcase_detailext(self, detail):
        self.output.testcase_detailext(detail)

    def testcase_state(self, state="DONE"):
        self.output.testcase_state(state)

    # endregion

