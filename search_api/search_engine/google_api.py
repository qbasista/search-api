from googleapiclient.discovery import build
# from search_api.settings import env

# GOOGLE_API_KEY = env('GOOGLE_API_KEY')
# GOOGLE_CSE_ID = env('GOOGLE_CSE_ID')


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
