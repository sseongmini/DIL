import pandas, copy
import error

DataFrame = pandas.DataFrame

class Anonymity:
    def __init__(self, df:DataFrame, columns:list, k:int=10):
        try:
            if columns == []:
                raise error.ColumnsEmptyError
            else:
                self.columns = columns
        except Exception as e:
            return print('[Init Error]', e)

        try:
            if k < 1:
                raise error.KSizeError
            else:
                self.k = k
        except Exception as e:
            return print('[Init Error]', e)

        self.df = copy.deepcopy(df.loc[:, self.columns])

    def run(self):
        datas = list(set(map(tuple, self.df.values.tolist())))

        overlap = dict()
        for data in datas:
            overlap[data] = list(map(tuple, self.df.values.tolist())).count(data)

        return overlap

        


if __name__ == '__main__':
    excel = pandas.read_csv('../../../Sample/kTest_Full.csv', index_col=0)
    print('데이터 컬럼 >>>>', list(excel))

    test = Anonymity(excel, ['주소', '성별', '나이'])
    test.run()