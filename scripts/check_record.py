"""Check one lab record against its schema and domain rules."""
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def domain_error(record):
    if record["elapsed_ms"] < 0:
        return "Crossing precedes the heat start"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    schema = json.loads((ROOT / "contracts/record.schema.json").read_text(encoding="utf8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    try:
        record = json.loads(args.record.read_text(encoding="utf-8-sig"))
        errors = [error.message for error in validator.iter_errors(record)]
        if not errors:
            message = domain_error(record)
            if message:
                errors.append(message)
    except (OSError, UnicodeError, ValueError) as error:
        errors = [str(error)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Record accepted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
