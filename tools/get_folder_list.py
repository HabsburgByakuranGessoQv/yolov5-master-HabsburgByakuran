# 该文件是一个读取文件夹下所有文件夹绝对路径的程序。 用于制作数据集的txt文件中数据的写入, 配合 split_data.py 使.。
import os

# exam_path = r'D:\StuData\tomato\dataset_factory\tomato'
exam_path = r'D:\StuData\tomato\lesson\dataset'
back_path = r'D:\StuData\tomato\dataset_factory\background'

# back_path = r'D:\StuData\tomato\dataset_factory\temp'

back_list = os.listdir(back_path)
exam_list = os.listdir(exam_path)

abs_list = []

# for i in range(len(back_list)):
#     abs_list.append(os.path.join(back_path, back_list[i]))

for j in range(len(exam_list)):
    abs_list.append(os.path.join(exam_path, exam_list[j]))

print(abs_list)
