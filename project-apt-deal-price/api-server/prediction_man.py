import numpy as np
import pandas as pd
import joblib
from dataframe_selector import DataFrameSelector


class predictionMan:
    def __init__(self):
        # models = {'강원도' : ['gw', gw_sub_region, gw_default, model], ..}
        self.models =  {}

        for idx, re in enumerate(region_table[:-1]):
            model = joblib.load(f'models/{re[1]}_region.pkl')
            self.models[re[0]] = [re[1], all_sub_region[idx], all_default[idx], model]

        # self.applyHomes 분양, 예측 가격 비교
        self.apply_home = pd.read_csv('models/apply_home_2020_ex.csv')

        self.region_dict = { r[0]:r[1] for r in region_table }

        print('init predictionMan')


    def predict_price(self, region, region_sub=None, pyung=None):
        model = self.models.get(region)

        if model == None:
            return 0

        features = model[2]

        if (region_sub != None) and (region_sub in model[1]):
            features[0]['region_sub'] = region_sub

        if pyung != None:
            features[0]['pyung'] = pyung

        features_df = pd.DataFrame.from_records(features)
        print(features_df)
        price = model[3].predict(features_df)

        result = {'region':region, 'regionSub':features_df['region_sub'].values[0],
                  'pyung':features_df['pyung'].values[0], 'price':int(price.round()[0])}

        return result


    def predict_price_all(self, region, pyung=None):
        model = self.models.get(region)

        if model == None:
            return 0

        sub_regions = model[1]
        features = model[2]

        if pyung != None:
            features[0]['pyung'] = pyung

        result_list = []
        for sub in sub_regions:
            features[0]['region_sub'] = sub

            features_df = pd.DataFrame.from_records(features)
            price = model[3].predict(features_df)

            result = {'region':region, 'regionSub':features_df['region_sub'].values[0],
                      'pyung':features_df['pyung'].values[0], 'price':int(price.round()[0])}

            result_list.append(result)

        result_list = sorted(result_list, key=lambda r: r['price'], reverse=True)
        return result_list


    def get_apply_home(self, region='전국', is_pyung=False):
        chk_region = self.region_dict.get(region)
        home_df = self.apply_home

        if chk_region != None and chk_region != 'all':
            bool_mat = home_df['지역'] == region
            home_df = home_df[bool_mat]

        pyung_cols = [
            '공급위치','건설사','아파트명','전용면적','평',
            '평당 분양가격','평당 예측가격','평당 분양-예측','평당 분양/예측%'
        ]
        not_pyung_cols = [
            '공급위치','건설사','아파트명','전용면적','평',
            '분양가격','예측가격','분양-예측','분양/예측%'
        ]
        home_df = home_df[pyung_cols if is_pyung else not_pyung_cols]

        converted_cols = [
            'region', 'constFirm', 'aptName', 'area', 'pyung',
            'applyPrice', 'predPrice', 'delta', 'percent'
        ]
        home_df.columns = converted_cols

        return home_df.to_dict('records')


region_table = [
    ('강원도','gw'), ('경기도','gg'), ('경상남도','gsn'),
    ('경상북도','gsb'), ('광주광역시','gj'), ('대구광역시','dg'),
    ('대전광역시','dj'), ('부산광역시','bs'), ('서울특별시','so'),
    ('세종특별자치시','sj'), ('울산광역시','us'), ('인천광역시','ic'),
    ('전라남도','jrn'), ('전라북도','jrb'), ('제주특별자치도','jj'),
    ('충청남도','ccn'), ('충청북도','ccb'), ('전국','all')
]


gw_default = [{
    'region_sub': '원주시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gw_pop': 1540094, 'gg_pop': 13351891, 'gsb_pop': 2644001, 'ccb_pop': 1597936,
    'gw_re_ccsi': 110.0, 'gw_loan': 21721.7
}]

