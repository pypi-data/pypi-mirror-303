import pandas as pd
import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import MinMaxScaler

class DataProcessor:
    
    @staticmethod
    def preprocess_data(data):
      
        data = pd.get_dummies(data, columns=['place'])
        data = data.replace({'False': '0', 'True': '1'})
        data['targetTime'] = pd.to_datetime(data['targetTime'])
        data.sort_values(['이름', 'targetTime'], inplace=True)
        data = data.fillna(0)
       

        numeric_features = data.select_dtypes(include=[np.number]).columns.tolist()
        scaler = MinMaxScaler(feature_range=(-1, 1))
        data[numeric_features] = scaler.fit_transform(data[numeric_features])

        return data

    @staticmethod
    def reset_week_numbers(df, date_col='targetTime'):
        df['week'] = df.groupby('이름')[date_col].transform(lambda x: ((x - x.min()).dt.days // 7) + 1)
        return df

    @staticmethod
    def find_max_sequence_length_by_week(df, seq_cols):
        max_length = 0
        for _, group in df.groupby(['이름', 'week']):
            if len(group) > max_length:
                max_length = len(group)
        return max_length

    @staticmethod
    def transform_target(df):
        df['BPRS_change'] = (df['BPRS_sum'].diff().shift(-1) < 0).astype(int)
        df['YMRS_change'] = (df['YMRS_sum'].diff().shift(-1) < 0).astype(int)
        df['MADRS_change'] = (df['MADRS_sum'].diff().shift(-1) < 0).astype(int)
        df['HAMA_change'] = (df['HAMA_sum'].diff().shift(-1) < 0).astype(int)
        return df

    @staticmethod
    def pad_sequence(id_df, max_length, seq_cols):
        sequence = id_df[seq_cols].values
        num_padding = max_length - len(sequence)
        padding = np.zeros((num_padding, len(seq_cols)))
        padded_sequence = np.vstack([padding, sequence])
        return padded_sequence
    @staticmethod
    def find_max_sequence_length_by_week(df, seq_cols):
        max_length = 0
        for _, group in df.groupby(['이름', 'week']):
            if len(group) > max_length:
                max_length = len(group)
        return max_length

    @staticmethod
    def prepare_data_for_model_by_week(df, max_length, seq_cols, target_cols):
        results = []
        target_means = df[target_cols].mean()

        for id in df['이름'].unique():
            patient_data = df[df['이름'] == id]
            for week in range(1, 5):  # 항상 1주차부터 4주차까지 고려
                if week in patient_data['week'].unique():
                    week_data = patient_data[patient_data['week'] == week]
                    padded_seq = DataProcessor.pad_sequence(week_data, max_length, seq_cols)
                    X_week = np.array([padded_seq], dtype=np.float32)
                    y_week = week_data[target_cols].dropna().iloc[-1].values
                else:
                    X_week = np.zeros((1, max_length, len(seq_cols)), dtype=np.float32)
                    y_week = target_means.values.astype(np.float32)

                results.append({
                    'Patient_ID': id,
                    'Week': week,
                    'X': X_week,
                    'y': y_week
                })
        return results

    @staticmethod
    def convert_results_to_tensors(results):
        X_data = np.vstack([result['X'] for result in results])
        y_data = np.array([result['y'] for result in results], dtype=np.float32)
        valid_indices = ~np.isnan(y_data).any(axis=1)
        X_data = X_data[valid_indices]
        y_data = y_data[valid_indices]
        X_tensor = torch.tensor(X_data, dtype=torch.float32)
        y_tensor = torch.tensor(y_data, dtype=torch.float32)
        return X_tensor, y_tensor

    @staticmethod
    def get_dataloaders(train_data, test_data, seq_cols, target_cols, max_length, batch_size=16):
        train_results = DataProcessor.prepare_data_for_model_by_week(train_data, max_length, seq_cols, target_cols)
        test_results = DataProcessor.prepare_data_for_model_by_week(test_data, max_length, seq_cols, target_cols)
        X_train_tensor, y_train_tensor = DataProcessor.convert_results_to_tensors(train_results)
        X_test_tensor, y_test_tensor = DataProcessor.convert_results_to_tensors(test_results)
        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        return train_loader, test_loader
