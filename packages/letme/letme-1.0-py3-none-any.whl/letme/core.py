from pyspark.sql import SparkSession
from delta import *
import pandas as pd
import getpass
import panel as pn

from .config import *
from .auth import *
from .helpers import *
from .gui import *
from .source.mssql import MSSQL

pn_setup()

class App:
    def __init__(self, username: str, password: str = None, spark_memory: int = 2, spark_cpu_cores: int = 1):
        self.spark_memory = spark_max_memory if spark_memory > spark_max_memory else spark_memory
        self.spark_cpu_cores = spark_max_cpu_cores if spark_cpu_cores > spark_max_cpu_cores else spark_cpu_cores
        self.username = username
        self.__password = getpass.getpass('Please enter your password: ') if not password else password
        self.user_id = None
        self.__spark = None
        self.__start()

        self.read = self.__spark.read
        self.createDataFrame = self.__spark.createDataFrame
        self.stop = self.__spark.stop

    def __start(self):
        if not Auth(self.username, self.__password).login():
            print('The username and/or password is incorrect. Make sure you have an account and it is activated.')
            return None
        self.spark_memory = f'{self.spark_memory}g'
        self.spark_cpu_cores = f'{self.spark_cpu_cores}'
        self.__set_user_id()
        self.__spark = self.__create_spark_session()

    def __set_user_id(self):
        sql = f''' select user_id from users where user_username = '{self.username}' and user_password = '{self.__password}'  '''
        self.user_id = metastore_select(sql)[0][0]

    def __create_spark_session(self):
        builder = SparkSession.builder.master(f'local[{self.spark_cpu_cores}]') \
            .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension') \
            .config('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog') \
            .config('spark.sql.warehouse.dir', spark_warehouse) \
            .config('spark.driver.memory', self.spark_memory) \
            .config('spark.driver.maxResultSize', self.spark_memory) \
            .config('spark.sql.repl.eagerEval.enabled', True) \
            .config('spark.databricks.delta.schema.autoMerge.enabled', True) \
            .config('spark.databricks.delta.autoCompact.enabled', True)
        return builder.getOrCreate()

    #######################################################################################################
    ## General methods
    #######################################################################################################

    def sql(self, script: str, gui: bool = False):
        try:
            output = self.__spark.sql(script)
        except:
            return 'Not found.'
        if identify_script_type(script) != 'other_script':
            metastore_save_script(self, script)

        df = output.toPandas()
        if not df.empty:
            if gui:
                return simple(output.toPandas())
            return output

    def load(self):
        rows = Auth(self.username, self.__password).get_metastore_scripts()
        for row in rows:
            try:
                self.__spark.sql(row[0])
            except:
                pass

    def list_objects(self, gui: bool = False):
        sql = f'''
        select distinct
            object_name,
            object_type,
            object_created_at
        from objects o inner join objects_users ou on o.object_id = ou.object_id 
        where ou.user_id = {self.user_id}
        '''
        df = pd.read_sql(sql, get_metastore_con())
        if gui:
            return simple(df)
        return df

    def drop_object(self, object_name: str):
        sql = f'''
        select object_id, object_type from objects o where object_name = '{object_name}' and object_owner_id = {self.user_id}
        '''
        row = metastore_select(sql)
        if not row:
            print('Object not found.')
            return
        object_id = row[0][0]
        object_type = row[0][1]

        try:
            self.__spark.sql(f'''drop {object_type} {object_name}''')
        except:
            pass
        sql = f'''
        delete from objects where object_id = {object_id}
        '''
        metastore_ciud(sql)

        sql = f'''
        delete from objects_users where object_id = {object_id}
        '''
        metastore_ciud(sql)

    #######################################################################################################
    ## Permissions and Access
    #######################################################################################################

    def give_permission(self, target_username: str, object_name: str):
        sql = f'''
        select
            distinct o.object_id
        from objects o inner join objects_users ou on o.object_id = ou.object_id
        where 
            o.object_owner_id = {self.user_id} and o.object_name = '{object_name}'
        '''
        row = metastore_select(sql)
        if row:
            object_id = row[0][0]
        else:
            print('You are not the owner of the Object and can not give permission on this object.')
            return

        sql = f''' select user_id from users u where user_username = '{target_username}' '''
        row = metastore_select(sql)
        if row:
            target_user_id = row[0][0]
        else:
            print('Target username not found!')
            return

        sql = f''' insert into objects_users (object_id, user_id) values ({object_id}, {target_user_id}) '''
        try:
            metastore_ciud(sql)
        except:
            pass

    def remove_permission(self, target_username: str, object_name: str):
        sql = f'''
        select * from objects where object_owner_id = {self.user_id} and object_name = '{object_name}' 
        '''
        row = metastore_select(sql)
        if not row:
            print('You are not the owner of this object and can not remove permission.')
            return

        sql = f'''
        select
            distinct ou.object_user_id
        from objects o inner join objects_users ou on o.object_id = ou.object_id
        inner join users u on u.user_id = ou.user_id 
        where 
            u.user_username = '{target_username}' and o.object_name = '{object_name}'
        '''
        row = metastore_select(sql)
        if row:
            sql = f'''delete from objects_users where object_user_id = {row[0][0]}'''
            metastore_ciud(sql)

    #######################################################################################################
    ## Add sources
    #######################################################################################################

    def add_mssql_source(
            self,
            source_name: str,
            server: str,
            database: str,
            username: str,
            password: str,
            port: int = 1433
    ):
        return MSSQL(
            app=self,
            source_name=source_name,
            server=server,
            database=database,
            username=username,
            password=password,
            port=port
        )

    #######################################################################################################
    ## Work with sources
    #######################################################################################################

    def find_source(self, source_name_like:str, gui: bool = False):
        sql = f'''
        select distinct
            object_name as source_name,
            object_created_at 
        from objects o inner join objects_users ou on ou.object_id = o.object_id 
        where o.object_type = 'source' and ou.user_id = {self.user_id} and o.object_name like '%{source_name_like}%' 
        '''
        df = pd.DataFrame(metastore_select(sql))
        if df.empty:
            return
        if gui:
            return simple(df)
        return df

    def load_source(self, source_name: str):
        sql = f'''
        select
            object_extra_info 
        from objects o inner join objects_users ou on ou.object_id = o.object_id 
        where o.object_type = 'source' and ou.user_id = 1 and o.object_name = '{source_name}'
        '''
        output = metastore_select(sql)
        if not output:
            print('Source not found.')
            return
        object_extra_info = output[0][0]
        if object_extra_info.get('source_type') == 'mssql':
            return self.add_mssql_source(
                source_name=object_extra_info.get('source_name'),
                server=object_extra_info.get('server'),
                database=object_extra_info.get('database'),
                username=object_extra_info.get('username'),
                password=object_extra_info.get('password'),
                port=object_extra_info.get('port')
            )
