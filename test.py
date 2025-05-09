import win32job
import subprocess
import sys
import locale

def run_with_memory_limit(script_path, input_path, memory_limit_mb=64):
    memory_limit_bytes = memory_limit_mb * 1024 * 1024

    # 프로세스 생성 (일시중지 없이 바로 실행)
    proc = subprocess.Popen(
        [sys.executable, script_path],
        stdin=open(input_path, 'r'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Job 객체 생성 및 제한 설정
    job = win32job.CreateJobObject(None, "")
    info = win32job.QueryInformationJobObject(job, win32job.JobObjectExtendedLimitInformation)
    info['BasicLimitInformation']['LimitFlags'] = win32job.JOB_OBJECT_LIMIT_PROCESS_MEMORY
    info['ProcessMemoryLimit'] = memory_limit_bytes
    win32job.SetInformationJobObject(job, win32job.JobObjectExtendedLimitInformation, info)

    # 프로세스를 Job에 할당
    win32job.AssignProcessToJobObject(job, proc._handle)

    # 결과 수집
    stdout, stderr = proc.communicate()

    encoding = locale.getpreferredencoding()

    print("📤 STDOUT:\n", stdout.decode(encoding, errors='replace'))
    print("❗ STDERR:\n", stderr.decode(encoding, errors='replace'))


# 실행
if __name__ == "__main__":
    run_with_memory_limit("./Class2/1654.py", "input.txt", memory_limit_mb=128)
