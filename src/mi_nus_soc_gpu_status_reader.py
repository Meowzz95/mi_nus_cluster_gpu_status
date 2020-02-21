import paramiko
import json

SOC_USERNAME = "mingda"
PRIVATE_KEY_PATH = paramiko.RSAKey.from_private_key_file("/Users/mimimi/Documents/sshKeys/nus_server_key")

NUS_SERVER_HOSTS = [
    # add more server here
    'xgpb0',
    'xgpb1',
    'xgpb2',


    
    'xgpc0',
    'xgpc1',
    'xgpc2',
    'xgpc3',
    'xgpc4',
    'xgpc5',
    'xgpc6',
    'xgpc7',
    'xgpc8',
    'xgpc9',
    
    'xgpd0',
    'xgpd1',
    'xgpd2',
    'xgpd3',
    'xgpd4',
    'xgpd5',
    'xgpd6',
    'xgpd7',
    'xgpd8',
    'xgpd9',

    'xgpe0',
    'xgpe1',
    'xgpe2',
    'xgpe3',
    'xgpe4',
    'xgpe5',
    'xgpe6',
    'xgpe7',
    'xgpe8',
    'xgpe9',
    'xgpe10',
    'xgpe11',

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
    'xgpf11',
]

def print_status_list(host, status_list_obj):
    for status_obj in status_list_obj:
        status_obj['host'] = host
        print_status(status_obj)

def print_status(status_obj):
    output = ''
    output += f'{status_obj["host"]}.comp.nus.edu.sg'.ljust(23)
    output += str(status_obj['id']).ljust(4)
    output += str(status_obj['name']).ljust(10)
    output += format(status_obj['load'] * 100, '.2f').rjust(6)
    output += format(status_obj['mem_used'], '.0f').rjust(10)
    output += format(status_obj['mem_free'], '.0f').rjust(10)
    output += format(status_obj['mem_total'], '.0f').rjust(10)
    output += format(status_obj['mem_util'] * 100, '.2f').rjust(6)

    print(output)

def print_most_mem_free(status_obj):
    print("*"*10,f"Most Free Mem: {status_obj['host']}","*"*10)
    print_status(status_obj)
    print('\n')

def print_least_util(status_obj):
    print("*"*10,f"Least Utilization: {status_obj['host']}","*"*10)
    print_status(status_obj)
    print('\n')





status_list = []
processed_counter = 0
auth_fail_counter = 0
error_counter = 0
header = ''
header += 'Host'.ljust(23)
header += 'Id'.ljust(4)
header += 'Name'.ljust(10)
header += 'Load(%)'.rjust(6)
header += 'Used(MB)'.rjust(10)
header += 'Free(MB)'.rjust(10)
header += 'Total(MB)'.rjust(10)
header += 'Uti(%)'.rjust(6)
print(header)
print('-' * 80)
for host in NUS_SERVER_HOSTS:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.connect(f'{host}.comp.nus.edu.sg', username=SOC_USERNAME, password='PASSWORD_HERE')
        client.connect(f'{host}.comp.nus.edu.sg', username=SOC_USERNAME, pkey=PRIVATE_KEY_PATH)
        stdin, stdout, stderr = client.exec_command('python3 mi_gpu_slave_script.py')
        for line in stdout:
            status_list_obj = json.loads(line)
            print_status_list(host,status_list_obj)
            for status_obj in status_list_obj:
                # status_obj['host']=host
                status_list.append(status_obj)

        client.close()
        processed_counter+=1
    except paramiko.ssh_exception.AuthenticationException as ex:
        auth_fail_counter+=1
        print(f'Auth fail for {host}, the host may be reserved.')
    except Exception as ex:
        error_counter+=1
        print(f'Unexpected error for {host} error is {ex}')

if len(status_list)>0:
    print(f"Host count: {len(NUS_SERVER_HOSTS)}")
    print(f"Auth fail: {auth_fail_counter} host(s)")
    print(f"Unexpected error: {error_counter} host(s)")
    print(f"Processed : {processed_counter} host(s)")
    status_list.sort(key=lambda x:-x['mem_free'])
    print_most_mem_free(status_list[0])

    status_list.sort(key=lambda x:x['mem_util'])
    print_least_util(status_list[0])





