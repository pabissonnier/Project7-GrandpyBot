import pytest
import main


class TestMain:
    # - Test if input is a string
    def test_userinput(self):
        if type(main.userinput) == str:
            pass


if __name__ == '__main__':
    pytest.main()
