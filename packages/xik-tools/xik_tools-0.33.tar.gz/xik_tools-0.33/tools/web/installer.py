import subprocess
import os
import platform
import logging

class Installer:
    @staticmethod
    def install_chrome_and_driver():
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        current_os = platform.system()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 기본 경로 설정
        chrome_path = os.path.join(current_dir, "chrome")
        driver_path = os.path.join(current_dir, "chromedriver")

        # 드라이버 경로 존재 여부 확인
        if not os.path.exists(driver_path) or not os.path.exists(chrome_path):
            logger.info("Chrome 또는 ChromeDriver가 존재하지 않습니다. 설치를 시작합니다.")
            if current_os == "Linux":
                chrome_path, driver_path = Installer._install_chrome_and_driver_linux()
            
            elif current_os == "Windows":
                chrome_path, driver_path = Installer._install_chrome_and_driver_win()
            else:
                logger.error("지원하지 않는 운영체제입니다.")
                chrome_path, driver_path = None, None
        else:
            logger.info("Chrome 및 ChromeDriver가 이미 존재합니다.")
        
        return {"chrome_path": chrome_path, "driver_path": driver_path}

    @staticmethod
    def _install_chrome_and_driver_linux() -> dict:
        logger = logging.getLogger(__name__)
        logger.info("Linux용 Chrome 및 ChromeDriver 설치 중...")
        
        # 쉘 스크립트 내용
        shell_script_content = """
        #!/bin/bash
    
        # Download and setup Chrome
        wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.86/linux64/chrome-linux64.zip
        unzip chrome-linux64.zip
        rm chrome-linux64.zip
        mv chrome-linux64 chrome
        rm chrome-linux64
    
        # Download and setup ChromeDriver
        wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.86/linux64/chromedriver-linux64.zip
        unzip chromedriver-linux64.zip
        rm chromedriver-linux64.zip
        mv chromedriver-linux64 chromedriver
        rm chromedriver-linux64
    
        # Return Chrome installation path and ChromeDriver path
        echo $(pwd)/chrome
        echo $(pwd)/chromedriver
        """

        script_file_path = "set_chrome.sh"
        with open(script_file_path, "w") as script_file:
            script_file.write(shell_script_content)

        # 쉘 스크립트 실행
        result = subprocess.run(["bash", script_file_path], capture_output=True, text=True)

        # 쉘 스크립트 파일 삭제 (선택 사항)
        os.remove(script_file_path)

        if result.returncode == 0:
            logger.info("Linux에 Chrome 및 ChromeDriver 설치 완료.")
        else:
            logger.error(f"설치 중 오류 발생: {result.stderr}")

        current_dir = os.path.abspath(os.getcwd())
        chrome_path = os.path.join(current_dir, "chrome/chrome")
        driver_path = os.path.join(current_dir, "chromedriver/chromedriver")
        return chrome_path, driver_path

    @staticmethod
    def _install_chrome_and_driver_win() -> dict:
        logger = logging.getLogger(__name__)
        logger.info("Windows용 Chrome 및 ChromeDriver 설치 중...")
        
        # Windows에서 사용되는 배치 파일 내용
        batch_script_content = """
            @echo off
    
            :: Download and setup Chrome
            powershell -Command "& {Invoke-WebRequest -Uri 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/ChromeSetup.exe' -OutFile 'chrome_installer.exe'}"
            Start-Process -Wait -FilePath 'chrome_installer.exe' -ArgumentList '/silent /install'
            del 'chrome_installer.exe'
    
            :: Download and setup ChromeDriver
            powershell -Command "& {Invoke-WebRequest -Uri 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/chromedriver_win64.zip' -OutFile 'chromedriver.zip'}"
            Expand-Archive -Path 'chromedriver.zip' -DestinationPath 'chromedriver'
            del 'chromedriver.zip'
    
            :: Return Chrome installation path and ChromeDriver path
            echo %cd%\chrome
            echo %cd%\chromedriver
            """

        # 배치 파일에 내용 쓰기
        script_file_path = "set_chrome.bat"
        with open(script_file_path, "w") as script_file:
            script_file.write(batch_script_content)

        # 배치 파일 실행
        result = subprocess.run([script_file_path], shell=True, capture_output=True, text=True)

        # 배치 파일 삭제 (선택 사항)
        os.remove(script_file_path)

        if result.returncode == 0:
            logger.info("Windows에 Chrome 및 ChromeDriver 설치 완료.")
        else:
            logger.error(f"설치 중 오류 발생: {result.stderr}")

        # 반환된 결과에서 경로 추출
        current_dir = os.path.abspath(os.getcwd())
        chrome_path = os.path.join(current_dir, "chrome")
        driver_path = os.path.join(current_dir, "chromedriver")
        return chrome_path, driver_path
