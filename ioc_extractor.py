import re
from pathlib import Path
import argparse

RE_IPV4 = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
RE_DOMAIN = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
RE_URL = r'https?://[^\s]+'
RE_EMAIL = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
RE_HASH = r'\b[a-fA-F0-9]{32,64}\b'

parser = argparse.ArgumentParser(description="IOC Extractor Tool")
parser.add_argument("-i", "--input", required=True, help="Input text file")
args = parser.parse_args()

text = Path(args.input).read_text(errors="ignore")

iocs = {
    "ipv4": re.findall(RE_IPV4, text),
    "domains": re.findall(RE_DOMAIN, text),
    "urls": re.findall(RE_URL, text),
    "hashes": re.findall(RE_HASH, text),
    "emails": re.findall(RE_EMAIL, text),
}

print("\n[+] Extracted IOCs:\n")

for key, values in iocs.items():
    print(f"== {key.upper()} ==")
    if values:
        for v in set(values):
            print(v)
    else:
        print("(none)")
    print()
