from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os 
import logging
from tools.web.installer import Installer

class WebDriver:
    def __init__(self, headless=False):
        self.SELENIUM_URL = os.getenv('SELENIUM_URL')
        self.headless= headless
        self.driver = None
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_chrome(self):
        self.logger.info("Initializing Chrome WebDriver.")
        chrome_options = Options()
        chrome_options.add_argument(
            "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'"
        )  

        if self.headless:
            chrome_options.add_argument('--headless=new')  # 헤드리스 모드로 실행
            chrome_options.add_argument('--disable-gpu')  # 헤드리스 모드로 실행
        
        chrome_options.add_argument('--no-sandbox')  # 헤드리스 크롬 브라우저를 "사용자 네임스페이스" 옵션 없이 실행하도록 설정
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-extensions")  # 헤드리스 모드로 실행
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument('--disable-search-engine-choice-screen')
        chrome_options.add_argument('--disable-features=OptimizationGuideModelDownloading,OptimizationHintsFetching,OptimizationTargetPrediction,OptimizationHints')

        if self.SELENIUM_URL is not None:
            self.logger.info("Using remote WebDriver.")
            self.driver = webdriver.Remote(
                command_executor=self.SELENIUM_URL,
                options=chrome_options
            )
        else:
            self.logger.info("Installing Chrome and ChromeDriver.")
            webdriver_path = Installer.install_chrome_and_driver()
            self.webdriver_path = webdriver_path.get('driver_path')
            self.browser_path = webdriver_path.get('chrome_path')
            self.logger.info(f"ChromeDriver path: {self.webdriver_path}")
            self.logger.info(f"Chrome browser path: {self.browser_path}")
            chrome_options.binary_location = self.browser_path
            service = Service(executable_path=self.executable_path)  # 크롬 드라이버 경로 설정
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.logger.info("Chrome WebDriver initialized successfully.")
        return self.driver
    
    def move_element_to_center(self, element):
        """ 주어진 웹 요소를 뷰포트의 중앙으로 이동시킵니다. """
        self.logger.info("Moving element to center.")
        driver = self.driver
        ActionChains(driver).move_to_element(element).perform()

        # 뷰포트 크기 얻기
        viewport_width = driver.execute_script("return window.innerWidth;")
        viewport_height = driver.execute_script("return window.innerHeight;")

        # 객체의 위치 얻기
        object_x = element.location['x']
        object_y = element.location['y']
        object_width = element.size['width']
        object_height = element.size['height']

        # 화면 중앙으로 이동
        target_x = object_x + object_width / 2 - viewport_width / 2
        target_y = object_y + object_height / 2 - viewport_height / 2
        driver.execute_script(f"window.scrollTo({target_x}, {target_y});")
        self.logger.info(f"Element moved to center at ({target_x}, {target_y}).")
        return None

    def getDistanceScrollToBtm(self):
        """ 스크롤을 페이지 아래로 내립니다. """
        self.logger.info("Scrolling to the bottom of the page.")
        driver = self.driver
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)  # 스크롤이 내려가는 동안 대기

        # 스크롤이 이동한 거리 계산
        scrollDistance = driver.execute_script("return window.pageYOffset;")
        self.logger.info(f"Scrolled distance: {scrollDistance} pixels.")

        # Home 키를 눌러 시작 위치로 복귀
        driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(1)  # 스크롤이 위로 올라가는 동안 대기
        return scrollDistance

    def get_scroll_distance_total(self):
        """ 페이지 스크롤의 총 거리를 계산합니다. """
        self.logger.info("Calculating total scroll distance.")
        total_scroll_distance = 0
        prev_scroll_distance = -1
        
        while True:
            scroll_distance = self.__get_scroll_distance__()
            total_scroll_distance += scroll_distance
            if scroll_distance == 0 or scroll_distance == prev_scroll_distance:
                break
            prev_scroll_distance = scroll_distance
        
        # 초기 위치로 복귀하기 위해 페이지 맨 위로 스크롤합니다.
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        self.logger.info(f"Total scroll distance: {total_scroll_distance} pixels.")
        return total_scroll_distance

    def __get_scroll_distance__(self):
        driver = self.driver
        # 현재 페이지의 스크롤 위치를 가져옵니다.
        current_scroll_position = driver.execute_script("return window.scrollY || window.pageYOffset")
        self.logger.info(f"Current scroll position: {current_scroll_position} pixels.")
        
        # 스크롤 이벤트를 발생시킵니다.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        
        # 새로운 스크롤 위치를 가져옵니다.
        new_scroll_position = driver.execute_script("return window.pageYOffset")
        # 페이지 이동 거리를 계산합니다.
        scroll_distance = new_scroll_position - current_scroll_position
        self.logger.info(f"Scrolled distance: {scroll_distance} pixels.")
        return scroll_distance
