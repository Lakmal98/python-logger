import datetime


class Logger():
    def __init__(self, log_file='logs.log'):
        self.log_file = log_file

    def log(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(f"{prefix}{datetime.datetime.now()} - {message}\n")

    def warn(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[WARN] \t\t{str(datetime.datetime.now())}: {message}\n")

    def error(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[ERROR] \t{str(datetime.datetime.now())}: {message}\n")

    def info(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[INFO] \t\t{str(datetime.datetime.now())}: {message}\n")

    def success(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[SUCCESS] \t{str(datetime.datetime.now())}: {message}\n")

    def debug(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[DEBUG] \t{str(datetime.datetime.now())}: {message}\n")

    def report(self, message, prefix=''):
        with open(self.log_file, 'a') as f:
            f.write(
                f"{prefix}[REPORT] \t{str(datetime.datetime.now())}: {message}\n")
