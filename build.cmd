pyinstaller --onefile --windowed ^
--name="leetcode-daily" ^
--icon="icon.ico" ^
--distpath . ^
--hidden-import=winotify ^
--collect-all winotify ^
src/main.py
