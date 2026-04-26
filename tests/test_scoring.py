from pathlib import Path

def test_log_headers_exist() -> None:
    from app import load_log
    df = load_log(Path("outputs/diagnosis_log_pro.csv"))
    expected = ["timestamp_tz","case_id","source","physician","age","sex","csf_glucose","csf_protein","csf_wbc","symptoms","pcr","microscopy","exposure","risk_score","risk_label","comments"]
    for c in expected:
        assert c in df.columns
