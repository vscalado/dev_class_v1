from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str

# Fatores de conversão (usando metros como base)
LENGTH_FACTORS = {
    "m": 1,
    "cm": 0.01,
    "km": 1000,
    "mm": 0.001
}

# Fatores de conversão (usando litros como base)
VOLUME_FACTORS = {
    "l": 1,
    "ml": 0.001,
    "m3": 1000,
    "cm3": 0.001
}

@router.post("/length")
async def convert_length(conversion: ConversionRequest):
    if conversion.from_unit not in LENGTH_FACTORS or conversion.to_unit not in LENGTH_FACTORS:
        raise HTTPException(status_code=400, detail="Unidade inválida")
    
    # Converte para a unidade base (metros)
    base_value = conversion.value * LENGTH_FACTORS[conversion.from_unit]
    
    # Converte da unidade base para a unidade desejada
    result = base_value / LENGTH_FACTORS[conversion.to_unit]
    
    return {
        "result": result,
        "from": conversion.from_unit,
        "to": conversion.to_unit,
        "original_value": conversion.value
    }

@router.post("/volume")
async def convert_volume(conversion: ConversionRequest):
    if conversion.from_unit not in VOLUME_FACTORS or conversion.to_unit not in VOLUME_FACTORS:
        raise HTTPException(status_code=400, detail="Unidade inválida")
    
    # Converte para a unidade base (litros)
    base_value = conversion.value * VOLUME_FACTORS[conversion.from_unit]
    
    # Converte da unidade base para a unidade desejada
    result = base_value / VOLUME_FACTORS[conversion.to_unit]
    
    return {
        "result": result,
        "from": conversion.from_unit,
        "to": conversion.to_unit,
        "original_value": conversion.value
    }