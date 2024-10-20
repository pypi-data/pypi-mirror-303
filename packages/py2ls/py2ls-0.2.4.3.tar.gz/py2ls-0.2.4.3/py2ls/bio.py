import GEOparse
from typing import Union
import pandas as pd
import os
import logging
from . import ips
from . import plot 
import matplotlib.pyplot as plt 

def load_geo(
    datasets: Union[list, str] = ["GSE00000", "GSE00001"],
    dir_save: str = "./datasets",
    verbose=False,
) -> dict:
    """
    Check if GEO datasets are already in the directory, and download them if not.

    Parameters:
    datasets (list): List of GEO dataset IDs to download.
    dir_save (str): Directory where datasets will be stored.

    Returns:
    dict: A dictionary containing the GEO objects for each dataset.
    """
    use_str = """
    get_meta(geo: dict, dataset: str = "GSE25097")
    get_expression_data(geo: dict, dataset: str = "GSE25097")
    get_probe(geo: dict, dataset: str = "GSE25097", platform_id: str = "GPL10687")
    get_data(geo: dict, dataset: str = "GSE25097")
    """
    print(f"you could do further: \n{use_str}")
    if not verbose:
        logging.getLogger("GEOparse").setLevel(logging.WARNING)
    else:
        logging.getLogger("GEOparse").setLevel(logging.DEBUG)
    # Create the directory if it doesn't exist
    if not os.path.exists(dir_save):
        os.makedirs(dir_save)
        print(f"Created directory: {dir_save}")
    if isinstance(datasets, str):
        datasets = [datasets]
    geo_data = {}
    for dataset in datasets:
        # Check if the dataset file already exists in the directory
        dataset_file = os.path.join(dir_save, f"{dataset}_family.soft.gz")

        if not os.path.isfile(dataset_file):
            print(f"\n\nDataset {dataset} not found locally. Downloading...")
            geo = GEOparse.get_GEO(geo=dataset, destdir=dir_save)
        else:
            print(f"\n\nDataset {dataset} already exists locally. Loading...")
            geo = GEOparse.get_GEO(filepath=dataset_file)

        geo_data[dataset] = geo

    return geo_data


def get_meta(geo: dict, dataset: str = "GSE25097", verbose=True) -> pd.DataFrame:
    """
    df_meta = get_meta(geo, dataset="GSE25097")
    Extracts metadata from a specific GEO dataset and returns it as a DataFrame.
    The function dynamically extracts all available metadata fields from the given dataset.

    Parameters:
    geo (dict): A dictionary containing the GEO objects for different datasets.
    dataset (str): The name of the dataset to extract metadata from (default is "GSE25097").

    Returns:
    pd.DataFrame: A DataFrame containing structured metadata from the specified GEO dataset.
    """
    # Check if the dataset is available in the provided GEO dictionary
    if dataset not in geo:
        raise ValueError(f"Dataset '{dataset}' not found in the provided GEO data.")

    # List to store metadata dictionaries
    meta_list = []

    # Extract the GEO object for the specified dataset
    geo_obj = geo[dataset]

    # Overall Study Metadata
    study_meta = geo_obj.metadata
    study_metadata = {key: study_meta[key] for key in study_meta.keys()}

    # Platform Metadata
    for platform_id, platform in geo_obj.gpls.items():
        platform_metadata = {
            key: platform.metadata[key] for key in platform.metadata.keys()
        }
        platform_metadata["platform_id"] = platform_id  # Include platform ID

        # Sample Metadata
        for sample_id, sample in geo_obj.gsms.items():
            sample_metadata = {
                key: sample.metadata[key] for key in sample.metadata.keys()
            }
            sample_metadata["sample_id"] = sample_id  # Include sample ID
            # Combine all metadata into a single dictionary
            combined_meta = {
                "dataset": dataset,
                **{
                    k: (
                        v[0]
                        if isinstance(v, list) and len(v) == 1
                        else ", ".join(map(str, v))
                    )
                    for k, v in study_metadata.items()
                },  # Flatten study metadata
                **platform_metadata,  # Unpack platform metadata
                **{
                    k: (
                        v[0]
                        if isinstance(v, list) and len(v) == 1
                        else "".join(map(str, v))
                    )
                    for k, v in sample_metadata.items()
                },  # Flatten sample metadata
            }

            # Append the combined metadata to the list
            meta_list.append(combined_meta)

    # Convert the list of dictionaries to a DataFrame
    meta_df = pd.DataFrame(meta_list)
    if verbose:
        print(
            f"Meta info columns for dataset '{dataset}': \n{sorted(meta_df.columns.tolist())}"
        )
        display(meta_df[:3].T)
    return meta_df


