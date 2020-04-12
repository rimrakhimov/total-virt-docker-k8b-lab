import logging
import psycopg2

log = logging.getLogger(__name__)


class TaskTwo(object):

    @staticmethod
    def run(task, db_config):
        log.info("Started SECOND task")

        task_result = {}

        command = """
            INSERT INTO type1(message)
            VALUES (%s);
        """
        conn = None
        try:
            ## YOUR ALGORITHM HERE
            conn = psycopg2.connect(
                host=db_config['host'],
                port=db_config['port'],
                database=db_config['database'],
                user=db_config['login'],
                password=db_config['password']
            )
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(command, (task))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
            task_result["status"] = "Success"
        except Exception as e:
            log.error("Error running task: {0}".format(task))
            if conn is not None:
                conn.close()
            task_result["status"] = "Failed"
        else:
            pass
        return task_result

    @staticmethod
    def child_task_type(task):
        return '\n\n***\n\n'

    @staticmethod
    def has_child_task(task):
        return False

