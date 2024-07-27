class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigurationManager(metaclass=SingletonMeta):
    def __init__(self):
        self.configurations = {}
        self.load_configurations()
    
    def load_configurations(self):
        # Simulating loading from a file
        self.configurations = {
            "database_url": "http://localhost:5432/mydb",
            "api_key": "1234567890abcdef"
        }
    
    def get(self, key):
        return self.configurations.get(key)

# Usage
config1 = ConfigurationManager()
config2 = ConfigurationManager()

print(config1 is config2)  # True, both are the same instance
print(config1.get("database_url"))  # Output: http://localhost:5432/mydb
