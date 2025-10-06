# MutacoesDNA – Anotação Clínica de Mutações Genéticas

## 🔬 Descrição do Projeto
MutacoesDNA é um pipeline em Python para **análise e anotação clínica de variantes genéticas humanas**.  
O projeto integra dados de bancos públicos, como **ClinVar** e **Ensembl**, e gera relatórios estruturados que facilitam a interpretação de mutações para fins de pesquisa e estudos clínicos.

Este projeto faz parte de uma iniciativa de bioinformática aplicada à saúde, combinando **conhecimento clínico e computacional** para análise de DNA humano.

---

## 🧩 Funcionalidades Principais
- Consulta automática de informações de variantes genéticas nos bancos **ClinVar** e **Ensembl**.  
- Combinação de dados clínicos e genômicos em um **relatório estruturado (CSV)**.  
- Facilita a análise de mutações em genes de interesse, por exemplo, o gene GCK.  
- Modular e expansível para integrar outros bancos públicos ou formatos de saída.

---

## ⚡ Tecnologias e Bibliotecas
- **Python 3.7+**  
- **Pandas** – manipulação de tabelas e exportação de dados  
- **APIs ClinVar e Ensembl** – consulta de variantes genéticas  
- Estrutura modular (`utils/clinvar_api.py`, `utils/ensembl_api.py`)  

---

