import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder


class SuicideDataset(Dataset):
    def __init__(self, data, target_col, static_variables, sequence_variables):
        """
        SuicideDataset 클래스 생성자.
        
        :param data: DataFrame 형태의 입력 데이터.
        :param target_col: 타겟 컬럼 이름.
        :param static_variables: 정적 변수 목록.
        :param sequence_variables: 시계열 변수 목록.
        """
        self.df = data
        self.target_col = target_col
        self.static_variables = static_variables
        self.sequence_variables = sequence_variables

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        target = row[self.target_col]
        static_data = row[self.static_variables].astype(np.float32)
        sequence_data = row[self.sequence_variables].astype(np.float32)
        return torch.tensor(static_data.values, dtype=torch.float32), torch.tensor(sequence_data.values, dtype=torch.float32), torch.tensor(target, dtype=torch.float32)

class DataHandler:
    def __init__(self, data=None, static_variables=None, sequence_variables=None):
        self.data = data
        self.static_variables = static_variables
        self.sequence_variables = sequence_variables

    def load_data(self, data_sources):
        if isinstance(data_sources, list):  # 리스트로 데이터가 들어올 경우
            dataframes = []
            for source in data_sources:
                if isinstance(source, pd.DataFrame):
                    dataframes.append(source)
                elif isinstance(source, str):
                    if source.endswith('.csv'):
                        # 데이터 로드 시 dtype 및 low_memory 옵션 사용
                        dataframes.append(pd.read_csv(source, dtype={'column_47': str}, low_memory=False))
                    elif source.endswith('.xlsx'):
                        dataframes.append(pd.read_excel(source))
            self.data = pd.concat(dataframes, ignore_index=True)
        elif isinstance(data_sources, pd.DataFrame):  # 하나의 DataFrame 객체가 들어올 경우
            self.data = data_sources
        else:
            raise ValueError("지원되지 않는 데이터 소스 형식입니다.")


    def preprocess_data(self):
        """
        데이터 전처리 함수.
        
        :return: 전처리된 DataFrame.
        """
        if self.data is None:
            raise ValueError("데이터가 없습니다. 데이터를 로드하거나 제공해야 합니다.")

        # 'sex' 칼럼의 데이터 유형을 문자열로 변환
        if 'sex' in self.data.columns:
            self.data['sex'] = self.data['sex'].astype(str)  # 또는 필요한 경우 int로 변환

        # 숫자형 변수 스케일링
        numeric_features = self.data.select_dtypes(include=[np.number]).columns.tolist()
        scaler = MinMaxScaler(feature_range=(-1, 1))
        self.data[numeric_features] = scaler.fit_transform(self.data[numeric_features])
                    
            ## LabelEncoder를 사용하여 범주형 변수를 숫자형으로 변환
        label_encoders = {}
        columns_to_encode = ['DIG_cat', 'DIG_text', 'occu', 'relig', 'place', 'insurance', 'PH_tx_status', 'MED_duration', 'MINI_MDx_text']

        for column in columns_to_encode:
            try:
                if column not in self.data.columns:
                    raise ValueError(f"Column '{column}' is not in the DataFrame.")
                
                # NaN 값을 빈 문자열로 대체
                self.data[column] = self.data[column].fillna('')

                # Convert all entries to string to ensure uniformity
                self.data[column] = self.data[column].astype(str)

                # Initialize LabelEncoder and fit-transform the column
                label_encoders[column] = LabelEncoder()
                self.data[column] = label_encoders[column].fit_transform(self.data[column])
            
            except Exception as e:
                print(f"Error encoding column '{column}': {e}")

        # NaN 값 채우기
        self.data = self.data.fillna(0)

        # 타겟 값 변환
        self.data['suicide'] = (self.data['suicide'] > 0).astype(float)

        # 정적 및 시계열 변수 설정
        self.static_variables = self.static_variables or [
            'VH_selfharm', 'DIG_cat', 'CTQ_EA',  'MED_duration', 'PH_tx_status', 'YMRS_sum', 
            'BPRS_sum', 'CTQ_PN', 'MED_AD', 'crime', 'age', 'sex'
        ]

        self.sequence_variables = self.sequence_variables or [
            'Daily_Entropy', 'Normalized_Daily_Entropy', 'Eight_Hour_Entropy',
            'Normalized_Eight_Hour_Entropy', 'Location_Variability', 'place',
            'first_TOTAL_ACCELERATION', 'last_TOTAL_ACCELERATION', 'mean_TOTAL_ACCELERATION',
            'median_TOTAL_ACCELERATION', 'max_TOTAL_ACCELERATION', 'min_TOTAL_ACCELERATION',
            'std_TOTAL_ACCELERATION', 'nunique_TOTAL_ACCELERATION', 'first_HEARTBEAT',
            'last_HEARTBEAT', 'mean_HEARTBEAT', 'median_HEARTBEAT', 'max_HEARTBEAT',
            'min_HEARTBEAT', 'std_HEARTBEAT', 'nunique_HEARTBEAT', 'delta_DISTANCE',
            'delta_SLEEP', 'delta_STEP', 'delta_CALORIES'
        ]
        
        return self.data


    def get_dataloaders(self, target_col='suicide', batch_size=16):
        """
        데이터 로더 생성 함수.
        
        :param target_col: 타겟 컬럼 이름.
        :param batch_size: DataLoader의 배치 크기.
        :return: train_dataloader, val_dataloader
        """
        if self.data is None:
            raise ValueError("데이터가 없습니다. 데이터를 로드하거나 제공해야 합니다.")

        dataset = SuicideDataset(self.data, target_col, self.static_variables, self.sequence_variables)
        train_size = int(0.8 * len(dataset))
        val_size = len(dataset) - train_size
        train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

        train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

        return train_dataloader, val_dataloader


# 예제 사용:
# 1. 데이터 로드
# data_handler = DataHandler()
# data_handler.load_data([
#     './data/merged_data_m1_dong.csv',
#     './data/merged_data_m1_yongin.csv',
#     './data/merged_data_m1_seoul.csv'
# ])

# # 2. 데이터 전처리
# data_handler.preprocess_data()

# # 3. 데이터 로더 생성
# train_dataloader, val_dataloader = data_handler.get_dataloaders()
