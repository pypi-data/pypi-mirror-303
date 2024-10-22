# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@Author: xiaodong.li
@Time: 2/4/2021 2:47 PM
@Description: Description
@File: mysql_task.py
"""
import subprocess


class MysqlCommand(str):
    MYSQL = "mysql"
    MYSQLDUMP = "mysqldump"


class MysqlTask:

    def __init__(self, host, port, password, user, db=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db or ""

    def __mysql_task(self, sql_path, task_type, ignore_table=None):
        task_type_symbol = dict(mysql="<", mysqldump=">").get(task_type, None)
        if task_type_symbol is None:
            raise Exception("Task type symbol is illegal.")
        option = ""
        if task_type == MysqlCommand.MYSQLDUMP:
            option = "--set-gtid-purged=OFF"
            if ignore_table is not None:
                option += " " + MysqlOption(self.db).ignore_table(ignore_table)
        host = f"-h{self.host}"
        port = f"-P {self.port}"
        user = f"-u{self.user}"
        password = f"-p{self.password}"
        db = f'"{self.db}"'
        sql_path = f"\"{sql_path}\""
        cmd = " ".join([task_type, host, port, user, password, option, db, task_type_symbol, sql_path])
        exitcode, data = subprocess.getstatusoutput(cmd)
        if exitcode != 0:
            raise Exception(data)

    def _mysql_task(self, sql_path):
        return self.__mysql_task(sql_path, MysqlCommand.MYSQL)

    def _mysqldump_task(self, sql_path, ignore_table):
        return self.__mysql_task(sql_path, MysqlCommand.MYSQLDUMP, ignore_table)

    def mysql_task(self, sql_path):
        return self._mysql_task(sql_path)

    def mysqldump_task(self, sql_path, ignore_table=None):
        return self._mysqldump_task(sql_path, ignore_table)


class MysqlOption:

    def __init__(self, db):
        self.db = db

    def ignore_table(self, ignore_table):
        args = ["--ignore-table"]
        for table in ignore_table:
            args.append("{db}.{table}".format(db=self.db, table=table))
        return " ".join(args)
