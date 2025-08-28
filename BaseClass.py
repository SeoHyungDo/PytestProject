import logging

class BaseClass :
    def test_log(self):
        logger = logging.getLogger(__name__)  # 로그를 남길 수 있도록 로깅 선언 및 로그에 TC 이름을 새길 수 있는 __name__ 선언
        fileHandler = logging.FileHandler('logfile.log')  # Filehandler는 객체가 아닌 상위 로깅에서 가져온다 / 파일 이름을 입력해 준다.
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # asctime으로 시간 출력, levelname으로 로그들의 수준을 가져옴, name으로 TC 이름을 가져옴
        # s가 붙어야 문자열 취급
        fileHandler.setFormatter(formatter)  # 여기까지 formatter, filehandler 연결, filehandler에 형식 정보가 전달이 됨

        logger.addHandler(fileHandler)  # 로그 객체가 출력되어야 하는 파일이 무엇인지 정확한 파일 위치를 알려줌, addhandler 내에 filehandler를 넣어줌
        # 현재는 filehandler 정보만 로거에 전달하도록 규정되어 있는데, 형식정보를 filehandler에 전달 할 수 있다면 모든 정보는 파일 핸들러에 담겨있으므로 자동으로 로거에 연결 될 것

        logger.setLevel(logging.INFO)  # 로그의 레벨을 설정한다, 설정된 레벨 이상의 로그만 찍히게 됨.
        logger.debug("A debug statement is executed")
        logger.info("A Info statement is executed")
        logger.warning("잔액 부족!")  # 신용카드 결제 등에서 잔액이 마이너스인 경우 로그에 경고를 표시하되 테스트를 실패로 처리하고 싶지 않다면 자동화 테스트가 마이너스 잔고를 발견할 때 마다 warning을 입력
        logger.error("중대한 오류가 발생하여 테스트 실패!")
        logger.critical("테스트를 실행 할 수 없을 정도의 심각한 문제 발생")
        return logger