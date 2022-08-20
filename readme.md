# Code level information

## how to find all availabe sub direcotry form main directory?

There is main ways to find it few are mention here:

Using os.walk()

        sub_folders = []
        for dir, sub_dirs, files in os.walk('../python/'):
            sub_folders.extend(sub_dirs)

Using gloab():

        files = glob('../python/*/', recursive=True)
        files = glob(os.path.join('../python/', "*", ""))   

Using os.scandir() it's faster then other        

        files = subfolders = [ f.path for f in os.scandir('../python/') if f.is_dir() ] 
        print(files);exit()

Chech which way is faster form here there is also included few more methods or class:

        os.scandir      took   1 ms. Found dirs: 439
        os.walk         took 463 ms. Found dirs: 441 -> it found the nested one + base folder.
        glob.glob       took  20 ms. Found dirs: 439
        pathlib.iterdir took  18 ms. Found dirs: 439
        os.listdir      took  18 ms. Found dirs: 439
