from .my_dataset import MyDataset


dataset_list = {
                "mydataset": MyDataset,
                }


def build_dataset(dataset, root_path, shots):
    return dataset_list[dataset](root_path, shots)