from sqlalchemy import create_engine, text
from pathlib import Path
import re
from datetime import datetime

from .config import *

# get metastore sqlalchemy engine
def get_metastore_con():
    connection_string = f'postgresql://{pg_username}:{pg_password}@{pg_server}:{pg_port}/{pg_database}'
    return create_engine(connection_string, isolation_level='autocommit')

def metastore_ciud(script: str):
    engine = get_metastore_con()
    with engine.connect() as conn:
        conn.execute(text(script))

def metastore_select(script: str):
    engine = get_metastore_con()
    with engine.connect() as conn:
        return conn.execute(text(script)).fetchall()

# normalize the script
def normalize_script(script: str):
    script = script.replace('\n', ' ').strip().replace(';', '').replace('"', "'")
    new_words = [word.strip() for word in script.split(' ') if len(word.strip()) != 0]
    script = ' '.join(new_words)
    return f'{script} ;'

# get absolute path related to a given path
def get_absolute_path(system_path: str):
    return Path(system_path).resolve().__str__()

# create metastore entities
def initdb():
    sql = '''
    create table if not exists objects 
    ( 
        object_id serial primary key,
        object_type varchar(256),
        object_name varchar(256),
        object_owner_id int,
        object_location varchar(256),
        object_script text,
        object_extra_info json,
        object_created_at timestamp
    );
    
    create unique index if not exists objects_unique_type_name on objects (object_type, object_name);
    
    create unique index if not exists objects_unique_location on objects (object_location) where length(object_location) > 0;
    
    create table if not exists users 
    (
        user_id serial primary key, 
        user_username varchar(256), 
        user_password varchar(256),
        user_email varchar(256),
        user_is_active boolean default false
    );
    
    create unique index if not exists users_unique_username on users (user_username);
    
    insert into users (user_username, user_password, user_email, user_is_active) values ('admin', 'admin1234', '', True);
    
    insert into users (user_username, user_password, user_email, user_is_active) values ('testuser', 'testuser1234', '', True);
    
    
    create table if not exists objects_users 
    ( 
        object_user_id serial primary key, 
        user_id int, 
        object_id int 
    );
    
    create unique index if not exists objects_users_unique_persmission on objects_users (object_id, user_id);
    '''
    try:
        metastore_ciud(sql)
    except:
        pass

# identity the type of script user has entered
def identify_script_type(script: str):
    script = normalize_script(script).lower()
    patterns = {
        'create_table': r'^create\s(or replace\s)?table\s(if not exists\s)?.*\susing\sdelta\slocation\s.*\s;$',
        'create_view': r'^create\s(or replace\s)?view\s(if not exists\s)?.*\sas\sselect\s.*\s;$',
        'create_database': r'^create\sdatabase\s(if not exists\s)?.*\s;$'
    }
    for key, value in patterns.items():
        if re.match(value, script):
            return key
    return 'other_script'

# extract info from create table script
def __extract_info_from_create_table_script(script: str):
    start = script.lower().find(' using delta location ') + 21
    end = len(script.lower())
    table_location = script[start:end].replace(';', '').strip().replace("'", "")
    table_location = get_absolute_path(table_location)
    if ' if not exists ' in script.lower():
        start = script.lower().find(' if not exists ') + 14
    else:
        start = script.lower().find(' table ') + 6
    end = script.find('(')
    table_name = script[start:end].strip()
    return {
        'object_script': f'''{script}''',
        'object_type': 'table',
        'object_name': table_name,
        'object_location': table_location,
        'object_created_at': datetime.now()
    }

# extract info from create view script
def __extract_info_from_create_view_script(script: str):
    if ' if not exists ' in script.lower():
        start = script.lower().find(' if not exists ') + 14
    else:
        start = script.lower().find(' view ') + 5
    end = script.lower().find('as')
    view_name = script[start:end].strip()
    return {
        'object_script': f'''{script}''',
        'object_type': 'view',
        'object_name': view_name,
        'object_location': '',
        'object_created_at': datetime.now()
    }

# extract info from create database script
def __extract_info_from_create_database_script(script: str):
    db_name = script.replace(';', '').strip().split(' ')[-1]
    return {
        'object_script': f'''{script}''',
        'object_type': 'database',
        'object_name': db_name,
        'object_location': '',
        'object_created_at': datetime.now()
    }

# extract the info needed to save in the metastore
def __extract_info_from_user_script(script: str):
    script = normalize_script(script)
    script_type = identify_script_type(script)
    if script_type == 'create_table':
        return __extract_info_from_create_table_script(script)
    elif script_type == 'create_view':
        return __extract_info_from_create_view_script(script)
    elif script_type == 'create_database':
        return __extract_info_from_create_database_script(script)

# save the object to the metastore
def metastore_save_script(app ,script: str):
    info = __extract_info_from_user_script(script)
    data = [{
        'object_script': str(info.get('object_script')),
        'object_type': info.get('object_type'),
        'object_name': info.get('object_name'),
        'object_location': info.get('object_location'),
        'object_owner_id': app.user_id,
        'object_created_at': str(info.get('object_created_at'))
    }]
    sql = '''
         insert into public.objects (object_script, object_type, object_name, object_location, object_owner_id, object_created_at)
         values (:object_script, :object_type, :object_name, :object_location, :object_owner_id, :object_created_at) returning object_id
         '''
    engine = get_metastore_con()
    with engine.connect() as conn:
        object_id = conn.execute(text(sql), data).fetchone()[0]

    sql = f''' insert into objects_users (object_id, user_id) values ({object_id}, {app.user_id})'''
    metastore_ciud(sql)

def register_user():
    pass