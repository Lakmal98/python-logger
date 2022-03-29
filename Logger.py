import datetime


class Logger():
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f'{datetime.datetime.now()} - {message}\n')

    def warn(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"[WARN] {str(datetime.datetime.now())}: {message}\n")

    def error(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"[ERROR] {str(datetime.datetime.now())}: {message}\n")

    def info(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"[INFO] {str(datetime.datetime.now())}: {message}\n")

    def success(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"[SUCCESS] {str(datetime.datetime.now())}: {message}\n")

    def debug(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"[DEBUG] {str(datetime.datetime.now())}: {message}\n")
