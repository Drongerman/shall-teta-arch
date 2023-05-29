import time
import logging
import requests

logging.basicConfig(level=logging.INFO)

class CircuitBreaker:
    def __init__(self, name, max_failures, reset_timeout, max_retries):
        self.name = name
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.max_retries = max_retries
        self.failures = 0
        self.last_failure_time = None
        self.state = 'CLOSED'

    def execute(self, url, fallback_result):
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time >= self.reset_timeout:
                self.state = 'HALF_OPEN'
                logging.info('Try half_open Circuit breaker')
            else:
                logging.info('Stay Circuit breaker open')
                return fallback_result

        retries = 0
        while retries <= self.max_retries:
            try:
                response = requests.get(url, timeout=3)

                logging.info('Request successful')
                self.reset()
                return response
            except requests.exceptions.RequestException as e:
                logging.warning('Request failed')
                self.failures += 1
                self.last_failure_time = time.time()

                if self.failures >= self.max_failures:
                    self.state = 'OPEN'
                    raise ConnectionError('Service is unavailable')
                elif self.failures < self.max_failures and retries == self.max_retries:
                    raise ConnectionError('Service is unavailable')
                else:
                    retries += 1
                    logging.warning(f'Retrying request ({retries}/{self.max_retries})')
                

    def reset(self):
        self.failures = 0
        self.last_failure_time = None
        self.state = 'CLOSED'