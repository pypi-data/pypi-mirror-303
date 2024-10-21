import panel as pn

# metastore database configurations
pg_username = 'postgres'
pg_password = 'PiIs&&&31415926535'
pg_server = 'localhost'
pg_database = 'postgres'
pg_port = '5432'

# spark configurations
spark_warehouse = '/home/morteza/Documents/Projects/letme/storage/spark-warehouse'

# max resources for each app
spark_max_memory = 20
spark_max_cpu_cores = 8

# config panel
def pn_setup():
    pn.extension('tabulator')
    pn.widgets.Tabulator.theme = 'simple'


