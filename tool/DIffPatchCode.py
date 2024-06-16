# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
55 48 89 E5 41 57 41 56 41 55 41 54 53 48 83 EC 78 48 8B 05 88 88 69 00 48 8B 00 48 89 45 D0 48 8D 3D BA FD 7B 00 E8 25 79 EC FF 48 8B 40 F8 48 8B 40 40 48 89 E3 48 83 C0 0F 48 83 E0 F0 48 29 C3 48 89 DC 31 FF E8 E7 AF 59 00 49 89 C6 4C 8B 60 F8 49 8B 44 24 40 48 89 E1 48 83 C0 0F 48 83 E0 F0 48 29 C1 48 89 4D A8 48 89 CC 48 89 E1 48 29 C1 48 89 4D A0 48 89 CC 49 89 E7 49 29 C7 4C 89 FC 31 FF E8 67 6B F5 FF 49 89 C5 48 89 D8 31 FF 48 BE 00 00 00 00 00 00 00 E0 E8 00 68 F5 FF 48 89 DF BE 01 00 00 00 4D 89 F5 4C 89 F2 41 FF 54 24 30 83 F8 01 75 0D 48 89 DF E8 A0 33 ED FF E9 05 04 00 00 4C 89 FF 48 89 DE 4C 89 EA 4C 89 6D 88 41 FF 54 24 20 48 BF 2E 6C 69 63 65 6E 73 65 48 BE 6D 61 63 00 00 00 00 EB 4C 8B 75 A0 4C 89 F0 4C 89 65 98 4D 89 FD E8 FE AE 59 00 48 8B 3D 5B C1 72 00 E8 D2 C8 59 00 48 8B 35 37 57 72 00 48 89 85 70 FF FF FF 48 89 C7 E8 0A C6 59 00 48 89 C7 E8 26 C6 59 00 48 89 C3 4D 89 F5 E8 ED AE 59 00 49 89 D5 48 89 C7 48 89 D6 E8 13 B4 59 00 4C 89 7D 90 4C 8B 75 88 49 89 C4 4C 89 EF E8 DA C7 59 00 48 8B 35 A5 5F 72 00 48 89 DF 4C 89 E2 E8 C4 C5 59 00 41 89 C5 4C 8B 3D 50 88 69 00 48 89 DF 41 FF D7 4C 89 E7 41 FF D7 45 84 ED 0F 84 68 01 00 00 48 8B 5D A8 48 89 DF 4C 89 F2 4C 8B 75 A0

55 48 89 E5 41 57 41 56 41 55 41 54 53 48 81 EC ?? 00 00 00 48 8D 3D ?? ?? 79 00 E8 ?? ?? EB FF 48 8B 40 F8 48 8B 40 40 48 89 E3 48 83 C0 0F 48 83 E0 F0 48 29 C3 48 89 DC 31 FF E8 ?? ?? ?? 00 49 89 C4 ?? 8B ?? F8 ?? ?? ?? ?? 48 ?? ?? ?? ?? ?? ?? 48 83 ?? ?? 48 ?? ?? ?? ?? ?? ?? ?? 89 ?? 48 89 E1 48 29 C1 48 89 4D ?? 48 89 CC 49 89 E6 49 29 C6 4C 89 F4 31 FF E8 ?? ?? F4 FF 49 89 C5 48 ?? ?? ?? ?? ?? ?? 00 00 ?? ?? ?? ?? ?? ?? E8 ?? ?? F4 FF ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??
"""

data1 = []

for i in data.split("\n"):
    if i == "":
        continue
    else:
        data1.append(i)
        if len(data1) > 1:
            res = " ".join(
                [
                    d1 if d1 == d2 else "??"
                    for d1, d2 in zip(data1[0].split(), data1[1].split())
                ]
            )
            data1 = [res]

print(data1[0])
