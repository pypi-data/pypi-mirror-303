import pymysql


class MysqlInstance:
    # 初始化方法，创建一个mysql连接
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cursor = None
        self.db = None

    def init_connect(self):
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.db.cursor()
        return self

    def save_table_sql(self, table_name: str, data: dict):
        """
        保存一条数据
        【demo】
        table_name = "user"
        data = {"name":"张三","age":18}
        :param table_name:表名
        :param data:字典数据
        :return:lastId
        """
        keys = data.keys()
        values = tuple(data.values())
        fields = "`,`".join(keys)
        temp = ",".join(["%s"] * len(keys))
        self.db.ping()
        sql = f"INSERT INTO `%s` (%s) VALUES (%s)" % (table_name, '`' + fields + '`', temp)
        self.cursor.execute(sql, values)
        self.db.commit()
        return self.cursor.lastrowid

    def update_table_sql(self, table_name: str, t_set: dict, t_where: dict):
        """
        更新一条数据
        【demo】
        table_name = "user"
        t_set = {"name":"张三","age":18}
        t_where = {"id":1}
        :param table_name:表名
        :param t_set:字典数据
        :param t_where:字典数据
        :return:受影响的行数
        """
        t_str = w_str = ''
        for key in t_set:
            t_str += "`{}`='{}',".format(key, str(t_set.get(key)).replace("'", "\\'"))
        t_str = t_str[:-1]
        for key in t_where:
            w_str += "`{}`='{}' and ".format(key, str(t_where.get(key)).replace("'", "\\'"))
        w_str = w_str[:-4]
        self.db.ping()
        sql = f"UPDATE `%s` set %s where %s" % (table_name, t_str, w_str)
        check = self.cursor.execute(sql)
        self.db.commit()
        return check
