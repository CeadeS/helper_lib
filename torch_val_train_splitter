def get_hyp_ind(d = '/data/workspace/datasets/imagenet/raw-data/validation/', partition = 10, complement = False):
    ind = []
    num = 0
    f =  lambda num,l,partition : num+l//partition,l if complement  else lambda num,l : num,num+l//partition
        for a in os.listdir(d):
            l=len(os.listdir(d+'/'+a))
            ind += list(np.arange(f(num,l,partition),1))
            num=num+l
    return ind
