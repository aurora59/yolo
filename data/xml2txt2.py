import glob
import os
xml_path = '/home/qqqq/123/data/road/labels'
def _read_anno(filename):
    import xml.etree.ElementTree as ET

    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    a = tree.find('size')
    w,h = [int(a.find('width').text),
           int(a.find('height').text)]

    objects = []
    if w==0:
        return []
    for obj in tree.findall('object'):
        name = obj.find('name').text
        if name == 'D00' or name == 'D10' or name == 'D20' or name == 'D40':
            label = 0
        else:
            continue

        bbox = obj.find('bndbox')
        x1, y1, x2, y2 = [int(float(bbox.find('xmin').text)),
                          int(float(bbox.find('ymin').text)),
                          int(float(bbox.find('xmax').text)),
                          int(float(bbox.find('ymax').text))]

        obj_struct = [label,round((x1+x2)/(2.0*w),4), round((y1+y2)/(2.0*h),4), round((x2-x1)/(w),4),round((y2-y1)/(h),4)]
        #
        objects.append(obj_struct)



    return objects
if __name__ == '__main__':
    t = ''
    # labels = []
    allfilepath = []
    # for file in os.listdir(xml_path):
    #     if file.endswith('.xml'):
    #         file = os.path.join(xml_path,file)
    #         allfilepath.append(file)
    #     else:
    #         pass

    for d, ds, fs in os.walk(xml_path):
        for file in fs:
            if file.endswith(".xml"):
                allfilepath.append(f"{d}/{file}")

    for file in allfilepath:
        # txt_path_file = os.path.dirname(file).replace('annotations/xmls', 'labels')
        # if not os.path.exists(txt_path_file):
        #     os.makedirs(txt_path_file)
        # txt_path = (file.split('.')[0] + '.txt').replace('annotations/xmls', 'labels')
        txt_path = file.split('.')[0] + '.txt'

        result = _read_anno(file)

        if len(result)==0.0:
            continue
        with open(txt_path,'w') as f:
            for line in result:
                if not line[1:] == [0.0,0.0,0.0,0.0]:
                    for a in line:
                        t = t+str(a)+' '
                    f.writelines(t)
                    f.writelines('\n')
                    t =''


