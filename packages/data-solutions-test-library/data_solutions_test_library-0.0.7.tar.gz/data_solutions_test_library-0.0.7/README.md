# Welcome to the Chainalysis Data Solutions Python SDK
A modern python wrapper for the Chainalysis Data Solutions API Suite.

## Documentation
See the latest documentation on all available classes and methods [here](https://docs.transpose.io/chainalysis-data-solutions-python-sdk/).

## Installation

To install the SDK, run the following command in bash.

```bash
pip install chainalysis
```

## Getting Started
Get an API Key at our [website](https://data.chainalysis.com/) by registering an account and
navigating to settings in the data solutions product section.


Begin using the SDK with the code below as a sample. The following code snippet details how to import and instantiate the Data Solutions Client to then be used to execute two kinds of queries: Analytical and Transactional.

Analytical queries are queries targeting the data you can view under the 'Explore Data' tab in Data Solutions. Transactional queries are queries targeting data you can find at [docs.transpose.io](docs.transpose.io).

```python
    # Import the module
    from chainalysis import DataSolutionsClient

    # Instantiate with an API Key
    ds = DataSolutionsClient({API_KEY})

    # Create an AnalyticalSelect object
    analytical_select = ds.orm.AnalyticalSelect("cross_chain.clusters")

    # Construct a query
    query = analytical_select.with_columns(
        analytical_select.c.cluster_id, analytical_select.c.entity_name
    ).where(
        analytical_select.c.address == "0x00703a0ce5406501c44ca657497c0f785e83dde0"
    ).limit(10)

    # Execute the query
    query_results = query.execute()

    # Print the results of the query as a json blob
    print(query_results.json())

    # Return the results of the query as a Pandas Dataframe
    dataframe = query_results.df()

    # OR construct an analytical query manually
    query = """
        SELECT * FROM cross_chain.clusters
        WHERE address = '0x00703a0ce5406501c44ca657497c0f785e83dde0'
        LIMIT 10;
    """

    # Execute the query
    query_results = ds.sql.analytical_query(
        query=query,
        polling_interval_sec=5, # How often to check if data is available yet
    )
```

## Future

More details on our SDK incoming!
