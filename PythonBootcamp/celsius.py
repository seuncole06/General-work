def convert_temperature(temp: float, target_unit: str) -> float:

    target_unit = target_unit.lower()
    units = "cf"

    if target_unit not in units:
        return "Target unit must be either Fah or Cel"
    
    elif 