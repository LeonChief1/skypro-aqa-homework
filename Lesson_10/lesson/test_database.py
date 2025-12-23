from sqlalchemy import create_engine 
from sqlalchemy.sql import text


db_connection_string = "postgres://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'app_users'


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]

    assert row1[-1] == 1468
    assert row1["name"] == "YQQulyBxbm"


def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 1468).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "YQQulyBxbm"


# def test_select_1_row_with_two_filters():
#     db = create_engine(db_connection_string)
#     sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")
#     rows = db.execute(sql_statement, id = 1468, is_active = True).fetchall()

#     assert len(rows) == 4


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")
    my_params = {
        'id': 1468,
        'is_active': True
    }

    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 4


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, descr = 'New descr', id = 1704)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 1704)