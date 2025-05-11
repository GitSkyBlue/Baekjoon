import win32job
import subprocess
import sys
import locale
import time  # time 모듈 추가

def run_with_memory_limit(script_path, input_path, memory_limit_mb=64):
    memory_limit_bytes = memory_limit_mb * 1024 * 1024

    # 실행 시간 측정을 시작
    start_time = time.time()

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

    # 실행 시간 계산
    end_time = time.time()
    execution_time = end_time - start_time  # 실행 시간 (초)

    encoding = locale.getpreferredencoding()

    print("📤 STDOUT:\n", stdout.decode(encoding, errors='replace'))
    print("❗ STDERR:\n", stderr.decode(encoding, errors='replace'))
    print(f"⏱ 실행 시간: {execution_time:.2f}초")  # 실행 시간 출력


# 실행
if __name__ == "__main__":
    run_with_memory_limit("./Class6/1019.py", "input.txt", memory_limit_mb=128)