## aws-tw-sample
AWS Lambda endpoint for executing Alpaca bracket orders.

### Resources

- Uses [AWS Chalice Framework][1] for Serverless Python
- [Alpaca Documentation][2] 

```bash
git config --global credential.helper cache
## 5 mins
git config credential.helper 'cache --timeout=300' 
## 1 week
git config credential.helper 'cache --timeout=604800'

#or

git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git
```

#### Installation

```bash
sudo apt install python3-pip
sudo apt install python3-venv

python3 -m nvenv ~/dev/py/venvs/aws-tw-sample
. ~/dev/py/venvs/aws-tw-sample/bin/activate
pip install chalice
chalice new-project aws-tw
cd aws-tw
tree
chalice deploy

## add requests 
pip install -r requirements.txt
```

#### TradingView message format
```json
{
    "open": {{open}},
    "high": {{high}},
    "low": {{low}},
    "close": {{close}},
    "exchange": "{{exchange}}",
    "ticker": "{{ticker}}",
    "volume": {{volume}},
    "time": "{{time}}",
    "timenow": "{{timenow}}"
}
```
example

```json
{
  "open": 37423.83,
  "high": 37461.05,
  "low": 37409.59,
  "close": 37444.11,
  "exchange": "BITSTAMP",
  "ticker": "BTCUSD",
  "volume": 3.07961616,
  "time": "2022-02-02T17:25:00Z",
  "timenow": "2022-02-02T17:25:45Z"
}
```

### Author

Teocci (teocci@yandex.com)

### License

The code supplied here is covered under the MIT Open Source License.

[1]: https://github.com/aws/chalice
[2]: https://alpaca.markets/docs/api-documentation/api-v2/orders/#request-a-new-order