import wget

link = 'https://www.ans.gov.br/images/stories/Legislacao/rn/Anexo_I_Rol_2021RN_465.2021_RN647.2025.pdf'
#link do site para fazer o dowload
wget.download(link, 'teste.pdf')
#nomedoarquivo.extençãoparasersalvo (pdf, img, svg, etc)