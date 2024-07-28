from pathlib import Path
import configparser
import os

def load_config(ini_path: str) -> dict:
    def eachsection(parser, section):
        config = dict(parser.items(section))
        for key in config:
            try:
                config[key] = eval(config[key])
            except:
                pass
        return config
    if not Path(ini_path).exists():
        raise FileNotFoundError(f'Not found: {ini_path}')
    parser = configparser.ConfigParser()
    parser.read(ini_path)
    database = {'database': {'tokenkey': os.getenv('tokenkey'),
                'database_id': os.getenv('database_id')}}
    return database | {section: eachsection(parser, section)
            for section in parser.sections()}
