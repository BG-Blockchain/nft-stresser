# Candymachine NFT Stresser
0. Требования
Ubuntu 20.04+
(Solana)[https://docs.solana.com/ru/cli/install-solana-cli-tools]
Загруженная колекция в candymachine
metaplex

1. устновка зависимостей
`sudo apt update`
`sudo apt upgrade`
`sudo apt install tor proxychains`

2. Создаем кошельки для теста

`bash wallet_creator.sh amount_wallets`

3. Пополняем эти кошельки
`bash airdropper.sh amount_airdrop`

4. Переносим папку wallets, stresser.sh, start_stresser.sh в metaplex/
5. Запускаем бота
`bash start_stresser.sh строка_которую_писали_в_ключе_c колчество_нфт_на_поток`

