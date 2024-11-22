sns.set_theme(style="darkgrid")

grafico = sns.lineplot(x="dia", y="venda", palette='pastel', data=gasolina_df)