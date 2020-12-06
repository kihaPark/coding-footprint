from dataframe_selector import DataFrameSelector
import joblib

if __name__ == "__main__":
    region_table = [
        ('강원도','gw'), ('경기도','gg'), ('경상남도','gsn'),
        ('경상북도','gsb'), ('광주광역시','gj'), ('대구광역시','dg'),
        ('대전광역시','dj'), ('부산광역시','bs'), ('서울특별시','so'),
        ('세종특별자치시','sj'), ('울산광역시','us'), ('인천광역시','ic'),
        ('전라남도','jrn'), ('전라북도','jrb'), ('제주특별자치도','jj'),
        ('충청남도','ccn'), ('충청북도','ccb'), ('전국','all')
    ]

    for re in region_table[:-1]:
        model = joblib.load(f'models/{re[1]}_region.pkl')
        joblib.dump(model, f'models/{re[1]}_region.pkl')

