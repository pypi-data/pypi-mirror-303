import pandas as pd
import numpy as np
import torch
import pkg_resources
import pickle  # pickle 사용
from model1.dataloader import DataHandler  # DataHandler는 그대로 사용
from model1.model import TemporalFusionTransformer
class PredictionHandler:
    def __init__(self, data_paths, batch_size=16, device='cpu',model_path=None):
        if model_path is None:
            # pkg_resources를 사용하여 패키지 내부 경로에서 모델 파일 로드
            model_path = pkg_resources.resource_filename('saferx', 'model1/model/tft_model.pkl')
        self.model_path = model_path
        self.data_paths = data_paths
        self.batch_size = batch_size
        self.device = device

        # 데이터 로드 및 전처리
        self.data_handler = DataHandler()
        self.data_handler.load_data(data_paths)
        self.data_handler.preprocess_data()  # Ensure preprocessing is applied

        # 데이터 로더 생성
        self.train_dataloader, self.val_dataloader = self.data_handler.get_dataloaders(batch_size=batch_size)

        # pickle로 저장된 모델 불러오기
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

        # 모델을 디바이스로 이동 (예: GPU 또는 CPU)
        self.model.to(self.device)
        self.model.eval()

    def predict(self):
        """
        예측 수행 및 결과 반환. 결과는 이진 값 (0 또는 1)으로 변환됩니다.

        :return: 이진 예측 결과 numpy 배열.
        """
        self.model.eval()  # 모델을 평가 모드로 설정
        predictions = []
        with torch.no_grad():
            for batch in self.val_dataloader:
                static_data, sequence_data, _ = batch  # Unpack batch
                static_data, sequence_data = static_data.to(self.device), sequence_data.to(self.device)
                outputs, _, _ = self.model(static_data, sequence_data)
                
                # 확률을 0 또는 1로 변환
                predictions.append((outputs >= 0.5).cpu().numpy())

        return np.concatenate(predictions, axis=0)

    def count_predictions(self):
        """
        예측 결과에서 0과 1의 개수를 계산.

        :return: 0과 1의 개수를 포함하는 튜플 (count_0, count_1).
        """
        predictions = self.predict()
        count_0 = np.sum(predictions == False)
        count_1 = np.sum(predictions == True)
        
        print(f"Number of 0s: {count_0}")
        print(f"Number of 1s: {count_1}")
        
        return count_0, count_1
