import os
from platformdirs import user_data_dir


def first_run_decorator(app_name: str, version: str = ""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            first_run = FirstRun(app_name, version)
            if first_run.is_first_run():
                try:
                    result = func(*args, **kwargs)
                    first_run.mark_first_run()
                    return result
                except Exception as ex:
                    print(f"Failed to run the script: {ex}")
            return None
        return wrapper
    return decorator


class FirstRun:
    def __init__(self, app_name: str, version: str = ""):
        self.app_name = app_name
        self.version = version
        self._user_data_path: str = os.path.join(user_data_dir(appname=self.app_name), "first_run.txt")

    def is_first_run(self) -> bool:
        if not os.path.exists(self._user_data_path):
            return True
        with open(self._user_data_path, "r") as f:
            if self.version and f.read() != self.version:
                return True
            return False

    def mark_first_run(self):
        os.makedirs(os.path.dirname(self._user_data_path), exist_ok=True)
        with open(self._user_data_path, "w") as f:
            f.write(self.version)
