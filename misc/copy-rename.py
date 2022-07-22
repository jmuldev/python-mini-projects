
# Copy and rename with timestamp
import os
import shutil
import datetime

now = str(datetime.datetime.now())[:19]
now = now.replace(":","_")

src_dir="C:\\files\\xcel_test\\test.xlsm"
dst_dir="C:\\files\\xcel_test\\test_"+str(now)+".xlsm"
shutil.copy(src_dir,dst_dir)