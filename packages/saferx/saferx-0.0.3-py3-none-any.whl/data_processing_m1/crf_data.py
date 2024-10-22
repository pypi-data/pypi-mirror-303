import pandas as pd

class DataProcessor:
    def __init__(self, location_data=None, sensor_data=None, crf_data=None, trait_data=None, self_harm_data=None):
        """
        DataProcessor 클래스 생성자.
        데이터는 DataFrame으로 직접 전달하거나 나중에 load_data 메소드를 통해 로드할 수 있습니다.
        """
        self.location_data = location_data
        self.sensor_data = sensor_data
        self.crf_data = crf_data
        self.trait_data = trait_data
        self.merged_data = None
        self.self_harm_data = self_harm_data  # 자해 발생 데이터 초기화

    def load_data(self, location_file=None, sensor_file=None, crf_file=None, trait_file=None):
        """
        CSV 파일을 로드하여 DataFrame으로 저장하는 함수. 파일 경로 또는 DataFrame을 입력 받을 수 있습니다.
        """
        if isinstance(location_file, str):
            self.location_data = pd.read_csv(location_file)
        elif isinstance(location_file, pd.DataFrame):
            self.location_data = location_file

        if isinstance(sensor_file, str):
            self.sensor_data = pd.read_csv(sensor_file)
        elif isinstance(sensor_file, pd.DataFrame):
            self.sensor_data = sensor_file

        if isinstance(crf_file, str):
            self.crf_data = pd.read_csv(crf_file, encoding='utf-8')
        elif isinstance(crf_file, pd.DataFrame):
            self.crf_data = crf_file

        if isinstance(trait_file, str):
            self.trait_data = pd.read_csv(trait_file, encoding='utf-8')
        elif isinstance(trait_file, pd.DataFrame):
            self.trait_data = trait_file

        # Return the loaded data for verification
        return self.location_data, self.sensor_data, self.crf_data, self.trait_data

    def merge_location_and_sensor(self):
        """
        위치 데이터와 센서 데이터를 공통 컬럼으로 병합하는 함수.
        """
        if self.location_data is None or self.sensor_data is None:
            raise ValueError("Location data or Sensor data is missing.")
        
        # Ensure both dataframes have the same 'targetTime' dtype
        self.location_data['targetTime'] = pd.to_datetime(self.location_data['targetTime'])
        self.sensor_data['targetTime'] = pd.to_datetime(self.sensor_data['targetTime'])
        
        # Merge the location and sensor dataframes on '이름' and 'targetTime'
        self.merged_data = pd.merge(self.location_data, self.sensor_data, on=['이름', 'targetTime'], how='inner')
        
        # Debugging: Output the merged data length
        print(f"Merged data length: {len(self.merged_data)}")

        # Optionally, inspect the data
        print(self.merged_data.head())

        # If there are mismatches, you can check where they occur
        if len(self.merged_data) != len(self.location_data):
            print("Mismatch in merging: ")
            print("Location data head:\n", self.location_data.head())
            print("Sensor data head:\n", self.sensor_data.head())

        return self.merged_data  # Return the merged data for verification

    def process_crf_data(self):
        """
        CRF 데이터를 처리하고 merged_data와 병합하는 함수.
        """
        if self.crf_data is None or self.merged_data is None:
            raise ValueError("CRF 데이터 또는 병합된 데이터가 없습니다.")

        # 불필요한 열 제거 및 열 이름 변경
        if 'Unnamed: 0' in self.crf_data.columns:
            self.crf_data = self.crf_data.drop(columns=['Unnamed: 0'])
        if 'researchNum' in self.crf_data.columns:
            self.crf_data = self.crf_data.drop(columns=['researchNum'])
        
        self.crf_data = self.crf_data.rename(columns={'key': '이름'})
        
        drop_columns = ['VE_tx', 'VE_tx_inj_time', 'VE_tx_secl_startime', 'VE_tx_secl_endtime', 
                        'VE_tx_rest_startime', 'VE_tx_rest_endtime', 'week', 'Eval_datetime', 'elapsed_date']
        existing_columns = [col for col in drop_columns if col in self.crf_data.columns]
        if existing_columns:
            self.crf_data = self.crf_data.drop(columns=existing_columns)
        
        # 'VE_tx_time'을 datetime으로 변환
        self.crf_data['VE_tx_time'] = pd.to_datetime(self.crf_data['VE_tx_time'])
        
        # 병합된 데이터 정렬
        self.merged_data.sort_values(by=['이름', 'targetTime'], inplace=True)
        
        # CRF 데이터와 merged_data 병합
        for key, group in self.merged_data.groupby('이름'):
            first_date = group['targetTime'].min()
            crf_subset = self.crf_data[self.crf_data['이름'] == key].reset_index(drop=True)
            #7일 간격으로 mapping
            for i, crf_row in crf_subset.iterrows():
                start_date = first_date + pd.Timedelta(days=7 * i)
                end_date = start_date + pd.Timedelta(days=7)
                mask = (self.merged_data['이름'] == key) & (self.merged_data['targetTime'] >= start_date) & (self.merged_data['targetTime'] < end_date)
                for col in crf_row.index:
                    if col not in ['이름', 'targetTime']:
                        self.merged_data.loc[mask, col] = crf_row[col]
            
            # 응급 상황 처리
            emergency_data = crf_subset[crf_subset['status'] == 'emergency']
            for emg_row in emergency_data.itertuples():
                date_match = (self.merged_data['이름'] == key) & (self.merged_data['targetTime'].dt.date == getattr(emg_row, 'VE_tx_time').date())
                if date_match.any():
                    for col in crf_subset.columns.difference(['이름', 'VE_tx_time', 'status']):
                        self.merged_data.loc[date_match, col] = getattr(emg_row, col)
        
        # 'idxInfo' 열이 존재하면 제거
        if 'idxInfo' in self.merged_data.columns:
            self.merged_data = self.merged_data.drop(columns=['idxInfo'])

        return self.merged_data  # Return the merged data for verification

    def merge_trait_data(self):
        """
        성향 데이터를 병합된 데이터에 병합하는 함수.
        """
        if self.trait_data is None or self.merged_data is None:
            raise ValueError("성향 데이터 또는 병합된 데이터가 없습니다.")
        
        self.trait_data = self.trait_data.rename(columns={'key': '이름'})
        trait_subset = self.trait_data
        
        self.merged_data = pd.merge(self.merged_data, trait_subset, on='이름')

        return self.merged_data  # Return the merged data for verification

    def clean_and_set_suicide_flag(self, suicide_flags):
        """
        데이터 정리 및 'suicide' 플래그 설정 함수.
        외부에서 전달된 'suicide_flags'를 사용하여 플래그를 설정합니다.
        """
        # 'targetTime'을 datetime으로 변환
        self.merged_data['targetTime'] = pd.to_datetime(self.merged_data['targetTime'])

        # "이름" 열의 문자열 일관되게 정리
        self.merged_data['이름'] = self.merged_data['이름'].str.replace(r'\s+', '', regex=True)

        # "suicide" 칼럼을 추가하고 기본값으로 0 설정
        self.merged_data['suicide'] = 0

        # 외부에서 전달된 suicide_flags를 사용하여 'suicide' 플래그를 설정합니다.
        for target_name, target_time in suicide_flags:
            condition = (
                (self.merged_data['이름'] == target_name) &
                (self.merged_data['targetTime'] >= target_time - pd.Timedelta(hours=1)) 
            )
            matched_rows = self.merged_data.loc[condition]
            print(f"Matched rows for {target_name} around {target_time}:\n", matched_rows)
            self.merged_data.loc[condition, 'suicide'] = 1

        return self.merged_data  # Return the final data for verification

    def filter_data_for_self_harm_and_random(self):
        """
        자해 발생 데이터와 랜덤 데이터를 필터링하는 함수.
        """
        if self.self_harm_data is None or self.merged_data is None:
            raise ValueError("자해 발생 데이터 또는 병합된 데이터가 없습니다.")
        
        filtered_df = pd.DataFrame()
        self.merged_data['targetTime'] = pd.to_datetime(self.merged_data['targetTime'], errors='coerce')
        
        # 자해 발생 환자들 처리
        for index, row in self.self_harm_data.iterrows():
            name = row['이름']
            specific_time = row['시간']
            start_range = specific_time - pd.Timedelta(hours=6)
            end_range = specific_time + pd.Timedelta(hours=6)
            patient_data = self.merged_data[
                (self.merged_data['이름'] == name) &
                (self.merged_data['targetTime'] >= start_range) &
                (self.merged_data['targetTime'] <= end_range)
            ]
            if not patient_data.empty:
                filtered_df = pd.concat([filtered_df, patient_data])

        # 나머지 환자들에 대해 랜덤으로 날짜 선택
        remaining_patients = self.merged_data[~self.merged_data['이름'].isin(self.self_harm_data['이름'])]
        for name, group in remaining_patients.groupby('이름'):
            if len(group) > 0:
                random_date = group['targetTime'].dt.date.sample(n=1).iloc[0]
                start_datetime = pd.to_datetime(str(random_date))
                start_range = start_datetime - pd.Timedelta(hours=6)
                end_range = start_datetime
                
                temp_df = group[(group['targetTime'] >= start_range) & (group['targetTime'] <= end_range)]
                filtered_df = pd.concat([filtered_df, temp_df])

        return filtered_df


