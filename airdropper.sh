#!/bin/bash
for wallet in "wallets"/*
do
echo "airdrop wallet $wallet"
for i in `seq 1 $1`
   do
      solana airdrop 1 -k $wallet
      sleep 2
   done
done