def get_probe(
    geo: dict, dataset: str = "GSE25097", platform_id: str = None, verbose=True
):
    """
    df_probe = get_probe(geo, dataset="GSE25097", platform_id: str = "GPL10687")
    """
    # try to find the platform_id from meta
    if platform_id is None:
        df_meta = get_meta(geo=geo, dataset=dataset, verbose=False)
        platform_id = df_meta["platform_id"].unique().tolist()
        platform_id = platform_id[0] if len(platform_id) == 1 else platform_id
        print(platform_id)
    df_probe = geo[dataset].gpls[platform_id].table
    if df_probe.empty:
        print(
            f"above is meta info, failed to find the probe info. 看一下是不是在单独的文件中包含了probe信息"
        )
        return get_meta(geo, dataset, verbose=True)
    if verbose:
        print(f"columns in the probe table: \n{sorted(df_probe.columns.tolist())}")
    return df_probe


def get_expression_data(geo: dict, dataset: str = "GSE25097") -> pd.DataFrame:
    """
    df_expression = get_expression_data(geo,dataset="GSE25097")
    只包含表达量数据,并没有考虑它的probe和其它的meta

    Extracts expression values from GEO datasets and returns it as a DataFrame.

    Parameters:
    geo (dict): A dictionary containing GEO objects for each dataset.

    Returns:
    pd.DataFrame: A DataFrame containing expression data from the GEO datasets.
    """
    expression_dataframes = []
    try:
        expression_values = geo[dataset].pivot_samples("VALUE")
    except:
        for sample_id, sample in geo[dataset].gsms.items():
            if hasattr(sample, "table"):
                expression_values = (
                    sample.table.T
                )  # Transpose for easier DataFrame creation
                expression_values["dataset"] = dataset
                expression_values["sample_id"] = sample_id
    return expression_values


def get_data(geo: dict, dataset: str = "GSE25097", verbose=True):
    # get probe info
    df_probe = get_probe(geo, dataset=dataset, verbose=False)
    # get expression values
    df_expression = get_expression_data(geo, dataset=dataset)
    print(
        f"df_expression.shape: {df_expression.shape} \ndf_probe.shape: {df_probe.shape}"
    )
    if any([df_probe.empty, df_expression.empty]):
        print(
            f"above is meta info, failed to find the probe info. 看一下是不是在单独的文件中包含了probe信息"
        )
        return get_meta(geo, dataset, verbose=True)
    df_exp = pd.merge(
        df_probe,
        df_expression,
        left_on=df_probe.columns.tolist()[0],
        right_index=True,
        how="outer",
    )

    # get meta info
    df_meta = get_meta(geo, dataset=dataset, verbose=False)
    col_rm = [
        "channel_count",
        "contact_web_link",
        "contact_address",
        "contact_city",
        "contact_country",
        "contact_department",
        "contact_email",
        "contact_institute",
        "contact_laboratory",
        "contact_name",
        "contact_phone",
        "contact_state",
        "contact_zip/postal_code",
        "contributor",
        "manufacture_protocol",
        "taxid",
        "web_link",
    ]
    # rm unrelavent columns
    df_meta = df_meta.drop(columns=[col for col in col_rm if col in df_meta.columns])
    # sorte columns
    df_meta = df_meta.reindex(sorted(df_meta.columns), axis=1)
    # find a proper column
    col_sample_id = ips.strcmp("sample_id", df_meta.columns.tolist())[0]
    df_meta.set_index(col_sample_id, inplace=True)  # set gene symbol as index

    col_gene_symbol = ips.strcmp("GeneSymbol", df_exp.columns.tolist())[0]
    # select the 'GSM' columns
    col_gsm = df_exp.columns[df_exp.columns.str.startswith("GSM")].tolist()
    df_exp.set_index(col_gene_symbol, inplace=True)
    df_exp = df_exp[col_gsm].T  # transpose, so that could add meta info

    df_merged = ips.df_merge(df_meta, df_exp)
    if verbose:
        print(
            f"\ndataset:'{dataset}' n_sample = {df_merged.shape[0]}, n_gene={df_exp.shape[1]}"
        )
        display(df_merged.sample(5))
    return df_merged


