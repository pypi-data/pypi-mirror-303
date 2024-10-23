import pandas as pd

def data_import(file,columnnames):

    """
    Imports a file and renames the columns.

    Args:
        file (str): The location of the file.

    Returns:
        data (Dataframe): In case of SAMM the table mostly contains time and concentration values.
    """

    data = pd.read_csv(file, sep="\t|,|;", engine='python')

    # set the column name
    data.columns = columnnames
    print("The overview of the dataset:\n", data)
    return data