gg_default = [{
    'region_sub': '화성시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gg_pop': 13351891, 'so_pop': 9715429, 'ccn_pop': 2120692, 'gg_re_ccsi': 123.8,
    'gg_loan': 275491.3
}]

gsn_default = [{
    'region_sub': '김해시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'gsb_pop': 2644001, 'jrn_pop': 1853339, 'gsn_re_ccsi': 110.6,
    'gsn_loan': 57313.4
}]

gsb_default = [{
    'region_sub': '구미시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gw_pop': 1540094, 'gsn_pop': 3347637, 'gsb_pop': 2644001, 'ccb_pop': 1597936,
    'gsb_re_ccsi': 109.5, 'gsb_loan': 39039.1
}]

gj_default = [{
    'region_sub': '북구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gj_pop': 1454709, 'jrn_pop': 1853339, 'jrb_pop': 1808044, 'gj_re_ccsi': 108.3,
    'gj_loan': 26480.8
}]

dg_default = [{
    'region_sub': '달서구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'gsb_pop': 2644001, 'dg_pop': 2428022, 'dg_re_ccsi': 121.2,
    'dg_loan': 44604.4
}]

dj_default = [{
    'region_sub': '서구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'dj_pop': 1470225, 'sj_pop': 346217, 'ccn_pop': 2120692, 'ccb_pop': 1597936,
    'gj_re_ccsi': 108.3, 'dj_loan': 26862.0
}]

bs_default = [{
    'region_sub': '해운대구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'bs_pop': 3402776, 'so_pop': 9715429, 'us_pop': 1141362,
    'bs_re_ccsi': 112.1, 'bs_loan': 66776.8
}]

so_default = [{
    'region_sub': '노원구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gg_pop': 13351891, 'so_pop': 9715429, 'sj_pop': 346217, 'so_re_ccsi': 131.9,
    'so_loan': 336897.1
}]

sj_default = [{
    'region_sub': '세종특별자치도', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'so_pop': 9715429, 'sj_pop': 346217, 'ccn_pop': 2120692, 'ccb_pop': 1597936,
    'so_re_ccsi': 131.9, 'ccb_re_ccsi': 119.6, 'ccn_re_ccsi': 120.3, 'sj_loan': 8117.9
}]

us_default = [{
    'region_sub': '남구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'dg_pop': 2428022, 'bs_pop': 3402776, 'us_pop': 1141362,
    'us_re_ccsi': 116.1, 'us_loan': 21518.6
}]

ic_default = [{
    'region_sub': '부평구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gg_pop': 13351891, 'so_pop': 9715429, 'ic_pop': 2945565, 'ic_re_ccsi': 116.1,
    'ic_loan': 59575.8
}]

jrn_default = [{
    'region_sub': '순천시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'gj_pop': 1454709, 'jrn_pop': 1853339, 'jrn_re_ccsi': 113.0,
    'jrn_loan': 24747.1
}]

jrb_default = [{
    'region_sub': '전주완산구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gsn_pop': 3347637, 'jrb_pop': 1808044, 'ccn_pop': 2120692, 'jrb_re_ccsi': 107.3,
    'jrb_loan': 26482.5
}]

jj_default = [{
    'region_sub': '제주시', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97,
    'dowjones': 25812.88, 'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6,
    'oil': 39.84, 'export': 39229801, 'import': 35597740, 'cpi_living': 104.88,
    'loan_interest_rate': 2.67, 'gg_pop': 13351891, 'so_pop': 9715429, 'jj_pop': 671913,
    'so_re_ccsi': 131.9, 'gg_re_ccsi': 123.8, 'jj_loan': 16286.1
}]

ccn_default = [{
    'region_sub': '천안서북구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'sj_pop': 346217, 'jrb_pop': 1808044, 'ccn_pop': 2120692, 'ccb_pop': 1597936,
    'ccn_re_ccsi': 120.3, 'ccn_loan': 34158.3
}]

