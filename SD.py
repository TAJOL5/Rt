
import os
import sys
import ctypes

# تحديد المسار إلى المكتبة الديناميكية
lib_path = os.path.join(os.path.dirname(__file__), "DM.cpython-311.so")

try:
    # تحميل المكتبة الديناميكية
    da_lib = ctypes.CDLL(lib_path)

    # استدعاء الدالة main من المكتبة
    da_lib.main()
except Exception as e:
    exit(str(e))
