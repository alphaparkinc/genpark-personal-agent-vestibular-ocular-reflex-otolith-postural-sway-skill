# Vestibular Ocular Reflex & Otolith Postural Sway Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `quantify_postural_vestibular_stability`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Analyzes 3-axis accelerometer/gyroscope sway area, Center of Pressure (CoP) velocity, Romberg quotient, and video-HIT VOR gain to preserve longevity balance and prevent falls.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Neuro-Vestibular Balance)`

## MCP Tool Specification
### `quantify_postural_vestibular_stability`
Parameters:
- `sway_area_eyes_open_mm2` (float): Center of pressure sway area with eyes open (mm^2)
- `sway_area_eyes_closed_mm2` (float): Center of pressure sway area with eyes closed (mm^2)
- `cop_mean_velocity_mm_s` (float): Mean velocity of CoP displacement (mm/s)
- `vor_gain_horizontal` (float): Vestibulo-ocular reflex gain (eye velocity / head velocity)
- `patient_age_years` (float): Age of subject in years

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-vestibular-ocular-reflex-otolith-postural-sway-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-vestibular-ocular-reflex-otolith-postural-sway-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
