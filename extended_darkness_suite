extended_darkness_suite/
├── README.md
├── .gitignore
├── requirements.txt
├── deploy/
│   └── deploy_all.sh
├── config/
│   ├── app_config.env
│   └── app_config.env.bak
├── injector/
│   └── inject_backdoor_key.py
├── defender/
│   └── file_hash_guardian.py
├── monitor/
│   └── realtime_audit_tui.py
├── logger/
│   └── rogue_key_logger.py
├── beacon/
│   ├── encrypted_beacon_client.py
│   └── encrypted_beacon_server.py
├── encryptor/
│   └── encrypt_note.py
├── ml/
│   └── anomaly_detector.py
├── tests/
│   └── test_config_integrity.py
├── .github/
│   └── workflows/
│       └── ci.yml

# Sample README.md

# Extended Darkness Suite
A modular cryptographic and config-monitoring framework for offensive and defensive security simulation.

## Features
- 🔐 Encrypted secret/key generation
- 🕵️ Insider threat simulation (key injection)
- 🛡️ File integrity and hash monitoring
- 📊 Real-time TUI monitoring dashboard
- 🧠 ML-based anomaly detection

## Installation
```bash
git clone https://github.com/yourusername/extended_darkness_suite.git
cd extended_darkness_suite
pip install -r requirements.txt
```

## Usage
Run the deploy script to simulate:
```bash
bash deploy/deploy_all.sh
```

### Individual Components
```bash
# Defender
python defender/file_hash_guardian.py

# Injector
python injector/inject_backdoor_key.py

# Monitor
python monitor/realtime_audit_tui.py
```

### ML Anomaly Detector
```bash
python ml/anomaly_detector.py --log monitor.log
```

## CI Integration
### .github/workflows/ci.yml
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install deps
      run: pip install -r requirements.txt
    - name: Run tests
      run: python -m unittest discover -s tests
```

## ML: anomaly_detector.py (Simplified)
```python
import json
from sklearn.ensemble import IsolationForest

with open('monitor.log') as f:
    logs = [json.loads(line) for line in f if line.strip()]

features = [[log['suspicious'], log['key_count']] for log in logs]
clf = IsolationForest()
clf.fit(features)
results = clf.predict(features)
for log, result in zip(logs, results):
    if result == -1:
        print("⚠️ Anomaly detected:", log)
```

## Requirements
```
curses
sklearn
```

---

Would you like this zipped or published to a GitHub repo via a Gist or export?
