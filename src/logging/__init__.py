import logging 
from logging import StreamHandler, FileHandler
from datetime import datetime
import sys 
import os 
from src.utils.constants import LOGS_DIRECTORY_NAME

directory = LOGS_DIRECTORY_NAME
os.makedirs(directory , exist_ok = True)

filename = f"{directory}/{datetime.now().strftime('%d_%m_%I_%M')}.log"

logging.basicConfig(level=logging.INFO,  format= '%(asctime)s %(levelname)s:%(message)s' , 
                    
                    handlers=[
                        StreamHandler(sys.stdout), FileHandler(filename=filename)
                    ]
                    )


logger = logging.getLogger('Loan Approval')