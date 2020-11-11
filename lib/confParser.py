import yaml

class Config(object):
    def __init__(self):
        with open("lib/config.yaml","w") as ymlfile:
            cfg = yaml.load(ymlfile,Loader=yaml.SafeLoader)

        self.config = ConfigParser.ConfigParser()

    def get_labels(self):
        return self.config.get('Web','Labels')

if __name__ == '__main__':
    c = Config()
    print c.get_path()