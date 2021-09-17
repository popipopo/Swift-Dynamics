## เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial 
## เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว


def zero_number_factorial(factorial):
    try:
        if factorial <= 0 or type(factorial) != "int"  :
            result = {"status":"ER","errorMessage":"factorial must be real number"}
            return result

        sum = 1
        last_zero_number = 0
        while factorial != 0:
            sum = sum * factorial
            factorial -= 1
        cal_sum = sum
        while (cal_sum % 10) == 0:
            last_zero_number += 1
            cal_sum /= 10

        print(sum/10)
        result = {"status":"OK","sum":sum,"last_zero_number":last_zero_number}

    except:
        result = {"status":"ER"}
    finally:
        return result

factorial = "gj"
print(zero_number_factorial(factorial))