import settings
from common import logger


class BaseCase:
    '''
    测试用例基类
    '''

    # 测试套名称
    name = None
    logger = logger
    settings = settings

    # xunit风格的前置后置
    @classmethod
    def setup_class(cls):
        cls.logger.info('======={}测试开始======'.format(cls.name))

    @classmethod
    def teardown_class(cls):
        cls.logger.info('======={}测试结束======'.format(cls.name))