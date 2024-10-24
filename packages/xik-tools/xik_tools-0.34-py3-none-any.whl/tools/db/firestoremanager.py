from google.cloud import firestore
from google.oauth2 import service_account
from datetime import datetime
import logging

class FirestoreManager:
    def __init__(self, credentials_file):
        # 로깅 설정
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # 서비스 계정 자격 증명 로드
        self.credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.logger.info("Credentials loaded successfully.")
        
        # Firestore 클라이언트 초기화
        self.db = firestore.Client(credentials=self.credentials)
        self.logger.info("Firestore client initialized successfully.")

    def save_dataframe(self, dataframe, collection_name):
        """데이터프레임의 내용을 Firestore에 저장합니다."""
        date_key = datetime.now().strftime("%Y-%m-%d")  # 예: "2024-10-19"
        date_doc_ref = self.db.collection(date_key).document(collection_name)

        for index, row in dataframe.iterrows():
            doc_key = f'doc_{index}'  
            doc_ref = date_doc_ref.collection(collection_name).document(doc_key)
            doc_ref.set(row.to_dict())
            self.logger.info(f"Document {doc_key} added successfully under {date_key}/{collection_name}.")

    def read_data(self, collection_name):
        """Firestore에서 데이터를 읽어옵니다."""
        docs = self.db.collection(collection_name).stream()
        data = {}
        for doc in docs:
            data[doc.id] = doc.to_dict()
            self.logger.info(f"Document {doc.id} retrieved successfully from {collection_name}.")
        return data