def split_at_lower_upper(lst):
    """
    将一串list,从全是lowercase,然后就是大写或者nan的地方分隔成两个list
    """
    for i in range(len(lst) - 1):
        if isinstance(lst[i], str) and lst[i].islower():
            next_item = lst[i + 1]
            if isinstance(next_item, str) and next_item.isupper():
                # Found the split point: lowercase followed by uppercase
                return lst[: i + 1], lst[i + 1 :]
            elif pd.isna(next_item):
                # NaN case after a lowercase string
                return lst[: i + 1], lst[i + 1 :]
    return lst, []


def add_condition(
    data: pd.DataFrame,
    column: str = "characteristics_ch1",  # 在哪一行进行分类
    column_new: str = "condition",  # 新col的命名
    by: str = "tissue: tumor liver",  # 通过by来命名
    by_not: str = ": tumor",  # 健康的选择条件
    by_name: str = "non-tumor",  # 健康的命名
    by_not_name: str = "tumor",  # 不健康的命名
    inplace: bool = True,  # replace the data
    verbose: bool = True,
):
    """
    Add a new column to the DataFrame based on the presence of a specific substring in another column.

        Parameters
        ----------
        data : pd.DataFrame
            The input DataFrame containing the data.
        column : str, optional
            The name of the column in which to search for the substring (default is 'characteristics_ch1').
        column_new : str, optional
            The name of the new column to be created (default is 'condition').
        by : str, optional
            The substring to search for in the specified column (default is 'heal').

    """
    # first check the content in column
    content = data[column].unique().tolist()
    if verbose:
        if len(content) > 10:
            display(content[:10])
        else:
            display(content)
    # 优先by
    if by:
        data[column_new] = data[column].apply(
            lambda x: by_name if by in x else by_not_name
        )
    elif by_not:
        data[column_new] = data[column].apply(
            lambda x: by_not_name if not by_not in x else by_name
        )
    if verbose:
        display(data)
    if not inplace:
        return data


def add_condition_multi(
    data: pd.DataFrame,
    column: str = "characteristics_ch1",  # Column to classify
    column_new: str = "condition",  # New column name
    conditions: dict = {
        "low": "low",
        "high": "high",
        "intermediate": "intermediate",
    },  # A dictionary where keys are substrings and values are condition names
    default_name: str = "unknown",  # Default name if no condition matches
    inplace: bool = True,  # Whether to replace the data
    verbose: bool = True,
):
    """
    Add a new column to the DataFrame based on the presence of specific substrings in another column.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame containing the data.
    column : str, optional
        The name of the column in which to search for the substrings (default is 'characteristics_ch1').
    column_new : str, optional
        The name of the new column to be created (default is 'condition').
    conditions : dict, optional
        A dictionary where keys are substrings to search for and values are the corresponding labels.
    default_name : str, optional
        The name to assign if no condition matches (default is 'unknown').
    inplace : bool, optional
        Whether to modify the original DataFrame (default is True).
    verbose : bool, optional
        Whether to display the unique values and final DataFrame (default is True).
    """

    # Display the unique values in the column
    content = data[column].unique().tolist()
    if verbose:
        if len(content) > 10:
            display(content[:10])
        else:
            display(content)

    # Check if conditions are provided
    if conditions is None:
        raise ValueError(
            "Conditions must be provided as a dictionary with substrings and corresponding labels."
        )

    # Define a helper function to map the conditions
    def map_condition(value):
        for substring, label in conditions.items():
            if substring in value:
                return label
        return default_name  # If no condition matches, return the default name

    # Apply the mapping function to create the new column
    data[column_new] = data[column].apply(map_condition)

    # Display the updated DataFrame if verbose is True
    if verbose:
        display(data)

    if not inplace:
        return data

