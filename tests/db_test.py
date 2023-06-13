import requests
import json
import pytest
import time


def test_each_lc_in_inventory(db_conn):

    select = f'''
                select i."type", i.state, i.lc_state,
                i.gtin_id, i.owner_id from public.item i
                where i.serial_number = 70
            '''

    with db_conn.cursor() as cursor:
        cursor.execute(select)
        select_result = cursor.fetchall()

    assert len(select_result) > 4