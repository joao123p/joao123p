### 👋 Olá! Eu sou o João Paulo.
### 🧑‍💻 Estudante De Analise E Desenvolvimento De Sistemas.
### 👉 Apaixonado por tecnologia, e feliz por poder facilitar e mudar a vida das pessoas através da programação.

<div align="">
  <a href="https://github.com/joao123p">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=joao123p&show_icons=true&theme=dracula&include_all_commits=true&count_private=true"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=joao123p&layout=compact&theme=dracula"/>
</div>

### Minhas Redes Sociais 👇
  <div>
  <a href="https://www.linkedin.com/in/jo%C3%A3o-paulo-457342186/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a>
<a href="https://www.instagram.com/jao_prg/" target="_blank"><img src="https://img.icons8.com/fluency/48/000000/instagram-new.png"/></a>
 <a href = "mailto:paulo2954@gmail.com"><img src="https://img.icons8.com/color/48/000000/google-plus--v1.png"/></a>
  </div>

##

### Tecnologias que uso no dia a dia.
<div>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" target="_blank">
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white" target="_blank">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank">
 </div>

---

## 🤖 Agente de I.A. local

Este repositório agora inclui um agente de inteligência artificial simples chamado **Aurora**. Ele usa uma memória curta para manter o contexto da conversa e consegue acionar ferramentas especializadas para responder perguntas sobre tecnologia ou resolver cálculos matemáticos básicos.

### ✨ Funcionalidades
- Memória curta das últimas mensagens trocadas.
- Ferramenta de consulta a uma base de conhecimento local com temas relacionados a I.A. e tecnologia.
- Ferramenta de cálculo matemático seguro, ideal para contas rápidas.
- Interface de linha de comando interativa ou modo demonstração automático.

### ▶️ Como executar
1. Certifique-se de ter o Python 3.10 ou superior instalado.
2. No terminal, execute o modo demonstração:
   ```bash
   python -m ia_agent.main --demo
   ```
3. Para conversar interativamente, execute sem a flag `--demo`:
   ```bash
   python -m ia_agent.main
   ```
   Para encerrar, digite `sair`.

### 🧱 Estrutura de pastas relevante
```
ia_agent/
├── __init__.py
├── agent.py        # Orquestra o fluxo do agente
├── data/
│   └── knowledge_base.json  # Base de conhecimento local
├── main.py         # Interface de linha de comando
├── memory.py       # Armazena o histórico curto da conversa
└── tools.py        # Implementação das ferramentas disponíveis
```

Sinta-se à vontade para expandir a base de conhecimento adicionando novos tópicos ao arquivo JSON ou criar novas ferramentas especializadas seguindo o protocolo definido em `tools.py`.
