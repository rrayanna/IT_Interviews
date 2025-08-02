# Robotic Package Sorter

A Python utility to classify packages for Thoughtful's robotic automation factory based on volume and mass.

## 🚀 Objective

Classify packages into:
- `STANDARD`: Not bulky or heavy.
- `SPECIAL`: Either bulky or heavy.
- `REJECTED`: Both bulky and heavy.

## 📦 Criteria

- **Bulky**: Volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
- **Heavy**: Mass ≥ 20 kg

## 🛠 Usage

### Run Classification
```python
from sorter import sort
print(sort(100, 100, 100, 10))  # Output: SPECIAL
