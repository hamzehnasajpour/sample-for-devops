### Run

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 app.py
```

### Requests

```bash
curl -X POST -H "Content-Type: application/json" -d '{"rate": 1.5, "currency_pair": "EURUSD"}' http://localhost:5000/set_rate
```

```bash
curl -X GET http://localhost:5000/get_rate?currency_pair=EUR/USD
```

### Test

```bash
python3 -m unittest test_app.py
```