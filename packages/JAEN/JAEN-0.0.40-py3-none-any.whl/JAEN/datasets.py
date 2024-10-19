import torch
import os

def load_house_price():
    # 현재 파일의 디렉토리 경로를 가져옴
    current_dir = os.path.dirname(__file__)

    # 절대 경로로 변환
    X_path = os.path.join(current_dir, 'data', '01', 'X_train_tensor.pt')
    y_path = os.path.join(current_dir, 'data', '01', 'y_train_tensor.pt')
    test_path = os.path.join(current_dir, 'data', '01', 'X_test_tensor.pt')

    # 파일을 로드
    X = torch.load(X_path, weights_only=True)
    y = torch.load(y_path, weights_only=True)
    TEST = torch.load(test_path, weights_only=True)

    return X, y, TEST

def load_small_image():
    # 현재 파일의 디렉토리 경로를 가져옴
    current_dir = os.path.dirname(__file__)

    # 절대 경로로 변환
    X_path = os.path.join(current_dir, 'data', '02', 'x_train.pt')
    y_path = os.path.join(current_dir, 'data', '02', 'y_train.pt')
    test_path = os.path.join(current_dir, 'data', '02', 'x_test.pt')

    # 저장된 데이터 불러오기
    X = torch.load(X_path, weights_only=True)
    y = torch.load(y_path, weights_only=True)
    TEST = torch.load(test_path, weights_only=True)


    # 평가용 데이터는 y_test가 없으므로 None으로 설정
    return X, y, TEST

def load_documents():
    # 현재 파일의 디렉토리 경로를 가져옴
    current_dir = os.path.dirname(__file__)

    # 절대 경로로 변환
    X_path = os.path.join(current_dir, 'data', '03', 'x_train.pt')
    y_path = os.path.join(current_dir, 'data', '03', 'y_train.pt')
    test_path = os.path.join(current_dir, 'data', '03', 'x_test.pt')

    # 저장된 데이터 불러오기
    X = torch.load(X_path, weights_only=True)
    y = torch.load(y_path, weights_only=True)
    TEST = torch.load(test_path, weights_only=True)


    # 평가용 데이터는 y_test가 없으므로 None으로 설정
    return X.long(), y, TEST.long()

def load_boston():
    from boston import load_boston
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from torch.utils.data import DataLoader, TensorDataset

    # 데이터셋 로드 및 전처리
    data = load_boston()
    X, y = data.data, data.target

    # 데이터 표준화
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 학습 및 테스트 데이터셋 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 텐서로 변환
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_test = torch.tensor(X_test, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)

    # DataLoader 생성
    train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=32, shuffle=True)
    test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=16, shuffle=False)   
    return train_loader, test_loader
