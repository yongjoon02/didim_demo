import pathlib, sys, pprint

root = pathlib.Path(sys.prefix) / "Lib" / "site-packages"
hits = list(root.rglob("libiomp5md.dll"))      # 재귀 검색
print(f"🔍  발견된 DLL 개수: {len(hits)}\n")
pprint.pprint([str(p.resolve()) for p in hits])