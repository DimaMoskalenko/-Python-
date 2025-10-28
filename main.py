def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file
# Імена файлів
file1_name = "TF17_1.txt"
file2_name = "TF17_2.txt"
file3_name = "TF17_3.txt"
# Створення TF17_1 з рядками різної довжини
file_1_w = Open(file1_name, "w")
if file_1_w != None:
    file_1_w.write("abc123\n456defgh\nijk7890lmn\n!@#12")
    print("Information was successfully added to TF17_1.txt!")
    file_1_w.close()
    print("File TF17_1.txt was closed!")
# Читання TF17_1 і обробка → TF17_3
file_1_r = Open(file1_name, "r")
file_3_w = Open(file3_name, "w")
if file_1_r != None and file_3_w != None:
    content = file_1_r.read()
    digits = ''.join([c for c in content if c.isdigit()])
    others = ''.join([c for c in content if not c.isdigit() and c != '\n'])
    file_3_w.write(digits + '\n' + others)
    file_1_r.close()
    file_3_w.close()
    print("TF17_3.txt was created!")
# Читання TF17_3 і запис у TF17_2 по 10 символів
file_3_r = Open(file3_name, "r")
file_2_w = Open(file2_name, "w")
if file_3_r != None and file_2_w != None:
    data = file_3_r.read().split('\n')
    digits_part = data[0]
    others_part = data[1]
    file_2_w.write(digits_part + '\n')
    for i in range(0, len(others_part), 10):
        file_2_w.write(others_part[i:i+10] + '\n')
    file_3_r.close()
    file_2_w.close()
    print("TF17_2.txt was created!")
# Виведення TF17_2 по рядках
print("Final content of TF17_2:")
file_2_r = Open(file2_name, "r")
if file_2_r != None:
    for line in file_2_r:
        print(line.strip())
    file_2_r.close()
    print("File TF17_2.txt was closed!")