from .helpers import metastore_select

class Auth:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self):
        sql = f''' select * from users where user_username = '{self.username}' and user_password = '{self.password}' and user_is_active is True '''
        rows = metastore_select(sql)
        if not rows:
            return False
        return True

    def get_metastore_scripts(self):
        sql = f'''
        select 
            o.object_script 
        from objects o inner join objects_users ou on o.object_id = ou.object_id 
        inner join users u on ou.user_id = u.user_id 
        where 
            u.user_username = '{self.username}' and u.user_password = '{self.password}' and object_script is not null
        order by o.object_created_at asc
        '''
        return metastore_select(sql)