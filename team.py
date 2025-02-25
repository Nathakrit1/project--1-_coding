def calculate_land_tax(land_value, land_type):
    """
    ฟังก์ชันคำนวณภาษีที่ดินตามประเภทของที่ดิน
    :param land_value: มูลค่าที่ดิน (บาท)
    :param land_type: ประเภทของที่ดิน (1-4)
    :return: จำนวนภาษีที่ต้องชำระ (บาท)
    """
    
    tax_rate = 0  # อัตราภาษีเริ่มต้น

    if land_type == 1:  # ที่ดินเพื่อการเกษตรกรรม
        if land_value <= 750000:
            tax_rate = 0  # ได้รับการยกเว้นภาษี
        elif land_value <= 50000000:
            tax_rate = 0.001  # 0.1%
        elif land_value <= 100000000:
            tax_rate = 0.002  # 0.2%
        else:
            tax_rate = 0.03   # 0.3%

    elif land_type == 2:  # ที่ดินเพื่อการอยู่อาศัย
        if land_value <= 10000000:
            tax_rate = 0.002  # 0.02%
        elif land_value <= 50000000:
            tax_rate = 0.003  # 0.03%
        elif land_value <= 100000000:
            tax_rate = 0.005  # 0.05%
        else:
            tax_rate = 0.01   # 0.1%

    elif land_type == 3:  # ที่ดินเพื่อพาณิชยกรรม
        if land_value <= 50000000:
            tax_rate = 0.003  # 0.3%
        elif land_value <= 100000000:
            tax_rate = 0.005  # 0.5%
        else:
            tax_rate = 0.01   # 1%

    elif land_type == 4:  # ที่ดินรกร้างว่างเปล่า
        if land_value <= 50000000:
            tax_rate = 0.005  # 0.5%
        elif land_value <= 100000000:
            tax_rate = 0.01   # 1%
        else:
            tax_rate = 0.015  # 1.5%

    else:
        return "ประเภทที่ดินไม่ถูกต้อง กรุณาเลือก 1-4"

    tax_amount = land_value * tax_rate
    return tax_amount


# รับค่ามูลค่าที่ดินและประเภทที่ดินจากผู้ใช้
try:
    land_value = float(input("กรุณากรอกมูลค่าที่ดิน (บาท): "))
    print("เลือกประเภทที่ดิน:")
    print("1. ที่ดินเพื่อการเกษตรกรรม")
    print("2. ที่ดินเพื่อการอยู่อาศัย")
    print("3. ที่ดินเพื่อพาณิชยกรรม")
    print("4. ที่ดินรกร้างว่างเปล่า")
    
    land_type = int(input("กรุณาเลือกประเภทที่ดิน (1-4): "))

    tax = calculate_land_tax(land_value, land_type)
    
    if isinstance(tax, str):
        print(tax)
    else:
        print(f"ภาษีที่ต้องชำระคือ: {tax:,.2f} บาท")

except ValueError:
    print("กรุณากรอกข้อมูลให้ถูกต้อง")
