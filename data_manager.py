import openpyxl
import requests


class DataManager:
    @staticmethod
    def download_file(url: str, filename: str):
        request = requests.get(url)

        with open(filename, 'wb') as output:
            output.write(request.content)

    @staticmethod
    def extract_data(filename):
        dataframe = openpyxl.load_workbook(filename)
        dataframe1 = dataframe.active

        data_dict = {}
        for col in dataframe1.iter_cols():
            if col[0].value is not None:
                data_dict[col[0].value.strip()] = []

        for col in dataframe1.iter_cols():
            if col is None:
                break
            for row in range(1, dataframe1.max_row):
                if col[row].value is None:
                    break
                data_dict[col[0].value.strip()].append(col[row].value)

        return data_dict
