# Cron Persistence Simulator

**Author:** Seneca
**Repo:** [redteam_toolkit](https://github.com/Jordanjohnson1999/redteam-toolkit)
**Tool:** cron_persistence.py
**Type:** Linux Persistence Simulation Tool
**Purpose:** Ethical Red Team education & practice
---

### Ovoerview

This tool simulates a common Linux persistence technique using the `cron` schduler.

It allows users to:
- Add a harmless `@reboot` cron job (mimicking attacker persistence)
- View current cron jobs
- Remove the simulated persistence

The job writes a simple job message to `~/cron_persistence_log.txt` every time the system boots - simulating post-exploitation behavior in a safe, ethicl way.
---

### Features
- [x] Simulates cron-based persistence
- [x] Prevents dublicate cron job entries
- [x] Allows cleanup/removal of the job
- [x] Educational and ethical by design
- [x] Terminal-based interface for real-world realism
---

## Usage
Run the tool with

```bash
python3 cron_persistence.py
