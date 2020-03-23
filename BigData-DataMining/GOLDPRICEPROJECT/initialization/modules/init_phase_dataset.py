import pandas as pd
import numpy as np
import datapackage
from initialization import MY_DATA_URL
from initialization import MY_SETS



def getting_dataset(url_path):
    print("MY_URL_PATH is :", url_path)
    package = datapackage.Package(url_path)
    resources = package.resources
    annual_path = resources[1].descriptor['path']
    monthly_path = resources[2].descriptor['path']
    total_resources = len(resources)
    print("How many resources ? ", total_resources)
    df_annual = pd.read_csv(annual_path, sep=',')
    df_monthly = pd.read_csv(monthly_path, sep=',')
    print("KEYS ANNUAL DATASET",df_annual.keys())
    print("KEYS MONTHLY DATASET ",df_monthly.keys())
    print("NB of monthly records ", df_annual.count())


    # #data_prices_monthly = pd.read_csv
    # for resource, i in enumerate(resources,1):
    #     print("resource ", resource)
    #     name_data = "data_".join(str(i))
    #     for resource in package.resources:
    #         if resource.descriptor['name'] == 'monthly_csv' and resource.descriptor['datahub']['type'] == 'derived/csv':
    #             print("CSV file path is :", resource.descriptor['path'])
    #





if __name__== '__main__':
    getting_dataset (MY_DATA_URL)