mkdir -p vendas

cp ~/Sprints/Sprint1/Desafio/ecommerce/dados_de_vendas.csv vendas/

mkdir -p vendas/backup

data=$(date +%Y%m%d)

cp vendas/dados_de_vendas.csv vendas/backup/dados-$data.csv

mv vendas/backup/dados-$data.csv vendas/backup/backup.dados-$data.csv

relatorio="vendas/backup/relatorio.txt"

echo "Data do sistema: $(date +%Y/%m/%d\ %H:%M)" > $relatorio

primeira_data=$(head -n 2 vendas/backup/backup.dados-$data.csv | awk -F, '{print $5}')
ultima_data=$(tail -n 1 vendas/backup/backup.dados-$data.csv | awk -F, '{print $5}')
echo "Data do primeiro registro: $primeira_data" >> $relatorio
echo "Data do último registro: $ultima_data" >> $relatorio

total_itens=$(cut -d, -f2 vendas/backup/backup.dados-$data.csv | sort | uniq | wc -l)
echo "Quantidade total de itens diferentes vendidos: $total_itens" >> $relatorio

echo "Primeiras 10 linhas do arquivo:" >> $relatorio
head -n 10 vendas/backup/backup.dados-$data.csv >> $relatorio

zip vendas/backup/backup-dados-$data.zip vendas/backup/backup.dados-$data.csv

rm vendas/backup/backup.dados-$data.csv
rm vendas/dados_de_vendas.csv

echo "Processo concluído! Arquivo de backup criado em vendas/backup/backup.dados-$data.csv"

