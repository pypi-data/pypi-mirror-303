"""
  TS602: Get data from on-line feature vector(s)
"""

from qgate_sln_mlrun.ts.tsbase import TSBase
import mlrun.feature_store as fstore
import os
import json


class TS602(TSBase):

    def __init__(self, solution):
        super().__init__(solution, self.__class__.__name__)

    @property
    def desc(self) -> str:
        return "Get data from on-line feature vector(s)"

    @property
    def long_desc(self):
        return "Get data from on-line feature vector(s), focus on target Redis"

    def prj_exec(self, project_name):
        """
        Get data from on-line feature vector
        """
        # get information, about list of on-line vectors
        vectors = None
        if self.test_setting.get('vector'):
            if self.test_setting['vector'].get('online'):
                vectors = self.test_setting['vector']['online']

        if vectors:
            for featurevector_name in self.get_featurevectors(self.project_specs.get(project_name)):
                if featurevector_name in vectors:
                    self._get_data_online(f"{project_name}/{featurevector_name}", project_name, featurevector_name)

    @TSBase.handler_testcase
    def _get_data_online(self, testcase_name, project_name, featurevector_name):
        self.project_switch(project_name)
        vector = fstore.get_feature_vector(f"{project_name}/{featurevector_name}")

        # information for testing
        test_featureset, test_entities, test_features = self._get_test_setting(featurevector_name)

        # own testing
        test_sets = self._get_data_hint(featurevector_name, test_featureset)
        for test_data in test_sets:
            with vector.get_online_feature_service() as svc:
                entities = []
                itm = {}

                # prepare "query"
                for test_entity in test_entities:
                    itm[test_entity] = test_data[test_entity]
                entities.append(itm)

                resp = svc.get(entities, as_list=False)
                if len(resp) == 0:
                    raise ValueError("Feature vector did not return value.")
                else:
                    for feature_name in test_features:
                        # TODO: this conversion type can be removed in case InferOptions.Null (where types will be equal]
                        if isinstance(test_data[feature_name], str):
                            if str(resp[0][feature_name]) != test_data[feature_name]:
                                raise ValueError(f"Invalid value for '{feature_name}', expected '{test_data[feature_name]}' but "
                                                 f"got '{resp[0][feature_name]}'")
                        else:
                            if resp[0][feature_name] != test_data[feature_name]:
                                raise ValueError(f"Invalid value for '{feature_name}', expected '{test_data[feature_name]}' but "
                                                 f"got '{resp[0][feature_name]}'")

    def _get_test_setting(self, featurevector_name):
        # get information for testing (feature set, entities and features)
        test_detail=self.test_setting['vector']['tests'][featurevector_name]

        test_featureset = test_detail['feature-set']
        test_entities = test_detail['entities']
        test_features = test_detail['features']
        return test_featureset, test_entities, test_features

    def _get_data_hint(self, featurevector_name, test_featureset):
        # get data hint for testing
        file = os.path.join(os.getcwd(),
                                   self.setup.model_definition,
                                   "03-test",
                                   f"{self.setup.dataset_name}.json")

        with open(file, "r") as json_file:
            json_content = json.load(json_file)
            name, desc, lbls, kind = TSBase.get_json_header(json_content)

        test_sets=[]
        for test_set in json_content['spec']:
            if test_set.startswith("HintLast"):
                test_sets.append(json_content['spec'][test_set][test_featureset])
        return test_sets

