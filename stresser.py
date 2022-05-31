from multiprocessing.pool import ThreadPool
import subprocess
import glob

wallets = glob.glob("./wallets/*")
CANDY_MACHINE_CLI_PATH = "/home/user/candymachine_test/metaplex/js/packages/cli/src/candy-machine-v2-cli.ts"
CACHED_NAME = "example_upload"
command = "ts-node "+CANDY_MACHINE_CLI_PATH+" mint_one_token -e devnet -k {0} -c "+CACHED_NAME
works = []


for i in range(60):
    for wallet in wallets:
        works.append([command.format(wallet), i])


def work(job):
    mint_subporcess=subprocess.call(job, shell=True, stdout=subprocess.PIPE)
    stdout, stderr = mint_subprocess.communicate()
    exit_code = mint_subprocess.wait()
    print(stdout, stderr, exit_code)



num = 10  # set to the number of workers you want (it defaults to the cpu count of your machine)
tp = ThreadPool(num)
for job in works:
    tp.apply_async(work, (job[0],))

tp.close()
tp.join()
