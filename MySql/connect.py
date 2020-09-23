import logging
import time

import pymysql


# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt='%Y-%m-%d %H:%M:%S %a'
#                     )


class DataBaseAccess(object):
    def __init__(self):
        self._host = 'rm-2zeeiu4k37a196nsxeo.mysql.rds.aliyuncs.com'
        self._port = 3306
        self._user = 'qweasd'
        self._password = 'ywl515816'
        self._db = 'python_pachong'

    def isConnect(self):
        self._conn = pymysql.connect(host=self._host,
                                     port=self._port,
                                     user=self._user,
                                     password=self._password,
                                     db=self._db,
                                     charset='utf8')

    def insertDatas(self, name):
        self.isConnect()
        cursor = self._conn.cursor()
        t = time.localtime()
        strftime = time.strftime('%Y-%m-%d %H:%M:%S', t)
        sql = 'insert into test(var,create_time) values("{}","{}")'.format(name, strftime)
        sql2 = 'insert into test(var,create_time) values(%s,%s)'
        list = [('abc', strftime), ('def', strftime)]
        try:
            cursor.executemany(sql2, list)
        except Exception as exception:
            logging.error(exception)
        finally:
            cursor.close()
            self._conn.commit()
            self._conn.close()

    def insertDatas2(self, dict):
        self.isConnect()
        cursor = self._conn.cursor()
        t = time.localtime()
        sql = 'insert into dangdang(`range`,image,title,recommend,author,times,price,createtime) ' \
              'values("{}","{}","{}","{}","{}","{}","{}",NOW())' \
            .format(dict.get("range"), dict.get("image"), dict.get("title"), dict.get("recommend"), dict.get("author"),
                    dict.get("times"), float(dict.get("price")))
        try:
            cursor.execute(sql)
        except Exception as exception:
            logging.error(exception)
        finally:
            cursor.close()
            self._conn.commit()
            self._conn.close()

    def insertDatasDouBan(self, list):
        self.isConnect()
        cursor = self._conn.cursor()
        sql = 'insert into douban(`rank`,title,image,author,content,score,create_time) ' \
              'values(%s,%s,%s,%s,%s,%s,NOW())'
        try:
            cursor.executemany(sql,list)
        except Exception as exception:
            logging.error(exception)
        finally:
            cursor.close()
            self._conn.commit()
            self._conn.close()


if __name__ == '__main__':
    DataBaseAccess().insertDatas('abc')
