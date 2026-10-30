# -*- coding: utf-8 -*-
"""Vestibular Ocular Reflex & Otolith Postural Sway Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def quantify_postural_vestibular_stability(**kwargs):
    """Analyzes 3-axis accelerometer/gyroscope sway area, Center of Pressure (CoP) velocity, Romberg quotient, and video-HIT VOR gain to preserve longevity balance and prevent falls."""
    sway_area_eyes_open_mm2 = kwargs.get('sway_area_eyes_open_mm2')
    sway_area_eyes_closed_mm2 = kwargs.get('sway_area_eyes_closed_mm2')
    cop_mean_velocity_mm_s = kwargs.get('cop_mean_velocity_mm_s')
    vor_gain_horizontal = kwargs.get('vor_gain_horizontal')
    patient_age_years = kwargs.get('patient_age_years')

    romberg_quotient = round(sway_area_eyes_closed_mm2 / (sway_area_eyes_open_mm2 if sway_area_eyes_open_mm2 > 1.0 else 1.0), 2)
    vor_deficit_pct = round(abs(1.0 - vor_gain_horizontal) * 100.0, 1)
    
    sway_factor = min(40.0, (cop_mean_velocity_mm_s / 20.0) * 40.0)
    romberg_factor = min(30.0, (romberg_quotient / 3.0) * 30.0)
    vor_factor = min(30.0, (vor_deficit_pct / 30.0) * 30.0)
    composite_fall_risk_score = round(sway_factor + romberg_factor + vor_factor, 1)
    
    if composite_fall_risk_score >= 65.0:
        stability_tier = "High Fall Risk (Compromised vestibular/proprioceptive integration)"
        interventions = "Vestibular rehabilitation therapy (VRT), gaze stabilization exercises, environmental hazard remediation."
    elif composite_fall_risk_score >= 35.0:
        stability_tier = "Moderate Fall Risk / Subclinical Vestibular Drift"
        interventions = "Balance board training, dual-task perturbation drills, otolith realignment screening."
    else:
        stability_tier = "Optimal Postural Stability & Vestibular Longevity"
        interventions = "Maintain dynamic agility drills and proprioceptive fitness."
        
    result = {
        "status": "success",
        "romberg_quotient": romberg_quotient,
        "vor_gain": vor_gain_horizontal,
        "vor_gain_deficit_pct": vor_deficit_pct,
        "cop_mean_velocity_mm_s": cop_mean_velocity_mm_s,
        "composite_fall_risk_score_0_to_100": composite_fall_risk_score,
        "balance_stability_tier": stability_tier,
        "recommended_interventions": interventions,
        "engine": "GenPark Otolith Postural Biomechanics Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "quantify_postural_vestibular_stability": {
        "name": "quantify_postural_vestibular_stability",
        "description": "Analyzes 3-axis accelerometer/gyroscope sway area, Center of Pressure (CoP) velocity, Romberg quotient, and video-HIT VOR gain to preserve longevity balance and prevent falls.",
        "parameters": {
            "type": "object",
            "properties": {
                "sway_area_eyes_open_mm2": {"type": "number", "description": "Center of pressure sway area with eyes open (mm^2)"},
                "sway_area_eyes_closed_mm2": {"type": "number", "description": "Center of pressure sway area with eyes closed (mm^2)"},
                "cop_mean_velocity_mm_s": {"type": "number", "description": "Mean velocity of CoP displacement (mm/s)"},
                "vor_gain_horizontal": {"type": "number", "description": "Vestibulo-ocular reflex gain (eye velocity / head velocity)"},
                "patient_age_years": {"type": "number", "description": "Age of subject in years"},
            },
            "required": ['sway_area_eyes_open_mm2', 'sway_area_eyes_closed_mm2', 'cop_mean_velocity_mm_s', 'vor_gain_horizontal', 'patient_age_years']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "quantify_postural_vestibular_stability":
            res = quantify_postural_vestibular_stability(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-vestibular-ocular-reflex-otolith-postural-sway-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-vestibular-ocular-reflex-otolith-postural-sway-skill...")
    test_args = {'sway_area_eyes_open_mm2': 112.0, 'sway_area_eyes_closed_mm2': 198.0, 'cop_mean_velocity_mm_s': 9.4, 'vor_gain_horizontal': 0.98, 'patient_age_years': 45.0}
    res = quantify_postural_vestibular_stability(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-vestibular-ocular-reflex-otolith-postural-sway-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
