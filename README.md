# NUS SoC cluster GPU status checker

## Sample output

![Sample Output](https://github.com/Meowzz95/mi_nus_cluster_gpu_status/blob/master/images/sample_output.png)

## Usage

1. Clone the project to one of the SoC servers' home directory. The home directory is shared across the cluster.
2. Make sure dependencies are installed `pip3 install -r req.txt`
3. Fill in your private key path in `mi_nus_soc_gpu_status_reader.py` if you are using key pair to authenticate, if not use this line instead(uncomment)
```
client.connect(f'{host}.comp.nus.edu.sg', username='mingda', password='PASSWORD_HERE')
```

Now run `mi_nus_soc_gpu_status_reader.py`
:)


## TODO

- ~Multi-thread?~
- CLI args?

# Please STAR if you find it useful!!!
Thanks!!!

# Contributor 

[@YipingRuan](https://github.com/YipingRuan)

Thanks to him, the output looks a lot nicer now! 🎉

[@lv2020](https://github.com/lv2020)

Thanks to lv2020, the program now executes in a thread pool, much faster!