ccb_default = [{
    'region_sub': '청주흥덕구', 'apt_floor': 5, 'period_completed': 0, 'pyung': 25.71,
    'kospi200': 280.09, 'kospi200construct': 189.47, 'kosdaq': 737.97, 'dowjones': 25812.88,
    'shanghai': 2984.67, 'exchange_rate': 1199.0, 'gold': 1793.6, 'oil': 39.84,
    'export': 39229801, 'import': 35597740, 'cpi_living': 104.88, 'loan_interest_rate': 2.67,
    'gw_pop': 1540094, 'gg_pop': 13351891, 'gsb_pop': 2644001, 'ccb_pop': 1597936,
    'ccb_re_ccsi': 119.6, 'ccb_loan': 23045.3
}]

all_default = [
    gw_default, gg_default, gsn_default, gsb_default, gj_default,
    dg_default, dj_default, bs_default, so_default, sj_default,
    us_default, ic_default, jrn_default, jrb_default, jj_default,
    ccn_default, ccb_default
]


gw_sub_region = [
    '강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군',
    '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군',
    '화천군', '횡성군'
]

gg_sub_region = [
    '가평군', '고양덕양구', '고양일산동구', '고양일산서구', '과천시', '광명시', '광주시', '구리시',
    '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남분당구', '성남수정구', '성남중원구',
    '수원권선구', '수원영통구', '수원장안구', '수원팔달구', '시흥시', '안산단원구', '안산상록구',
    '안성시', '안양동안구', '안양만안구', '양주시', '양평군', '여주시', '연천군', '오산시',
    '용인기흥구', '용인수지구', '용인처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시',
    '포천시', '하남시', '화성시'
]

gsn_sub_region = [
    '거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시',
    '의령군', '진주시', '창녕군', '창원마산합포구', '창원마산회원구', '창원성산구', '창원의창구',
    '창원진해구', '통영시', '하동군', '함안군', '함양군', '합천군'
]

gsb_sub_region = [
    '경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군',
    '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군',
    '울릉군', '울진군', '의성군', '청도군','청송군', '칠곡군', '포항남구', '포항북구'
]

gj_sub_region = [
    '광산구', '남구', '동구', '북구', '서구'
]

dg_sub_region = [
    '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'
]

dj_sub_region = [
    '대덕구', '동구', '서구', '유성구', '중구'
]

bs_sub_region = [
    '강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구',
    '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'
]

so_sub_region = [
    '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구',
    '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구',
    '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
]

sj_sub_region = [ '세종특별자치도' ]

us_sub_region = [
    '남구', '동구', '북구', '울주군', '중구'
]

ic_sub_region = [
    '강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '중구'
]

jrn_sub_region = [
    '강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시',
    '무안군', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군',
    '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'
]

jrb_sub_region = [
    '고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군',
    '익산시', '임실군', '장수군', '전주덕진구', '전주완산구', '정읍시', '진안군'
]

jj_sub_region = [ '서귀포시', '제주시' ]

ccn_sub_region = [
    '계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시',
    '서천군', '아산시', '예산군', '천안동남구', '천안서북구', '청양군', '태안군', '홍성군'
]

ccb_sub_region = [
    '괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군',
    '진천군', '청주상당구', '청주서원구', '청주청원구', '청주흥덕구', '충주시'
]

all_sub_region = [
    gw_sub_region, gg_sub_region, gsn_sub_region, gsb_sub_region, gj_sub_region,
    dg_sub_region, dj_sub_region, bs_sub_region, so_sub_region, sj_sub_region,
    us_sub_region, ic_sub_region, jrn_sub_region, jrb_sub_region, jj_sub_region,
    ccn_sub_region, ccb_sub_region
]


if __name__ == "__main__":
    pm = predictionMan()
    # print(pm.predict_price('강원도'))
    # print(pm.get_apply_home('강원도'))
    # print(pm.get_apply_home('서울특별시', is_pyung=True))
    result = pm.predict_price_all(region='서울특별시')
    print(result)


