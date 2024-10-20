import logging
from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class CoefficientsRepository(MongoDBBaseRepository):
    DB_NAME = 'uefa'

    def __init__(self):
        super().__init__(self.DB_NAME)

    def insert_coefficients(self, coefficients):
        self.insert_document('coefficients', coefficients)
        logger.info('Inserted coefficients data')

    def upsert_many_coefficients(self, coefficients):
        self.bulk_upsert_documents('coefficients', coefficients)
        logger.info('Upsert coefficients data')

    def get_coefficients(self, season: int) -> dict:
        query = {'parameters.season': season}
        coefficients = self.find_document('coefficients', query)
        logger.info(f'Fetching coefficients for season {season}')
        return coefficients
