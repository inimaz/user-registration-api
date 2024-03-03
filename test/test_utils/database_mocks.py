
from contextlib import contextmanager

class MockedCursor:
    def __init__(self) -> None:
        pass
    def execute(self, query, query_params):
        return query, query_params
    

class MockedDB:
    def __init__(self) -> None:
        pass
    @contextmanager
    def cursor(self):
        print('cursor called')
        yield MockedCursor()
    def commit(self):
        print('commit called')
        pass
    def close(self):
        print('close called')
        pass

@contextmanager
def override_get_db():
    try:
        db = MockedDB()
        yield db
    finally:
        db.close()