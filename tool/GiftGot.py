import subprocess

data = """
horizonl\t000cde9daabe484630396d3b92e34e95
"""

sourceCode = ""
sourceCodeBackup = ""

nickNameCode = 'NSString *devName = @"<UserNickName>";'
nickSerialCode = (
    'NSString *devSerial = @"<UserDeviceIdByUserCustomAndMachineAutomaticGenerate>";'
)


for i in data.split("\n"):
    if i == "":
        continue
    i1 = i.split("	")
    nick = i1[0]
    code = i1[1].split("/")[0]

    with open("/Volumes/data/macOS_HookWorkSpace/InjectLib/SurgeA.m", "r") as f:
        sourceCode = f.read()

    # 替换关键词
    sourceCode = sourceCode.replace(
        nickNameCode, nickNameCode.replace("<UserNickName>", nick)
    )
    sourceCode = sourceCode.replace(
        nickSerialCode,
        nickSerialCode.replace(
            "<UserDeviceIdByUserCustomAndMachineAutomaticGenerate>", code
        ),
    )

    with open("/Volumes/data/macOS_HookWorkSpace/InjectLib/src/Apps/Surge.m", "w") as f:
        f.write(sourceCode)

    # 执行shell
    subprocess.run(
        "rm -rf /Volumes/data/macOS_HookWorkSpace/InjectLib/cmake-build/BuildOut/Release/91QiuChenly.dylib && cd /Volumes/data/macOS_HookWorkSpace/InjectLib && sh /Volumes/data/macOS_HookWorkSpace/InjectLib/build.sh",
        shell=True,
    )

    subprocess.run(
        f"cd /Volumes/data/macOS_HookWorkSpace/InjectLib/cmake-build/BuildOut/Release && mv 91QiuChenly.dylib '{nick}-91QiuChenly.dylib'",
        shell=True,
    )

    sourceCode = sourceCodeBackup
