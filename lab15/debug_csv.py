from pathlib import Path
from noteCollection import NoteCollection

csv_path = Path(__file__).resolve().parent / "notesFile.csv"

print("目前工作資料夾：", Path.cwd())
print("CSV 路徑：", csv_path)
print("檔案是否存在：", csv_path.is_file())

if csv_path.is_file():
    try:
        notes = NoteCollection()
        notes.readNotes(csv_path)

        all_notes = notes.getAllNotes()
        print("讀取筆數：", len(all_notes))

        for note in all_notes:
            print(note)

        print("編號 1 的筆記：", notes.getNoteByNumber(1))

    except Exception:
        import traceback
        traceback.print_exc()
else:
    print("找不到 CSV，請確認檔名與位置。")