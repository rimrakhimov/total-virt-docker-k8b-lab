import time

import simplejson as json
import logging

import psycopg2

from task_one.task_one_exec import TaskOne
from task_two.task_two_exec import TaskTwo


log = logging.getLogger(__name__)


class TaskManager(object):

    def __init__(self, producer, database_config):
        log.info("Start initialization")

        atomic_processors = {
		    'Type_One': TaskOne,
		    'Type_Two': TaskTwo,
        }

        self.processors = {**atomic_processors}
        self.producer = producer

        self.db_config = database_config
        while (True):
            try:
                self._initialize_database()
                break
            except (Exception) as error:
                print(error)
                time.sleep(30)
        log.info("Finish initialization")

    @staticmethod
    def default_behavior(task: dict, processors, producer, db_config) -> None:
        result = processors[task['type']].run(task['body'], db_config)

        producer.publish(json.dumps(result))

    def execute(self, task):
        if (type(task) is bytes):
            task = task.decode("utf-8").replace("'", '"')
        try:
            if type(task) == str:
                task = json.loads(task)
            self.default_behavior(task, self.processors, self.producer, self.db_config)
        except Exception:
            log.info("CANNOT PARSE TASK {0}".format(task))
        log.info("TASK")
        log.info(task)

    def _initialize_database(self):
        commands = (
            """
            CREATE TABLE type1 (
                id SERIAL PRIMARY KEY,
                message VARCHAR(1000)
            );
            """,
            """
            CREATE TABLE type2 (
                id SERIAL PRIMARY KEY,
                message VARCHAR(1000)
            );
            """
        )
        conn = None
        try:
            conn = psycopg2.connect(
                host=self.db_config['host'],
                port=self.db_config['port'],
                database=self.db_config['database'],
                user=self.db_config['login'],
                password=self.db_config['password']
            )
            cur = conn.cursor()
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


