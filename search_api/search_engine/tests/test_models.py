from django.test import TestCase
from search_engine.models import Query, Item

DESC = """Lorem Ipsum is simply dummy 
            text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard 
            dummy text ever since the 1500s, when an unknown 
            printer took a galley of type and scrambled it to make a 
            type specimen book. It has survived not only five centuries, 
            but also the leap into electronic typesetting, remaining essentially unchanged."""


class QueryTest(TestCase):

    def test_create_query(self):
        name = 'book'
        total_result = 1000

        q = Query(
            name=name,
            total_result=total_result,
        )
        q.save()
        item1 = q.items.create(
            position=1,
            link='https://www.some-link.com',
            title='some title',
            desc=DESC
        )
        item2 = q.items.create(
            position=2,
            link='https://some-link2.com',
            title='some title 2',
            desc=DESC
        )

        print(q.created)

        self.assertIsInstance(q, Query)
        self.assertIsInstance(item1, Item)
        self.assertIsInstance(item2, Item)
        self.assertEqual(q.name, name)
        self.assertEqual(q.total_result, total_result)
        self.assertEqual(len(q.items.all()), 2)
        self.assertTrue(hasattr(q, 'created'))
        self.assertEqual(str(q), f'{name} found {q.created}')
        self.assertEqual(str(item1), f'[1] some title')
