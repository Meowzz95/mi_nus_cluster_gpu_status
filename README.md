# NUS SoC cluster GPU status checker

## Sample output
```
========== xgpf3 ==========
------- 0 Tesla T4 -------
Load: 0.0
Memory Free: 15079.0MB
Memory Used: 0.0MB / 15079.0MB  0.00%


Auth fail for xgpf7, the host may be reserved.
========== xgpf8 ==========
------- 0 Tesla T4 -------
Load: 1.0
Memory Free: 680.0MB
Memory Used: 14399.0MB / 15079.0MB  95.49%


========== xgpf9 ==========
------- 0 Tesla T4 -------
Load: 0.07
Memory Free: 444.0MB
Memory Used: 14635.0MB / 15079.0MB  97.06%


========== xgpf10 ==========
------- 0 Tesla T4 -------
Load: 1.0
Memory Free: 49.0MB
Memory Used: 15030.0MB / 15079.0MB  99.68%
------- 1 Tesla T4 -------
Load: 1.0
Memory Free: 6.0MB
Memory Used: 15073.0MB / 15079.0MB  99.96%


========== xgpf11 ==========
------- 0 Tesla T4 -------
Load: 0.05
Memory Free: 265.0MB
Memory Used: 14814.0MB / 15079.0MB  98.24%
------- 1 Tesla T4 -------
Load: 0.43
Memory Free: 351.0MB
Memory Used: 14728.0MB / 15079.0MB  97.67%


********** Most Free Mem: xgpf3 **********
------- 0 Tesla T4 -------
Load: 0.0
Memory Free: 15079.0MB
Memory Used: 0.0MB / 15079.0MB  0.00%


********** Least Utilization: xgpf3 **********
------- 0 Tesla T4 -------
Load: 0.0
Memory Free: 15079.0MB
Memory Used: 0.0MB / 15079.0MB  0.00%
```

## Usage

1. Upload `mi_gpu_slave_script.py` to your home directory. Upload to one server is enough as the home directory is shared.
2. Make sure dependencies are installed `pip3 install -r req.txt`
3. Fill in your private key path in `mi_nus_soc_gpu_status_reader.py` if you are using key pair to authenticate, if not use this line instead(uncomment)
```
client.connect(f'{host}.comp.nus.edu.sg', username='mingda', password='PASSWORD_HERE')
```

Now run `mi_nus_soc_gpu_status_reader.py`
:)


## TODO

- Multi-thread?
- CLI args?

# Please STAR if you find it useful!!!
Thanks!!!

# Contributor 

@YipingRuan 
Thanks to him, the output looks a lot nicer now! 🎉

