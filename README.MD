# Red Team Toolkit - SOC & Recon Tools

This repo contains small, interview-friendly tools and playbook snippets used during practice:
- `soc_log_parser.py` - Apache / Linux auth log parser, IOC matching, CSV export
- small sample logs & IOC lists for testing
- future: geoip enrichment, JSON output, windows parsing helper

---

## Quick start / usage

Run the SOC parser:

```bash
# parse a sample Apache access log
python3 soc_log_parser.py sample.log

# parse auth log
python3 soc_log_parser.py authsample.log

# include IOC file (one item per line)
python3 soc_log_parser.py sample.log --iocs iocs.txt

# debug: only parse first N lines
python3 soc_log_parser.py sample.log --limit 100

---

## Outputs

When you run the parser it writes the following artifacts into the `out/` directory:

- `out/events.csv` - normalized event rows (one event per line, CSV)
- `out/summary.csv` - aggregated stats (total events, SSH failed/accepted counts, top attacker IPs, HTTP status counts, IOC hits)

---

## FIles included (examples)

- `soc_log_parser.py` - main parser script (Apache + linux auth parsers, IOC matching)
- `sample.log` - sample Apache combined-format log lines for testing
- `authsample.log` - sample Linux auth/sshd lines for testing
- `iocs.txt` - example IOC file (one IOC per line)
- `out/` parser outputs (generated; **should be ignored** in the repo)
