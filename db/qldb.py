from logging import basicConfig, getLogger, INFO
from pyqldb.driver.qldb_driver import QldbDriver

logger = getLogger(__name__)
basicConfig(level=INFO)


class QldbQuery:
    def __init__(self):
        self.driver = QldbDriver(ledger_name='web-of-trust')

    @classmethod
    def call(cls):
        try:
            return cls().query_trust_records()
        except Exception as e:
            logger.exception('Error getting trust records.')
            raise e

    def query_trust_records(self):
        query = "SELECT * FROM Tests"
        cursor = self.driver.execute_lambda(lambda executor: executor.execute_statement(query))

        records = []

        for doc in cursor:
            records.append({'subject': doc["subject"],
                            'issuer': doc["issuer"],
                            'level': doc["level"]})

        return records


if __name__ == "__main__":
    records = QldbQuery.call()
    print(records)
