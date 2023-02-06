import copy


datasets = {}

#register用來註名model還是class之類的
def register(name):
    def decorator(cls):
        datasets[name] = cls
        return cls
    return decorator


def make(dataset_spec, args=None):
    #這裡的args有值的話通常都是dataset做過處理後的一個class
    if args is not None:
        dataset_args = copy.deepcopy(dataset_spec['args'])
        dataset_args.update(args)
    else:
        dataset_args = dataset_spec['args']
    #執行同spec_name之class
    dataset = datasets[dataset_spec['name']](**dataset_args)
    return dataset
