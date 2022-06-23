import shortuuid
import re

def generate_sample_valid_ref():
    reference = shortuuid.ShortUUID().random(length=10)
    return reference

def generate_sample_invalid_ref():
    reference = shortuuid.ShortUUID().random(length=20)
    return reference

def validate_ref(reference):    
    if len(reference) == 10 and re.match("^[a-zA-Z0-9_]*$", reference):
        return True
    return False
