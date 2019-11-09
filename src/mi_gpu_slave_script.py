import GPUtil
import json

def get_gpu_status_obj(gpu:GPUtil.GPU):
    return {
        'id':gpu.id,
        'name':gpu.name,
        'load':gpu.load,
        'mem_free':gpu.memoryFree,
        'mem_total':gpu.memoryTotal,
        'mem_used':gpu.memoryUsed,
        'mem_util':gpu.memoryUtil,
    }
devices = GPUtil.getGPUs()
gpu_status_obj_list = []
for device in devices:
    gpu_status_obj = get_gpu_status_obj(device)
    gpu_status_obj_list.append(gpu_status_obj)

print(json.dumps(gpu_status_obj_list))
