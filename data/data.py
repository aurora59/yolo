import glob
import os
import random

img_path = glob.glob('/home/qqqq/123/data/helmet2/images/*')
random.shuffle(img_path)
train_dataset = img_path[:150]
val_dataset = img_path[150:]

with open('train2.txt', 'w') as f:
    for train in train_dataset:
        label_path = train.replace('images', 'labels').replace(os.path.splitext(train)[-1], '.txt')
        if os.path.isfile(label_path):
            f.write(train)
            f.write('\n')

with open('val2.txt', 'w') as f:
    for val in val_dataset:
        label_path = val.replace('images', 'labels').replace(os.path.splitext(val)[-1], '.txt')
        if os.path.isfile(label_path):
            f.write(val)
            f.write('\n')