import pandas as pd
import numpy as np
import datapackage as dtpck


def getting_dataset(url_path):
    package = dtpck.Package(url_path)
    resources = package.resources
    print("How many resources ? ", resources)


if __name__== '__main__':
    print(pd.__version__)
    print(pd)
    print("Numpy library :" , np.__version__)
    print(np)
