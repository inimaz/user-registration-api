from contextlib import contextmanager


class MockedCursor:
    def __init__(self) -> None:
        pass

    def execute(self, query, query_params=None):
        return query, query_params

    def fetchall(self):
        return [
            (
                1,
                "test@email.com",
                "$2b$12$SNEZNiJRv/i4fH8ttAzVU.5kPAhNM90Yq.zKVn5g5Pdy7qEsoYPR.",
                "1234",
                False,
            )
        ]

class MockedDB:
    def __init__(self) -> None:
        pass

    @contextmanager
    def cursor(self):
        print("cursor called")
        yield MockedCursor()

    def commit(self):
        print("commit called")

    def close(self):
        print("close called")


@contextmanager
def override_get_db():
    try:
        db = MockedDB()
        yield db
    finally:
        db.close()


# Same as above but used when the user is not found
class MockedNotFoundCursor:
    def __init__(self) -> None:
        pass

    def execute(self, query, query_params=None):
        return query, query_params

    def fetchall(self):
        raise Exception('User found')


class MockedDBNotFound:
    def __init__(self) -> None:
        pass

    @contextmanager
    def cursor(self):
        print("cursor called")
        yield MockedNotFoundCursor()

    def commit(self):
        print("commit called")

    def close(self):
        print("close called")