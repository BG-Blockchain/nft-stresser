#!/bin/bash
for i in  `seq 1 $3`
do
   echo "start minting token $i"
   ts-node ./js/packages/cli/src/candy-machine-v2-cli.ts mint_one_token -e devnet -k $1 --rpc-url https://api.devnet.solana.com -c $2
   echo "wait 5 secs"
   sleep 5
done
