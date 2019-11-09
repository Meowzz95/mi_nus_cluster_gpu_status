import paramiko
import json
NUS_SERVER_HOSTS = [
    # add more server here
    'xgpf0',
    'xgpf1',
    'xgpf2',
    'xgpf3',
    'xgpf4',
    'xgpf5',
    'xgpf6',
    'xgpf7',
    'xgpf8',
    'xgpf9',
    'xgpf10',
    'xgpf11'
]

def print_status_list(host, status_list_obj):
    print("="*10,host,"="*10)
    for status_obj in status_list_obj:
        print_status(status_obj)
    print("\n")

def print_status(status_obj):
    print("-" * 7, status_obj['id'], status_obj['name'], "-" * 7)
    print(f"Load: {status_obj['load']}")
    print(f"Memory Free: {status_obj['mem_free']}MB")
    util = "{0:.2f}".format(float(status_obj['mem_util']) * 100)
    print(f"Memory Used: {status_obj['mem_used']}MB / {status_obj['mem_total']}MB  {util}%")

def print_most_mem_free(status_obj):
    print("*"*10,f"Most Free Mem: {status_obj['host']}","*"*10)
    print_status(status_obj)
    print('\n')

def print_least_util(status_obj):
    print("*"*10,f"Least Utilization: {status_obj['host']}","*"*10)
    print_status(status_obj)
    print('\n')





status_list = []
key = paramiko.RSAKey.from_private_key_file("/Users/mimimi/Documents/sshKeys/nus_server_key")
for host in NUS_SERVER_HOSTS:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.connect(f'{host}.comp.nus.edu.sg', username='mingda', password='PASSWORD_HERE')
        client.connect(f'{host}.comp.nus.edu.sg', username='mingda', pkey=key)
        stdin, stdout, stderr = client.exec_command('python3 mi_gpu_slave_script.py')
        for line in stdout:
            status_list_obj = json.loads(line)
            print_status_list(host,status_list_obj)
            for status_obj in status_list_obj:
                status_obj['host']=host
                status_list.append(status_obj)

        client.close()
    except paramiko.ssh_exception.AuthenticationException as ex:
        print(f'Auth fail for {host}, the host may be reserved.')
    except Exception as ex:
        print(f'Unexpected error for {host} error is {ex}')

if len(status_list)>0:
    status_list.sort(key=lambda x:-x['mem_free'])
    print_most_mem_free(status_list[0])

    status_list.sort(key=lambda x:x['mem_util'])
    print_least_util(status_list[0])





