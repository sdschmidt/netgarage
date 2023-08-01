from netgarage.utils.settings import LevelSettings
import subprocess


class ExecutableCache:
    def __init__(self, executable_path: str):
        self.executable_path = executable_path
        self.log = {}

    def run(self, number: int) -> str:
        if not self.log.get(number):
            p = subprocess.run(
                [self.executable_path],
                input=f"{number}\n".encode(),
                stdout=subprocess.PIPE)
            self.log[number] = p.stdout.decode()
        return self.log[number]

    def get(self, number):
        return self.log.get(number)


class Solver:
    def __init__(self, settings: LevelSettings):
        self._settings = LevelSettings
        self._cache = ExecutableCache(executable_path=settings.bin)
        self.result = None
        pass

    @property
    def log(self):
        return self._cache.log

    def solve(self, inputs) -> str:
        for number in inputs:
            result = self._cache.run(number)
            if result is not None:
                self.result = result
                return result

    def get_result(self) -> str:
        return self.result


def main():
    solver = Solver(LevelSettings(1))
    solver.solve(range(999))


if __name__ == "__main__":
    main()
