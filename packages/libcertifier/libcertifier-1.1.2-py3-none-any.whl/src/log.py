from .constants import change_dir
from inspect import currentframe, getframeinfo
import logging
from logging.handlers import RotatingFileHandler
from argparse import Namespace
import os, stat, json, sys
import importlib.resources as pkg_resources

logging.TRACE = 1
logging.DEBUG = 2
logging.INFO = 3
logging.WARNING = 4
logging.ERROR = 5
logging.FATAL = 6

logging.getLogger("urllib3").setLevel(logging.WARNING)

levels = {
    1: ["TRACE", "\x1b[94m"],
    2: ["DEBUG", "\x1b[36m"],
    3: ["INFO", "\x1b[32m"],
    4: ["WARN", "\x1b[33m"],
    5: ["ERROR", "\x1b[31m"],
    6: ["FATAL", "\x1b[35m"]
}

class log_cfg():
    def __init__(self, file_name = None, level = 4, quiet = 1, max_size = 5000000):
        self._file_name: str = file_name
        self._level: int = level
        self._quiet: int = quiet
        self._newlines: int = 0
        self._stripped: int = 0
        self._max_size: int = max_size

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def quiet(self):
        return self._quiet

    @quiet.setter
    def quiet(self, value):
        self._quiet = value

    def toggle_quiet(self):
        self._quiet = 1 if (self._quiet == 0) else 0

    @property
    def newlines(self):
        return self._newlines

    @newlines.setter
    def newlines(self, value):
        self._newlines = 1 if (self._newlines == 0) else 0

    def toggle_newlines(self):
        self._newlines = 1 if (self._newlines == 0) else 0

    @property
    def stripped(self):
        return self._stripped

    @stripped.setter
    def stripped(self, value):
        self._stripped = value

    def toggle_stripped(self):
        self._stripped = 1 if (self._stripped == 0) else 0

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        self._max_size = value

logger = logging.getLogger()
cfg = log_cfg()

def read_from_cfg(args: Namespace):
    
    path = None
    if args.config and os.path.isfile(args.config):
        path = args.config
    else:
        with pkg_resources.path('src.resources', 'libcertifier.cfg') as cfg_path:
            path = str(cfg_path)
            
    if path is None:
        return path

    with open(path, 'r') as file:
        data = json.load(file)

    if 'libcertifier.log.level' in data:
        cfg.level = data['libcertifier.log.level']
    
    if 'libcertifier.log.file' in data:
        cfg.file_name = data['libcertifier.log.file']
    
    if 'libcertifier.log.max.size' in data:
        cfg.max_size = data['libcertifier.log.max.size']
    
    return cfg
            
def log_setup(args: Namespace):
    cfg = read_from_cfg(args)
    if cfg == None:
        logger.fatal("Couldn't find a config to use")
        log_destroy()
        sys.exit()

    open_output(cfg)

    for level in levels:
        logging.addLevelName(level, levels[level][0])

    logging.basicConfig(
     handlers=[
        logging.StreamHandler(sys.stdout),
        RotatingFileHandler(cfg.file_name, maxBytes=cfg.max_size, backupCount=1)
     ],
     format='%(asctime)s %(levelname)s %(message)s',
     datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger.setLevel(cfg.level)

def verbose_log_check(verbose: bool, msg: str, lvl: str | int):
    if verbose:
        log(msg, lvl)

def log(msg: str, lvl: str|int):
    if cfg.quiet == 1:
        if not isinstance(msg, str):
            logging.error(msg= str(getframeinfo(currentframe().f_back).filename) + ":" +  str(getframeinfo(currentframe().f_back).lineno) + " Invalid message provided")
        elif (not isinstance(lvl, str) and not isinstance(lvl, int) or 
              isinstance(lvl, str) and (lvl.upper() not in logging.getLevelNamesMapping().keys()) or 
              isinstance(lvl, int) and (lvl not in logging.getLevelNamesMapping().values())):
            logging.error(msg= str(getframeinfo(currentframe().f_back).filename) + ":" +  str(getframeinfo(currentframe().f_back).lineno) + " Invalid level provided")
        else:
            if isinstance(lvl, str):
                lvl = logging.getLevelNamesMapping()[lvl.upper()]

            if isinstance(lvl, int) and lvl >= logger.level:
                message = str(getframeinfo(currentframe().f_back).filename) + ":" +  str(getframeinfo(currentframe().f_back).lineno) + " " + msg

                if (cfg.newlines == 1):
                    with open(cfg.file_name, 'a') as file:
                        file.write("\n") if os.path.getsize(cfg.file_name) > 0 else None
                
                logger.log(lvl, message)

@staticmethod
def open_output(cfg: log_cfg):
    try:
        if not os.path.exists(cfg.file_name):
            path = os.path.abspath(cfg.file_name)
            change_dir(os.path.dirname(path))
            open(cfg.file_name, "w").close()

        os.chmod(cfg.file_name, os.O_CREAT | os.O_APPEND | os.O_WRONLY | stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
    except Exception as e:
        log("Error opening output: " + str(e), "ERROR")
        log_destroy()
        exit()

def log_destroy():
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logging.shutdown()