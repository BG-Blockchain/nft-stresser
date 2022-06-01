#!/bin/bash

for i in  `seq 1 $1`
do
   echo | solana-keygen new --outfile wallets/$i.json
done
