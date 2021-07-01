import threading
from .models import *

from faker import Faker
fake = Faker()

import time
import random

class CreateStudentThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            for i in range(self.total):
                print(i)
                Student_Data.objects.create(
                    student_name        = fake.name(),
                    student_email       = fake.email(),
                    address             = fake.address(),
                    age                 = random.randint(15, 50)
                    )
        except Exception as e:
            print(e)