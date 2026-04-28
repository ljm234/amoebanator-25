from pathlib import Path

def test_log_headers_exist() -> None:
    from legacy_app import load_log  # legacy app.py renamed in Phase 4.5 T1.x to unblock app/ package shadowing
    df = load_log(Path("outputs/diagnosis_log_pro.csv"))
    expected = ["timestamp_tz","case_id","source","physician","age","sex","csf_glucose","csf_protein","csf_wbc","symptoms","pcr","microscopy","exposure","risk_score","risk_label","comments"]
    for c in expected:
        assert c in df.columns
