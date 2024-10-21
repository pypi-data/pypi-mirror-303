# Oscillation Spotter - Oscillation Detection Module

## Overview
The Oscillation Spotter module provides a unique approach to detect sharp oscillations in financial asset prices (e.g., stocks, cryptocurrencies) over very short timeframes. This software is open-source and offers the ability to detect areas of rapid price movement, helping researchers and analysts to explore potential correlations between certain events and price trends.

Example plot results:
![img.png](img.png)

### Why Use This Module?

- **Difficulty in Identifying Sharp Movements**: It is very challenging to distinguish between sharp movements caused by specific events directly affecting an asset's price. Such events might be caused by sudden news or specific market actions.
  
- **Manual Marking is Time-Consuming**: Even if you try to manually mark the price graph, it will take an enormous amount of time, especially when dealing with situations where you only want to test the feasibility of a potential correlation between specific events and their impact on a given asset's price trend.

- **Focus on Short, Strong Oscillations**: Often, many price movements make it difficult to focus on those that matter most. These are the short-term, strong oscillations that usually occur within 10 to 120 seconds, signaling an undeniable sharp price change. 

- **First Open-Source Model for Oscillation Detection**: This is the first open-source model that allows detection of new oscillations. The information produced can be used later to run AI models to investigate whether specific parameters occur during detected oscillations.

### Features

- **Automated Oscillation Detection**: Automatically detects short, sharp oscillations, typically ranging from 10 to 120 seconds.
- **Filtering Noise**: Filters out non-significant fluctuations, enabling users to focus on meaningful price changes.
- **Educational Use Only**: This software is strictly provided for educational and personal research purposes.

## Installation

You can install the library using the provided `setup.py` file. Make sure to have Python 3.7 or later.

1. Clone the repository:
    ```sh
    git clone https://github.com/Buki5/spotter_oscillation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd spotter_oscillation
    ```
3. Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```

Note: The system requires an active internet connection for usage monitoring. No data is stored except for the IP address and MAC address.

## Usage

### Basic Usage Example

The module provides several functions that help in processing oscillations within a financial asset's price data. Below is an example usage of the main function `process_oscillations()`:

```python
import pandas as pd
import pyarrow.parquet as pq

# Load data (for example from a parquet file)
table = pq.read_table("path/to/your/data.parquet")
df = table.to_pandas()

# Process the oscillations for a given asset
from spotter_oscillation.analytics_module import process_oscillations

processed_df = process_oscillations(df, time_column="time", price_column="price", plot=True)
```
In this example, we load a parquet file containing financial asset price data and pass it to the `process_oscillations()` function. The function returns a processed data with oscillation detections and plots the results.

### License Notice
- **Educational Use Only**: This software is provided solely for educational purposes. Any commercial use, including sale, lease, or provision of services using this software, requires explicit permission from the author.
- **Unauthorized Use Prohibited**: Redistribution or modification of this software without the owner's consent is strictly prohibited.
