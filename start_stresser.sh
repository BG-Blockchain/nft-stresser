for wallet in "wallets"/*
do
    gnome-terminal -- proxychains bash stresser.sh $wallet $1 $2
    sleep 1
done