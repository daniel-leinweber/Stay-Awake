# Stay-Awake

Python script to move your mouse and press the shift key every 60 seconds,
to keep your PC awake when you are away.

## Installing Dependencies

This software uses [PyAutoGui](https://github.com/asweigart/pyautogui) as the
driver behind the movement.

### 1. Create a virtual Environment

```python
python3 -m venv .venv
```

### 2. Activate the virtual environment

```python
source .venv/bin/activate
```

### 3. Install dependencies

```python
pip install -r requirements.txt
```

## Running the script

Leave the script running in a terminal:

```python
python src/awake.py
```
