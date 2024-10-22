from qgate_sln_mlrun.ts.tshelper import TSHelper
from qgate_sln_mlrun.ts.tsbase import TSBase
import mlrun.feature_store as fstore
from mlrun.features import Feature
from mlrun.datastore.targets import RedisNoSqlTarget, ParquetTarget, CSVTarget, SQLTarget, KafkaTarget
import sqlalchemy
import os
import glob
import json


class FeatureSetHelper(TSBase):
    """Create featureset based on json definition"""

    def __init__(self, solution):
        super().__init__(solution, self.__class__.__name__)

    def get_definition(self, project_name, featureset_name):
        # create full path for featureset definition
        source_file = os.path.join(os.getcwd(),
                                   self.setup.model_definition,
                                   "01-model",
                                   "02-feature-set",
                                   f"*-{featureset_name}.json")

        for file in glob.glob(source_file):
            # find relevant featureset file
            if os.path.isfile(file):
                return file
        return None

    def create_featureset(self, project_name, definition, featureset_prefix=None):
        with open(definition, "r") as json_file:
            json_content = json.load(json_file)
        name, desc, lbls, kind = TSBase.get_json_header(json_content)

        if kind == "feature-set":
            return self._create_featureset_content(project_name,
                                           f"{featureset_prefix}_{name}" if featureset_prefix else name,
                                           desc,
                                           json_content['spec'])
        return None

    def _create_featureset_content(self, project_name, featureset_name, featureset_desc, json_spec):
        """
        Create featureset based on json spec

        :param project_name:        project name
        :param featureset_name:     feature name
        :param featureset_desc:     feature description
        :param json_spec:   Json specification for this featureset
        :return:            New (created) feature set
        """

        project_spec = self.project_specs.get(project_name, None)
        self.project_switch(project_name)
        fs = fstore.FeatureSet(
            name=featureset_name,
            description=featureset_desc
        )

        # define entities
        for item in json_spec['entities']:
            fs.add_entity(
                name=item['name'],
                value_type=TSHelper.type_to_mlrun_type(item['type']),
                description=item['description']
            )

        # define features
        for item in json_spec['features']:
            fs.add_feature(
                name=item['name'],
                feature=Feature(
                    value_type=TSHelper.type_to_mlrun_type(item['type']),
                    description=item['description']
                )
            )

        # define targets
        count=0
        target_providers=[]

        for target in project_spec["targets"]:
            target = target.lower().strip()

            # add target
            if len(target) == 0:  # support bypass: switch empty targets
                continue
            target_provider = self._create_target(target, f"trg_{count}", featureset_name, project_name, json_spec)
            if target_provider:
                target_providers.append(target_provider)
            count += 1
        fs.set_targets(target_providers, with_defaults=False)

        fs.save()
        return fs

    def _create_target(self, target, target_name, featureset_name, project_name, json_spec):

        target_provider=None
        if target == "parquet":
            # support more parquet targets (each target has different path)
            target_provider = ParquetTarget(name=target_name,
                                          path=os.path.join(self.setup.model_output, project_name, target_name))
        elif target == "csv":
            # ERR: it is not possible to use os.path.join in CSVTarget because issue in MLRun
            # pth="/".join(self.setup.model_output, project_name, target_name, target_name + ".csv")
            target_provider = CSVTarget(name=target_name,
                                        path="/".join([self.setup.model_output, project_name, target_name,
                                                      target_name + ".csv"]))
        elif target == "redis":
            if self.setup.redis:
                target_provider = RedisNoSqlTarget(name=target_name, path=self.setup.redis)
            else:
                raise ValueError("Missing value for redis connection, see 'QGATE_REDIS'.")

        elif target == "mysql":
            if self.setup.mysql:
                # mysql+<dialect>://<username>:<password>@<host>:<port>/<db_name>
                # mysql+pymysql://testuser:testpwd@localhost:3306/test

                # TODO: add featureset name
                tbl_name = f"{project_name}_{featureset_name}_{target_name}r"

                # TODO: create table as work-around, because create_table=True does not work for Postgres, only for MySQL
                # self._createtable(self.setup.mysql, tbl_name, json_spec)

                sql_schema, primary_key=self._get_sqlschema(json_spec)
                target_provider = SQLTarget(name=target_name, db_url=self.setup.mysql, table_name=tbl_name,
                                            schema=sql_schema,
                                            if_exists="replace",
                                            create_table=True,
                                            primary_key_column=primary_key,
                                            varchar_len=250)
            else:
                raise ValueError("Missing value for mysql connection, see 'QGATE_MYSQL'.")
        elif target == "postgres":
            if self.setup.postgres:
                # postgresql+<dialect>://<username>:<password>@<host>:<port>/<db_name>
                # postgresql+psycopg2://testuser:testpwd@localhost:5432/test

                tbl_name = f"{project_name}_{target_name}"

                # TODO: create table as work-around, because create_table=True does not work for Postgres, only for MySQL
                #self._createtable(self.setup.postgres, tbl_name, json_spec)

                sql_schema, primary_key=self._get_sqlschema(json_spec)
                target_provider = SQLTarget(name=target_name, db_url=self.setup.postgres, table_name=tbl_name,
                                            schema=sql_schema,
                                            if_exists="replace",
                                            create_table=True,
                                            primary_key_column=primary_key)
            else:
                raise ValueError("Missing value for mysql connection, see 'QGATE_POSTGRES'.")
        elif target == "kafka":
            if self.setup.kafka:
                # NOTE: The topic name is combination of project name , feature name and target
                target_provider = KafkaTarget(name=target_name,
                                              bootstrap_servers=self.setup.kafka,
                                              path=f"{project_name}_{featureset_name}_{target_name}")
            else:
                raise ValueError("Missing value for kafka connection, see 'QGATE_KAFKA'.")
        else:
            # TODO: Add support for other targets
            raise NotImplementedError()
        return target_provider

    def _get_sqlschema(self, json_spec):
        schema = {}
        for item in json_spec['entities']:
            schema[item['name']] = TSHelper.type_to_type(item['type'])
        for item in json_spec['features']:
            schema[item['name']] = TSHelper.type_to_type(item['type'])
        return schema, json_spec['entities'][0]['name']

    def _createtable(self, db_url, table_name, json_spec):
        # https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e

        engine = sqlalchemy.create_engine(db_url, echo=False)
        meta = sqlalchemy.MetaData()

        # create table definition
        tbl=sqlalchemy.Table(table_name, meta)
        # create primary keys
        for item in json_spec['entities']:
            tbl.append_column(
                sqlalchemy.Column( item['name'],TSHelper.type_to_sqlalchemy(item['type']), primary_key=True))
        # create columns
        for item in json_spec['features']:
            tbl.append_column(
                sqlalchemy.Column(item['name'], TSHelper.type_to_sqlalchemy(item['type'])))

        # create table
        meta.create_all(engine)
