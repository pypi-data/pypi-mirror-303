"""
  TS203: Create feature set(s) & Ingest from CSV source (one step)
"""
from qgate_sln_mlrun.ts.tsbase import TSBase
import mlrun
import mlrun.feature_store as fstore
from mlrun.data_types.data_types import ValueType
from mlrun.datastore.sources import CSVSource
import os
import glob
from qgate_sln_mlrun.helper.featuresethelper import FeatureSetHelper


class TS203(TSBase):

    def __init__(self, solution):
        super().__init__(solution, self.__class__.__name__)
        self._fshelper = FeatureSetHelper(self._solution)

    @property
    def desc(self) -> str:
        return "Create feature set(s) & Ingest from from CSV source (one step)"

    @property
    def long_desc(self):
        return ("Create feature set(s) & Ingest from from CSV source (one step, without save and load featureset)")

    def prj_exec(self, project_name):
        """ Create featuresets and ingest"""

        for featureset_name in self.get_featuresets(self.project_specs.get(project_name)):
            definition = self._fshelper.get_definition(project_name, featureset_name)
            if definition:
                self._create_featureset(f'{project_name}/{featureset_name}', project_name, featureset_name, definition, self.name)

    @TSBase.handler_testcase
    def _create_featureset(self, testcase_name, project_name, featureset_name, definition, featureset_prefix=None):
        # Create feature set
        featureset = self._fshelper.create_featureset(project_name, definition, featureset_prefix)

        source_file = os.path.join(os.getcwd(),
                                   self.setup.model_definition,
                                   "02-data",
                                   self.setup.dataset_name,
                                   f"*-{featureset_name}.csv.gz")
        for file in glob.glob(source_file):
            fstore.ingest(featureset,
                          CSVSource(name="tst", path=file),
                          # overwrite=False,
                          return_df=False,
                          # infer_options=mlrun.data_types.data_types.InferOptions.Null)
                          infer_options=mlrun.data_types.data_types.InferOptions.default())
            # TODO: use InferOptions.Null with python 3.10 or focus on WSL
            # NOTE: option default, change types
            # NOTE: option Null, generate error with datetime in python 3.9

