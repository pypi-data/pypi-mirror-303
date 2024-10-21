from pydantic import BaseModel

CUSTOM: str
N2V: str
N2V2: str
STRUCT_N2V: str
STRUCT_N2V2: str
N2N: str
CARE: str
N2V_DESCRIPTION: str

class AlgorithmDescription(BaseModel):
    description: str

class N2VDescription(AlgorithmDescription):
    description: str

class N2V2Description(AlgorithmDescription):
    description: str

class StructN2VDescription(AlgorithmDescription):
    description: str

class StructN2V2Description(AlgorithmDescription):
    description: str

class N2NDescription(AlgorithmDescription):
    description: str

class CAREDescription(AlgorithmDescription):
    description: str
