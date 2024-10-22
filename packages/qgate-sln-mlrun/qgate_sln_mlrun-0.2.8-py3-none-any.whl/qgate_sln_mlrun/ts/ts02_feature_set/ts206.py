"""
  TS206: Create feature set(s) & Ingest from Kafka source (one step)
"""
from qgate_sln_mlrun.ts.tsbase import TSBase
import mlrun
import mlrun.feature_store as fstore
from mlrun.data_types.data_types import ValueType
from mlrun.datastore.sources import KafkaSource
import json
from qgate_sln_mlrun.helper.kafkahelper import KafkaHelper
import os
import glob
from qgate_sln_mlrun.helper.featuresethelper import FeatureSetHelper


class TS206(TSBase):

    def __init__(self, solution):
        super().__init__(solution, self.__class__.__name__)
        self._kafka = KafkaHelper(self.setup)
        self._fshelper = FeatureSetHelper(self._solution)

    @property
    def desc(self) -> str:
        return "Create feature set(s) & Ingest from Kafka source (one step)"

    @property
    def long_desc(self):
        return ("Create feature set(s) & Ingest from Kafka source (one step, without save and load featureset)")

    def prj_exec(self, project_name):
        """ Create featuresets & ingest"""

        # It can be executed only in case that configuration is fine
        if not self._kafka.configured:
            return

        for featureset_name in self.get_featuresets(self.project_specs.get(project_name)):
            # Create shared topic as data source
            # TODO: drop_if_exist=False plus Remove content in case of project delete
            self._kafka.create_insert_data(self._kafka.create_helper(featureset_name), featureset_name,True)

            definition = self._fshelper.get_definition(project_name, featureset_name)
            if definition:
                self._create_featureset(f'{project_name}/{featureset_name}', project_name, featureset_name, definition, self.name)

    @TSBase.handler_testcase
    def _create_featureset(self, testcase_name, project_name, featureset_name, definition, featureset_prefix=None):
        # Create feature set
        featureset = self._fshelper.create_featureset(project_name, definition, featureset_prefix)

        # samples
        #  https://github.com/mlrun/test-notebooks/tree/main/kafka_redis_fs
        #  https://docs.mlrun.org/en/latest/feature-store/sources-targets.html#id1

        # fstore.ingest(featureset,
        #               KafkaSource(brokers=self.setup.kafka,
        #                         topics=[self._kafka.create_helper(featureset_name)]),
        #               # overwrite=False,
        #               return_df=False,
        #               # infer_options=mlrun.data_types.data_types.InferOptions.Null)
        #               infer_options=mlrun.data_types.data_types.InferOptions.default())
