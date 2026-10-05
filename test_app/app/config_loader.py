import yaml

API_KEY = "sk-demo-not-a-real-key-1234"


def load(text):
    return yaml.load(text, Loader=yaml.Loader)