def clean_dataset(
    data: pd.DataFrame, dataset: str = "GSE25097", condition: str = "condition",sep="///"
):
    """
    #* it has been involved in bio.batch_effects(), but default: False
    1. clean data set and prepare super_datasets
    2. if "///" in index, then extend it, or others.
    3. drop duplicates and dropna()
    4. add the 'condition' and 'dataset info' to the columns
    5. set genes as index
    """
    #! (4.1) clean data set and prepare super_datasets
    # df_data_2, 左边的列是meta,右边的列是gene_symbol
    col_gene = split_at_lower_upper(data.columns.tolist())[1][0]
    idx = ips.strcmp(col_gene, data.columns.tolist())[1]
    df_gene = data.iloc[:, idx:].T  # keep the last 'condition'

    #! if "///" in index, then extend it, or others.
    print(f"before extend shape: {df_gene.shape}")
    df = df_gene.reset_index()
    df_gene = ips.df_extend(df, column="index", sep=sep)
    # reset 'index' column as index
    # df_gene = df_gene.set_index("index")
    print(f"after extended by '{sep}' shape: {df_gene.shape}")

    # *alternative:
    # df_unique = df.reset_index().drop_duplicates(subset="index").set_index("index")
    #! 4.2 drop duplicates and dropna()
    df_gene = df_gene.drop_duplicates(subset=["index"]).dropna()
    print(f"drop duplicates and dropna: shape: {df_gene.shape}")

    #! add the 'condition' and 'dataset info' to the columns
    ds = [data["dataset"][0]] * len(df_gene.columns[1:])
    samp = df_gene.columns.tolist()[1:]
    cond = df_gene[df_gene["index"] == condition].values.tolist()[0][1:]
    df_gene.columns = ["index"] + [
        f"{ds}_{sam}_{cond}" for (ds, sam, cond) in zip(ds, samp, cond)
    ]
    df_gene.drop(df_gene[df_gene["index"] == condition].index, inplace=True)
    #! set genes as index
    df_gene.set_index("index",inplace=True)
    display(df_gene.head())
    return df_gene

def batch_effect(
    data: list = "[df_gene_1, df_gene_2, df_gene_3]",
    datasets: list = ["GSE25097", "GSE62232", "GSE65372"],
    clean_data:bool=False, # default, not do data cleaning
    top_genes:int=10,# only for plotting
    plot_=True,
    dir_save="./res/",
    kws_clean_dataset:dict={},
    **kwargs
):
    """
    usage 1: 
        bio.batch_effect(
                data=[df_gene_1, df_gene_2, df_gene_3],
                datasets=["GSE25097", "GSE62232", "GSE65372"],
                clean_data=False,
                dir_save="./res/")
    
    #! # or conbine clean_dataset and batch_effect together
        # # data = [bio.clean_dataset(data=dt, dataset=ds) for (dt, ds) in zip(data, datasets)]
        data_common = bio.batch_effect(
                    data=[df_data_1, df_data_2, df_data_3],
                    datasets=["GSE25097", "GSE62232", "GSE65372"], clean_data=True
                    )
    """
    # data = [df_gene_1, df_gene_2, df_gene_3]
    # datasets = ["GSE25097", "GSE62232", "GSE65372"]
    # top_genes = 10  # show top 10 genes
    # plot_ = True
    from combat.pycombat import pycombat
    if clean_data:
        data=[clean_dataset(data=dt,dataset=ds,**kws_clean_dataset) for (dt,ds) in zip(data,datasets)]
    #! prepare data
    # the datasets are dataframes where:
    # the indexes correspond to the gene names
    # the column names correspond to the sample names
    #! merge batchs
    # https://epigenelabs.github.io/pyComBat/
    # we merge all the datasets into one, by keeping the common genes only
    df_expression_common_genes = pd.concat(data, join="inner", axis=1)
    #! convert to float
    ips.df_astype(df_expression_common_genes, astype="float", inplace=True)

    #!to visualise results, use Mini datasets, only take the first 10 samples of each batch(dataset)
    if plot_:
        col2plot = []
        for ds in datasets:
            # select the first 10 samples to plot, to see the diff
            dat_tmp = df_expression_common_genes.columns[
                df_expression_common_genes.columns.str.startswith(ds)
            ][:top_genes].tolist()
            col2plot.extend(dat_tmp)
        # visualise results
        _, axs = plt.subplots(2, 1, figsize=(15, 10))
        plot.plotxy(
            ax=axs[0],
            data=df_expression_common_genes.loc[:, col2plot],
            kind="bar",
            figsets=dict(
                title="Samples expression distribution (non-correction)",
                ylabel="Observations",
                xangle=90,
            ),
        )
    # prepare batch list
    batch = [
        ips.ssplit(i, by="_")[0] for i in df_expression_common_genes.columns.tolist()
    ]
    # run pyComBat
    df_corrected = pycombat(df_expression_common_genes, batch, **kwargs)
    print(f"df_corrected.shape: {df_corrected.shape}")
    display(df_corrected.head())
    # visualise results again
    if plot_:

        plot.plotxy(
            ax=axs[1],
            data=df_corrected.loc[:, col2plot],
            kind="bar",
            figsets=dict(
                title="Samples expression distribution (corrected)",
                ylabel="Observations",
                xangle=90,
            ),
        )
        if dir_save is not None:
            ips.figsave(dir_save + "batch_sample_exp_distri.pdf")
    return df_corrected

def get_common_genes(elment1, elment2):
    common_genes=ips.shared(elment1, elment2)
    return common_genes