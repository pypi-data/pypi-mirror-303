# OCFINANCE (Works with Cryptoquant)

`ocfinance` is a python package that enables you to download on-chain data from various sources, including Cryptoquant, CheckOnChain, etc.

## Features
- **Easy Data Download**: Download on-chain data from various sources with a single line of code.
- **CSV Export**: Save data as CSV files for easy analysis in Excel or other tools.
- **Pandas Integration**: Work with data directly as a pandas DataFrame for simple manipulation and analysis.
- **Customizable Queries**: Specify start and end date parameters.

## Installation
To install the `ocfinance` package, use pip:
```bash
pip install ocfinance
```

## Supported Websites
- [CheckOnChain](https://charts.checkonchain.com/)
- [ChainExposed](https://chainexposed.com/)
- [Woocharts](https://woocharts.com/)
- [Cryptoquant](https://cryptoquant.com/) (_follow the guide below_)
- [Bitbo Charts](https://charts.bitbo.io/)
- [Bitcoin Magazine Pro](https://www.bitcoinmagazinepro.com)

## Usage
To download the data of a chart, simply obtain the URL and pass it to the download function

```python
import ocfinance as of

# Download the data from the specified URL
data = of.download("https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html")

# Usage examples
# Export as CSV
data.to_csv('out.csv')

# Plot
data.plot()
```

#### Advanced usage
```python
# Filter by dates (Pass dates in YYYY-mm-dd format)
filtered = of.download(
    "https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html",
    start='2023-01-01',
    end='2023-12-31'
)
```

## Cryptoquant guide
To access data from Cryptoquant, you must have an account. **Your email and password are required** and should be passed to the download function (preferably using environment variables)

```python
import os
import ocfinance as of

# Setup environment variables
email = os.getenv('CRYPTOQUANT_EMAIL')
password = os.getenv('CRYPTOQUANT_PASSWORD')

# Download the data
data = of.download(
    "https://cryptoquant.com/analytics/query/66451fd6f3cac64b85386229?v=66451fd6f3cac64b8538622b",
    email=email,
    password=password
)
```
To obtain the url, click the source button and copy the URL of the page.

![Click the source button](/assets/cryptoquant_step1.png)
![Copy the url](/assets/cryptoquant_step2.png)

## Contributing
If you would like to contribute to the project, feel free to submit a pull request or open an issue for discussion.

## Running Tests
#### Optional
To run integration tests for Cryptoquant, you need to provide your account's email and password in a `.env` file. Copy the provided `.env.sample` file, rename it to `.env`, and fill in your credentials. Without this file, the tests using it will be skipped.

#### Running the tests
1. Clone the repository
```bash
git clone https://github.com/dhruvan2006/ocfinance
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Run the tests
```bash
pytest
```
