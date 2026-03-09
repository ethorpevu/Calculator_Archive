import glob, os

root = os.path.abspath(os.path.dirname(__file__))
# restrict to specified directories
subdirs = ["google", "meta-llama", "microsoft", "mistralai"]
files = []
for sd in subdirs:
    path = os.path.join(root, sd)
    if os.path.isdir(path):
        files.extend(glob.glob(os.path.join(path, "**", "*.json"), recursive=True))

# read raw contents preserving formatting
raw_list = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        raw = fp.read().strip()
    raw_list.append(raw)

out = os.path.join(root, 'merged_json.json')
with open(out, 'w', encoding='utf-8') as fp:
    fp.write("[\n")
    for i, raw in enumerate(raw_list):
        fp.write(raw)
        if i != len(raw_list) - 1:
            fp.write(',\n')
    fp.write("\n]\n")

print(f"merged {len(raw_list)} files into {out}")
