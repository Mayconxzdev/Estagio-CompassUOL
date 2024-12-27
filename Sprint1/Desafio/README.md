
# Etapas


1. Etapa criando o script processamento_de_vendas.sh

    Nessa etapa pode-se perceber com esse código:

```
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
```
Obtive esse retorno

   ![Captura de tela 2024-11-15 213328](https://github.com/user-attachments/assets/561c2f5e-597c-423d-89f7-62d49e89b60d)

   
 2. Já nessa etapa criando o script consolidador_de_processamento_de_vendas.sh
  
  ```
relatorio_final="vendas/backup/relatorio_final.txt" > $relatorio_final

echo "Relatório Consolidado de Vendas" >> $relatorio_final
echo "==============================" >> $relatorio_final

for relatorio in vendas/backup/relatorio.txt; do
    echo "Conteúdo de: $relatorio" >> $relatorio_final
    cat "$relatorio" >> $relatorio_final
    echo "" >> $relatorio_final  # Adicionar uma linha em branco entre os relatórios
done

echo "Relatório final gerado em $relatorio_final"


  ```

 Obtive esse retorno
    

![Captura de tela 2024-11-15 213317](https://github.com/user-attachments/assets/41fb2b10-709c-4ac2-aa98-486736ce5f6d)

Indicando que deu tudo certo para os dois

