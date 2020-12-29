import logging


class MyLogger:
    def __init__(self):
        self.name = "Health check _ {name}".format(name=__name__)
        self.logger = logging.getLogger()

    def error(self, msg: str):
        self.logger.critical(msg)
        print("TODO: Toggle cloud logger alert here, with the same message ({msg})".format(msg=msg))

    def warn(self, msg: str):
        self.logger.warning(msg)
        print("TODO: Toggle cloud logger alert here, with the same message ({msg})".format(msg=msg))

    def info(self, msg: str):
        self.logger.info(msg)
        print("TODO: Toggle cloud logger info here, with the same message ({msg})".format(msg=msg))

    def debug(self, msg: str):
        self.logger.debug(msg)
        print("TODO: Toggle cloud logger info here, with the same message ({msg})".format(msg=msg))