import os

all_file_dir = './trainstes/'

f = open('./train.txt', 'w')

label_id = 0

class_list = [c for c in os.listdir(all_file_dir) if os.path.isdir(os.path.join(all_file_dir, c))]

# print(class_list)
for class_dir in class_list:

    image_path_pre = os.path.join(all_file_dir, class_dir)

    for img in os.listdir(image_path_pre):
        # print(img)
        f.write("{0}\t{1}\n".format(os.path.join(image_path_pre, img), label_id).replace('\\', '/'))

    label_id += 1
