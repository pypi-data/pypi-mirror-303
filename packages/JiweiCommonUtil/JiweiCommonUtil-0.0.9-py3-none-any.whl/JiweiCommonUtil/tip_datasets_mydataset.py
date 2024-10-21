import os

from .utils import Datum, DatasetBase, read_json, write_json, build_data_loader


template=["indoor","apartment","courtyard","road","restaurant","corridor","grocery","farm","farmland","office","warehouse","intersection","staircase","street","river course","refuse room","kitchen"]

class MyDataset(DatasetBase):

    dataset_dir = 'my_dataset'

    def __init__(self, root, num_shots):
        
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, 'images')

        self.template = template

        classnames = []
        with open(os.path.join(self.dataset_dir, 'classes.txt'), 'r') as f:
            lines = f.readlines()
            for line in lines:
                classnames.append(line.strip())
        cname2lab = {c: i for i, c in enumerate(classnames)}
        print(cname2lab)
        train = self.read_data(cname2lab, 'val.txt')
        val = self.read_data(cname2lab, 'train.txt')
        test = self.read_data(cname2lab, 'test.txt')
        
        train = self.generate_fewshot_dataset(train, num_shots=num_shots)
        
        super().__init__(train_x=train, val=val, test=test)
    
    def read_data(self, cname2lab, split_file):
        filepath = os.path.join(self.dataset_dir, split_file)
        items = []
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                imname = line
                classname = line.split('/')[-2]
                impath = os.path.join(self.image_dir, imname)
                label = cname2lab[classname]
                item = Datum(
                    impath=impath,
                    label=label,
                    classname=classname
                )
                items.append(item)
        return items