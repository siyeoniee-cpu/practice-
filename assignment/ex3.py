src = open("input3.txt", "r", encoding="utf-8")
dst = open("copy.txt", "w", encoding="utf-8")
for line in src:
     dst.write(line)
src.close()
dst.close()
print("파일 복사가 완료되었습니다.")