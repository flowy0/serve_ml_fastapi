Install the Kaggle Python API as follows.

```
pip install kaggle
```

Save your API Token and update your shell env variables.

See [See Kaggle Github for details](https://github.com/Kaggle/kaggle-api#api-credentials)


We can now download the dataset via the API

```shell
kaggle datasets list -s camnugent/california-housing-prices 
kaggle datasets download camnugent/california-housing-prices -p data/raw
unzip -d data/raw/ data/raw/california-housing-prices.zip 
```



I have also placed this script in `scripts/get_kaggle_data.sh`