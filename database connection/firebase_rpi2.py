import os
import time
from firebase_admin import credentials, storage, initialize_app
from uuid import uuid4

PROJECT_ID = "apple-detection-e8c67"  # Owner Project ID

cred = credentials.Certificate("./Key/serviceKey.json")  # Service Key Path
default_app = initialize_app(cred, {
    'storageBucket': f"{PROJECT_ID}.appspot.com"
})
bucket = storage.bucket()

def file_upload(local_file_path, remote_file_path):
    blob = bucket.blob(remote_file_path)
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token}
    blob.metadata = metadata
    blob.upload_from_filename(filename=local_file_path, content_type='image/jpeg')
    print(f"File {local_file_path} uploaded to {remote_file_path}")
    print(blob.public_url.split('/')[-1])

def get_current_files(folder_path):
    # 현재 폴더 내 파일 목록 조회
    current_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".jpg")]
    return current_files

def upload_new_images(folder_path, storage_path, uploaded_files):
    # 이전에 업로드한 파일 목록과 현재 폴더의 파일 목록을 비교하여 새로운 파일만 업로드
    current_files = get_current_files(folder_path)
    new_files = set(current_files) - set(uploaded_files)

    for filename in new_files:
        local_file_path = os.path.join(folder_path, filename)

        # 'rotten'으로 시작하는 파일은 'rotten_apple' 폴더로, 'normal'로 시작하는 파일은 'normal_apple' 폴더로 업로드
        sub_folder = "rotten_apple" if filename.startswith("rotten") else "normal_apple"
        remote_file_path = f"{storage_path}/{sub_folder}/{filename}"

        file_upload(local_file_path, remote_file_path)

    return current_files  # 최신 파일 목록 반환

def main():
    # 수정 필요한 부분: 업로드하려는 폴더 경로 및 Storage 경로
    folder_path_to_upload = "/home/kge/captured_images"
    storage_path = "rasp_detect_image"

    # 프로그램이 처음 실행될 때의 폴더 내 파일 목록을 저장
    uploaded_files = get_current_files(folder_path_to_upload)

    while True:
        uploaded_files = upload_new_images(folder_path_to_upload, storage_path, uploaded_files)
        time.sleep(1)  # 1초마다 폴더 확인

if __name__ == "__main__":
    print("Start ......")
    main()
    print("End Of File")
