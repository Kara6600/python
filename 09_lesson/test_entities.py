import pytest
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://Kara:123@localhost:5432/qa"


@pytest.fixture(scope='function')
def db_connection():
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    yield conn
    conn.close()


def test_add_entity(db_connection):
    # Предположим, есть таблица users
    # Вставляем новую запись
    db_connection.execute(
        "INSERT INTO users (name) VALUES ('Test User')"
    )
    # Проверяем, что добавлена
    result = db_connection.execute(
        "SELECT COUNT(*) FROM users WHERE name='Test User'"
        )
    count = result.scalar()
    assert count == 1
    # Удаляем
    db_connection.execute(
        "DELETE FROM users WHERE name='Test User'"
        )


def test_update_entity(db_connection):
    # Предварительно добавляем запись
    db_connection.execute("INSERT INTO users (name) VALUES ('Old Name')")
    # Обновляем
    db_connection.execute(
        "UPDATE users SET name='New Name' WHERE name='Old Name'"
        )
    # Проверяем
    result = db_connection.execute(
        "SELECT name FROM users WHERE name='New Name'"
        )
    assert result.fetchone() is not None
    # Очистка
    db_connection.execute("DELETE FROM users WHERE name='New Name'")


def test_delete_entity(db_connection):
    # Предварительно добавляем
    db_connection.execute("INSERT INTO users (name) VALUES ('To Delete')")
    # Удаляем
    db_connection.execute("DELETE FROM users WHERE name='To Delete'")
    # Проверяем
    result = db_connection.execute(
        "SELECT * FROM users WHERE name='To Delete'"
        )
    assert result.fetchone() is None
