relatorio_final="vendas/backup/relatorio_final.txt" > $relatorio_final

echo "Relatório Consolidado de Vendas" >> $relatorio_final
echo "==============================" >> $relatorio_final

for relatorio in vendas/backup/relatorio.txt; do
    echo "Conteúdo de: $relatorio" >> $relatorio_final
    cat "$relatorio" >> $relatorio_final
    echo "" >> $relatorio_final  # Adicionar uma linha em branco entre os relatórios
done

echo "Relatório final gerado em $relatorio_final"
