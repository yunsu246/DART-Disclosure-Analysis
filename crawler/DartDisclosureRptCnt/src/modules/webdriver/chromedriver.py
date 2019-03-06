import os
import uuid
from arsenic import get_session, keys, browsers, services
from config import Config
from functools import wraps, partial


# Get Environment Variables & Parameters defined by src.config.py
BINARY_PATH = Config.BINARY_PATH

class AsyncWebDriverWrapper:
    def __init__(self):
        self.BINARY_PATH = Config.BINARY_PATH

        capabilities = { 'acceptSslCerts': True,'acceptInsecureCerts': True }            
        chromeOptions = {'args': [
            '--headless', '--no-sandbox', '--disable-dev-shm-usage', 
            '--disable-gpu', '--disable-setuid-sandbox', '--lang=ko_KR',
        ]}
        
        self.service = services.Chromedriver(binary=self.BINARY_PATH['CHROME_DRIVER'], log_file=os.devnull)
        self.browser = browsers.Chrome(chromeOptions=chromeOptions, **capabilities)

    def __call__ (self, func):
        @wraps(func)
        async def decorator(*args, **kwargs):
            async with get_session(self.service, self.browser) as session:
                copy_func = partial(func, session=session)
                return await copy_func(*args, **kwargs)
        return decorator
