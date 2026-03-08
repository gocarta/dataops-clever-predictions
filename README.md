# dataops-clever-predictions
> Real-Time Predictions of Bus Arrival Times

## background
Data standards are important to us at CARTA because they enable interoperability.  This pipeline takes the data about arrival times from our Clever deployment and publishes it to AWS S3.  Another pipeline will then use this data to create a GTFS-rt feed.

## frequency
The pipeline runs every minute.

## columns
| column | example | description |
| :--- | :--- | :--- |
| **stpid** | `2168` | The unique stop id |
| **vid** | `171` | The unique internal identifier for the vehicle |
| **rt** | `"1"` | The designated route number or shorthand name for the service |
| **prdtm** | `" 20260308 18:29"` | The predicted arrival time |

## download links
- [metadata](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_predictions/v1/meta.json)
- [csv](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_predictions/v1/data.csv)
- [parquet](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_predictions/v1/data.parquet)
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/clever_predictions/v1/data.json)

## preview link
- You can query the data with SQL using [duckdb](https://shell.duckdb.org/#queries=v0,CREATE-TABLE-dataset-AS-SELECT-*-FROM-'s3://gocarta/public/data/clever_predictions/v1/data.parquet'~,Describe-dataset~).

## support
Post an issue [here](https://github.com/gocarta/dataops-clever-predictions/issues) or email the package author at DanielDufour@gocarta.org.
