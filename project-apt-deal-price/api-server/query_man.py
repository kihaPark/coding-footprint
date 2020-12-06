import numpy as np
import pandas as pd
import cx_Oracle


def get_data_from_db(query, params):
    conn = cx_Oracle.connect('kiha', 'kiha', 'localhost:1521/xe')
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df

class queryMan:
    def __init__(self):
        print('queryMan init')

    def recent_deal_list(self, region='서울특별시'):
        query = """
            SELECT b.region||' '||b.region_sub address,
                b.apt_name aptname,
                b.completion_year completeyear,
                round(b.apt_size / 3.3, 2) pyung,
                b.apt_floor aptfloor,
                b.contract_price contractprice,
                to_char(b.contract_date, 'YYYY.MM.DD') contractdate
            FROM (SELECT *
                FROM apt_deal_price A
                WHERE A.region = :region
                ORDER BY A.contract_date DESC) b
            WHERE ROWNUM < 11
            """

        queD = get_data_from_db(query, params={'region':region})
        queD.columns = [
            'address', 'aptName', 'completeYear', 'pyung',
            'aptFloor', 'contractPrice', 'contractDate']

        return queD.to_dict('records')


if __name__ == "__main__":
    qm = queryMan()
    print(qm.recent_deal_list())

