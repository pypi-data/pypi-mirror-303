from typing import Dict, List


def get_text(record, key, default=""):
    fields = record["fields"]
    value = ''.join([ x["text"] for x in fields.get(key, []) ])
    if not value.strip():
        return default
    return value

def get_link_ids(record: Dict, key: str) -> List[str]:
    fields = record["fields"]
    return fields[key]["link_record_ids"]

