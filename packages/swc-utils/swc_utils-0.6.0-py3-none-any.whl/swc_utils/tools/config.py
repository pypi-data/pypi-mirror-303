class Config:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.__config = self.__read_config()

    def __read_config(self):
        config = {}
        with open(self.config_file, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    config[key] = value
        return config

    def __getitem__(self, item):
        return self.get(item)

    def get(self, key: str, default: str = None) -> str:
        return self.__config.get(key, default)

    def get_bool(self, key: str, default: bool = None) -> bool:
        return self.get(key, default) in ['True', 'true', '1']

    def get_list(self, key: str, default: list[str] = None) -> list[str]:
        return self.get(key, default).split(',')

    def get_int(self, key: str, default: int = None) -> int:
        return int(self.get(key, default))
