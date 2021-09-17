## เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
## ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข

input_array = [-1,0,-1,20,5,6,4,7,8,9,2,1]
max_value = 0
index = 0
ans_index = 0
for i in input_array:
    if i > max_value:
        max_value = i 
        ans_index = index
    index += 1

print(ans_index)