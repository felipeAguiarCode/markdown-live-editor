<div align="center">

# Live Notes

**Editor de notas em blocos que cabe num único arquivo HTML.**
Sem build, sem login, sem servidor — tudo salvo no seu navegador.

[![Abrir o app](https://img.shields.io/badge/%E2%96%B6%20ABRIR%20O%20APP-live%20agora-111111?style=for-the-badge&labelColor=22c55e)](https://felipeaguiarcode.github.io/live-notes/)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Zero deps](https://img.shields.io/badge/build-zero%20config-lightgrey?style=flat-square)
![Offline](https://img.shields.io/badge/offline-first-22c55e?style=flat-square)

</div>

---

## Recursos

- **Blocos pelo menu `/`** — título, lista, checklist, citação, destaque, toggle, código, tabela e divisor.
- **Organização** — pastas, busca e blocos que se reordenam arrastando.
- **7 temas** — claro, escuro, Dracula, Catppuccin, Nord, Gruvbox e HTB.
- **Mídia** — imagem, vídeo do YouTube/Vimeo/`.mp4`, tudo redimensionável.
- **Entra e sai fácil** — importa Markdown (arquivo ou pasta) e exporta `.md`, `.html`, PDF ou o projeto inteiro em `.json`.
- **Offline de verdade** — tudo mora no `localStorage`, nada sai da sua máquina.

---

## Rodar local

Duplo clique em `abrir.cmd` (ou `python servidor.py`). Ele sobe um servidor na primeira porta livre a partir da 8123 e abre o navegador. Live Server, `npx serve` ou qualquer outro servidor estático também servem.

Abrir o `index.html` por duplo clique também funciona — só que aí o YouTube recusa o player embutido (origem `null`, erro 153) e o vídeo abre no site. Por `http://localhost` ou pelo Pages, o vídeo toca dentro do app.

---

## Estrutura

```
index.html     o app inteiro — markup, estilo e lógica
servidor.py    servidor estático local, escolhe porta livre e abre o navegador
abrir.cmd      atalho de duplo clique para o servidor
```
