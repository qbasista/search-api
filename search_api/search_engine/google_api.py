from googleapiclient.discovery import build
from .models import Query
from .helpers import get_client_ip


class GoogleServiceError(Exception):
    pass


class GoogleService:

    def __init__(self, developer_key, cse_id, name='customsearch', version='v1',):
        self.name = name
        self.version = version
        self.developer_key = developer_key
        self.cse_id = cse_id
        self.service = build(self.name, self.version,
                             developerKey=self.developer_key)

    def search(self, query):
        try:
            return self.service.cse().list(q=query, cx=self.cse_id).execute()
        except GoogleServiceError as e:
            raise GoogleServiceError('Can\'t search in Google') from e

    def save_query(self, res, query, ip):
        try:
            total_result = int(res["searchInformation"]['totalResults'])

            query = Query(
                name=query,
                total_result=total_result,
                client_ip=ip
            )
            query.save()

            if total_result and hasattr(res, 'items'):

                for num, item in enumerate(res['items'], start=1):
                    query.items.create(
                        position=num,
                        link=item['link'],
                        title=item['title'],
                        desc=item['snippet'],
                    )
            return query
        except Exception as e:
            raise GoogleServiceError('Can\'t save query to database') from e
