# SAFER

This guide provides  SAFER model module

## Baseline

- Baseline
  - data_processing_m1
    - __init__.py
    - crf_data.py
    - location_data.py
    - sensor_data.py
  - data_processing_m2
    - __init__.py
    - crf_data.ppy
    - location_data.py
    - sensor_data.py
  - model1
    - __init__.py
    - model
      - tft_model.pkl
    - dataloader.py
    - model.py
    - predictor.py
  - model2
    - model
      - final_model.pkl
    - dataloader.py
    - model.py
    - preictor.py
  - setup.py
  - __init__.py
  - README.md

## How To Use 

***Start pip install***


```python
!pip install saferx
```


<h2> m1 </h2>
<h3>m1 data processing</h3>
  

  1. location data
  ```python
    # Location 데이터 
      import saferx

    # saferx 패키지에서 LocationProcessor 사용
      location_processor = saferx.M1LocationProcessor()

    # CSV 파일에서 데이터 로드 및 전처리
      file_path = 'path_to_location_data.csv'
      processed_data = location_processor.load_data_from_csv(file_path)

    # 엔트로피 및 위치 가변성 계산
      resampled_data = location_processor.resample_and_calculate(processed_data)

    # 위치 레이블 할당
      location_dict = {
          (37.7749, -122.4194): 'hallway',
          (34.0522, -118.2437): 'ward'
      }
      labeled_data = location_processor.assign_location_labels(processed_data, location_dict)
    
  ```

  2. sensor data
  ```python
      # saferx 패키지에서 M1SensorDataProcessor 사용
        import saferx

        # M1SensorDataProcessor 인스턴스 생성
        sensor_processor = saferx.M1SensorDataProcessor()

        # 센서 데이터 로드
        sensor_data = sensor_processor.load_sensing_data('path_to_sensor_data.csv')

        # 센서 데이터 처리
        processed_data = sensor_processor.process_sensing_data(sensor_data)

        # 데이터 집계
        aggregated_data = sensor_processor.aggregate_sensing_data(processed_data)

        # 열 이름 재정렬
        final_data = sensor_processor.reorganize_column_names(aggregated_data)

        # 결과 출력
        print(final_data.head())
  ```

  3. CRF data
  ```python
    import saferx

    data_processor = saferx.M1DataProcessor()
    # 데이터 로드
    location_data, sensor_data, crf_data, trait_data = processor.load_data(
        location_file='location_data.csv',
        sensor_file='sensor_data.csv',
        crf_file='crf_data.csv',
        trait_file='trait_data.csv'
    )
    # 위치와 센서 데이터 병합
    merged_data = processor.merge_location_and_sensor()

    # CRF 데이터 병합
    merged_data_with_crf = processor.process_crf_data()

    # 성향 데이터 병합
    merged_data_with_traits = processor.merge_trait_data()

    # 자살 플래그 설정
    suicide_flags = [('John Doe', pd.Timestamp('2024-01-15 08:00:00'))]
    merged_data_with_flags = processor.clean_and_set_suicide_flag(suicide_flags)

    # 자해 발생 데이터 필터링
    filtered_data = processor.filter_data_for_self_harm_and_random()

    # 결과 확인
    print(filtered_data.head())
        
  ```
<h3>m1 model</h3>

  ```python
    import torch
    import saferx
      # 데이터 경로 설정
      data_paths = ['merged_data_m1.csv']

      # PredictionHandler 객체 생성 (모델 경로는 고정)
      predictor = saferx.PredictionHandler(data_paths, batch_size=16, device='cpu')
     
      # 예측 수행
      predictions = predictor.predict()

      print(predictions)
  ```
<h2> m2 </h2>
<h3>m2 data processing</h3>

  1. location data
  ```python
    # Location 데이터 
      import saferx

    # saferx 패키지에서 LocationProcessor 사용
      location_processor = saferx.M2LocationProcessor()

    # CSV 파일에서 데이터 로드 및 전처리
      file_path = 'path_to_location_data.csv'
      processed_data = location_processor.load_data_from_csv(file_path)

    # 엔트로피 및 위치 가변성 계산
      resampled_data = location_processor.resample_and_calculate(processed_data)

    # 위치 레이블 할당
      location_dict = {
          (37.7749, -122.4194): 'hallway',
          (34.0522, -118.2437): 'ward'
      }
      labeled_data = location_processor.assign_location_labels(processed_data, location_dict)
  ```
  2. sensor data
  ```python
        # saferx 패키지에서 M2SensorDataProcessor 사용
        import saferx

        # M1SensorDataProcessor 인스턴스 생성
        sensor_processor = saferx.M2SensorDataProcessor()

        # 센서 데이터 로드
        sensor_data = sensor_processor.load_sensing_data('path_to_sensor_data.csv')

        # 센서 데이터 처리
        processed_data = sensor_processor.process_sensing_data(sensor_data)

        # 데이터 집계
        aggregated_data = sensor_processor.aggregate_sensing_data(processed_data)

        # 열 이름 재정렬
        final_data = sensor_processor.reorganize_column_names(aggregated_data)

        # 결과 출력
        print(final_data.head())
  ```
  3. CRF data
  ```python
    import saferx

    data_processor = saferx.M2DataProcessor()

    # 데이터 로드
    processor.load_data(
        location_file='location_data.csv',
        sensor_file='sensor_data.csv',
        crf_file='crf_data.csv',
        trait_file='trait_data.csv'
    )

    # 위치와 센서 데이터 병합
    processor.merge_location_and_sensor()

    # CRF 데이터 처리 및 병합
    processor.process_crf_data()

    # 성향 데이터 병합
    merged_data = processor.merge_trait_data()

    # 최종 결과 확인
    print(merged_data.head())
  ```

<h3>m2 model</h3>

 ```python
    import torch
    import saferx

    data_path = 'merged_data_m2.csv'  # 데이터 경로 (CRF, sensor, location 등 합친 상태)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Predictor 객체 생성
    predictor = saferx.Predictor(device=device)

    # 데이터 로드 및 전처리
    data_loader = predictor.preprocess_data(data_path)

    # 예측 수행
    predictions = predictor.predict(data_loader)

    # 예측 결과 출력
    print(predictions)
  ```