sns.set_theme(style="darkgrid")


plt.figure(figsize=(10, 6))
grafico = sns.lineplot(x="dia", y="venda", data=gasolina_df, color="blue",linewidth=2.5)

plt.title("Vendas de Gasolina por Dia", fontsize=16, weight='bold')
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Vendas (Litros)", fontsize=12)

plt.show()
