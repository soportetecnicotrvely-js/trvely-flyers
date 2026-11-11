"""Genera index.html a partir de src/template.html + data/assets.json + data/hoteles.json.
Uso:  python tools/build.py
"""
import json, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
t = (raiz / "src/template.html").read_text(encoding="utf-8")
a = json.loads((raiz / "data/assets.json").read_text(encoding="utf-8"))
a["hotels"] = json.loads((raiz / "data/hoteles.json").read_text(encoding="utf-8"))
(raiz / "index.html").write_text(t.replace("__ASSETS__", json.dumps(a, ensure_ascii=False)), encoding="utf-8")
print("index.html generado")
