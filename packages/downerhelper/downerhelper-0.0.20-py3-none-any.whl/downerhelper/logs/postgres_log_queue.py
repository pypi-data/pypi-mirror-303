import logging
import psycopg2 as pg
from datetime import datetime, timezone
from downerhelper.secrets import get_config_dict

class PostgresLogQueue():
    def __init__(self, logger_name, job_id, table, db_config):
        try:
            if '' in [logger_name, job_id, table] or \
                None in [logger_name, job_id, table] or db_config == {}:
                raise Exception("Invalid parameters")
            self.logger_name = logger_name
            self.job_id = job_id
            self.db_config = db_config
            self.table = table
            self.queue = [
                {
                    'levelname': 'INFO',
                    'message': f'queue: {logger_name} created for job_id: {job_id}',
                    'created_at': datetime.now(timezone.utc)
                }
            ]
        except Exception as e:
            logging.error(f"Error setting up PostgresLogHandler: {e}")
            raise e

    def add(self, levelname, message):
        self.queue.append({
            'levelname': levelname,
            'message': message,
            'created_at': datetime.now(timezone.utc)
        })

    def save(self):
        try:
            conn = pg.connect(**self.db_config)
            cursor = conn.cursor()
            cursor.execute("set time zone 'UTC'")
            cursor.execute(f"""
            create table if not exists {self.table} (
                id serial primary key,
                created_at timestamptz default now(),
                name varchar(255),
                levelname varchar(50),
                message text,
                job_id varchar(255) not null
            )""")
            conn.commit()
            
            for log in self.queue:
                cursor.execute(f"""
                insert into {self.table} (name, levelname, message, job_id, created_at)
                values (%s, %s, %s, %s, %s)
                """, (self.logger_name, log['levelname'], log['message'], self.job_id, log['created_at']))
            conn.commit()

            if cursor: cursor.close()
            if conn: conn.close()

            self.queue = []

        except Exception as e:
            logging.error(f"Error saving logs: {e}")
            if cursor: cursor.close()
            if conn: conn.close()

def setup_queue(logger_name, job_id, table, db_config_name, keyvault_url):
    try:
        db_config = get_config_dict(db_config_name, keyvault_url)
        return PostgresLogQueue(logger_name, job_id, table, db_config)
    except Exception as e:
        logging.error(f"Error setting up logger: {e}")
        raise Exception("Error setting up logger")