import pytest
import settings


if __name__ == '__main__':
    pytest.main(['-s','-v','--alluredir=./reports/allure',settings.TEST_CASE_DIR,'--clean-alluredir'])