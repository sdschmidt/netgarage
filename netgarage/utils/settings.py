
BIN_DIR = '/levels'
HOME_DIR = '/home'
NUM_LEVELS = 10


class LevelSettings:
    level = None

    def __init__(self, level: int) -> None:
        self.level = level
        pass

    @property
    def bin(self) -> str:
        return f"{BIN_DIR}/level{self.level:02}"

    @property
    def home(self) -> str:
        return f"{HOME_DIR}/level{self.level}"
