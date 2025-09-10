# myfunc2.py

def subtract_numbers(a, b):
    """
    ฟังก์ชันนี้รับพารามิเตอร์ตัวเลข 2 ตัว แล้วคืนค่าผลลบของมัน
    ตัวอย่าง: subtract_numbers(10, 3) => 7
    """
    return a - b

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    x = 15
    y = 8
    result = subtract_numbers(x, y)
    print(f"{x} - {y} = {result}")
