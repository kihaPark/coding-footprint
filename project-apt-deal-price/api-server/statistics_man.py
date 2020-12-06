import numpy as np
import pandas as pd

class statisticsMan:
    def __init__(self):
        # apply_homes = {0 : dataframe, ..}
        self.stat_dfs = {}
        for stat in stat_files:
            self.stat_dfs[stat[1]] = pd.read_csv(f'data-files/{stat[0]}')
        
        brands = ['자이', '힐스테이트', '래미안', '푸르지오', '롯데캐슬']
        brand_pyung_price = [8, 10, 12, 14, 16]
        brand_deal_count = [9, 11, 13, 15, 17]
        for idx, brand in zip(brand_pyung_price+brand_deal_count, brands+brands):
            self.stat_dfs[idx]['brand'] = brand

        self.region_dict = { r[0]:r[1] for r in region_table }

        print('init statisticsMan')


    def data_to_dict(self, id=0, region='전국'):
        chk_region = self.region_dict.get(region)
        stat = self.stat_dfs[id]

        if chk_region == None or chk_region == 'all':
            return stat.to_dict('records')

        return stat[stat['region'] == region].to_dict('records')


    def brand_apt_deal_count(self, region='서울특별시'):
        chk_region = self.region_dict.get(region)

        if chk_region == None or chk_region == 'all':
            region = '서울특별시'

        brands = []
        for id in [9, 11, 13, 15, 17]:
            stat = self.stat_dfs[id]
            bool_mat = stat['region'] == region
            brands.extend(stat[bool_mat].to_dict('records'))

        return brands


    def brand_apt_pyung_price(self, region='서울특별시'):
        chk_region = self.region_dict.get(region)

        if chk_region == None or chk_region == 'all':
            region = '서울특별시'

        brands = []
        for id in [8, 10, 12, 14, 16]:
            stat = self.stat_dfs[id]
            bool_mat = stat['region'] == region
            brands.extend(stat[bool_mat].to_dict('records'))

        return brands

    def compare_data(self, id=0, region1='서울특별시', region2='경기도'):
        compare = []
        compare.extend(self.data_to_dict(id=id, region=region1))
        compare.extend(self.data_to_dict(id=id, region=region2))

        return compare


stat_files = [
    ('region_deal_count.csv', 0),
    ('region_deal_count_month.csv', 1),
    ('region_avg_price_per_pyung.csv', 2),
    ('region_avg_price_per_pyung_month.csv', 3),

    ('region_size_deal_count.csv', 4),
    ('region_size_deal_count_month.csv', 5),
    ('region_size_avg_price_per_pyung.csv', 6),
    ('region_size_avg_price_per_pyung_month.csv', 7),

    ('xi_region_avg_price_per_pyung.csv', 8),
    ('xi_region_deal_count.csv', 9),
    ('healstate_region_avg_price_per_pyung.csv', 10),
    ('healstate_region_deal_count.csv', 11),
    ('raemian_region_avg_price_per_pyung.csv', 12),
    ('raemian_region_deal_count.csv', 13),
    ('prugio_region_avg_price_per_pyung.csv', 14),
    ('prugio_region_deal_count.csv', 15),
    ('lottecastle_region_avg_price_per_pyung.csv', 16),
    ('lottecastle_region_deal_count.csv', 17)
]

region_table = [
    ('강원도','gw'), ('경기도','gg'), ('경상남도','gsn'),
    ('경상북도','gsb'), ('광주광역시','gj'), ('대구광역시','dg'),
    ('대전광역시','dj'), ('부산광역시','bs'), ('서울특별시','so'),
    ('세종특별자치시','sj'), ('울산광역시','us'), ('인천광역시','ic'),
    ('전라남도','jrn'), ('전라북도','jrb'), ('제주특별자치도','jj'),
    ('충청남도','ccn'), ('충청북도','ccb'), ('전국','all')
]


if __name__ == "__main__":
    sm = statisticsMan()
    # print(sm.data_to_dict(region='전국'))
    print(sm.brand_apt_deal_count())
    print(sm.brand_apt_pyung_price())

