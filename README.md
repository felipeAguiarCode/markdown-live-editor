<div align="center">

# markdown-live-editor

**Editor de notas em blocos que cabe num único arquivo HTML.**
Sem build, sem login, sem servidor — tudo salvo no seu navegador.

[![Abrir markdown-live-editor](https://img.shields.io/badge/%E2%96%B6%20ABRIR%20O%20APP-live%20agora-111111?style=for-the-badge&labelColor=22c55e)](https://felipeaguiarcode.github.io/markdown-live-editor/)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Zero deps](https://img.shields.io/badge/build-zero%20config-lightgrey?style=flat-square)
![Offline](https://img.shields.io/badge/offline-first-22c55e?style=flat-square)

</div>

---

## Recursos

- **Modelos de nota** — o menu **Modelos** reúne prompts como Zero-shot, Few-shot e Many-shot, specs técnicas e uma seção **Fundamentos de projeto** com modelos de contexto do app, stack e bibliotecas, arquitetura, convenções e setup. Cada modelo cria uma nota editável na pasta ativa.
- **Blocos pelo menu `/`** — título, lista, checklist, citação, destaque, toggle, código, tabela e divisor. Selecione vários blocos pelo texto ou pelas alças e arraste uma alça para mover o conjunto.
- **Menu do editor** — clique com o botão direito no bloco ou na seleção para transformar, copiar, recortar, colar texto, duplicar, inserir acima ou abaixo, mover ou excluir. Dentro de uma célula, o clique direito abre as opções da tabela.
- **Tabelas editáveis** — use as alças para inserir, duplicar, mover ou remover linhas e colunas. Os botões nas bordas acrescentam linhas e colunas ao final, e Tab avança para a próxima célula.
- **Organização** — pastas e subpastas, notas fixadas no topo, busca sem acentos e ordenação por edição, criação ou título. Use o menu da nota ou arraste-a para movê-la a outra pasta.
- **Desktop e celular** — no desktop, os painéis começam ocultos. Use **Mostrar painéis** para abrir pastas e notas. No celular, a seta do editor volta à lista.
- **23 temas** — o Escuro usa a paleta do Dracula e é o padrão. O botão ao lado do modo imersivo alterna entre o Claro inspirado no Notion e o último tema escuro com uma transição circular. Em Configurações, a lista inclui DIO e paletas aconchegantes como Baunilha, Pêssego, Cacau e Mirtilo.
- **Papel do editor** — em Configurações, escolha fundo liso, pautado, quadriculado ou pontilhado.
- **Modo imersivo** — o editor ocupa a janela, com ferramentas centralizadas à direita e **Nova nota**, **Modelos** e **Opções da nota** no canto inferior direito. Use **Ctrl+I** para entrar ou sair, ou **Esc** para sair.
- **Mídia** — imagem, vídeo do YouTube/Vimeo/`.mp4`, tudo redimensionável.
- **Opções da nota** — o menu de três pontos reúne exportação em Markdown, HTML ou PDF e a opção **Resetar nota…**, que confirma antes de limpar o conteúdo.
- **Entrada e saída** — a barra lateral importa Markdown (arquivo ou pasta) e permite fazer backup do projeto inteiro em JSON.
- **Exportação de pastas** — clique com o botão direito sobre uma pasta e escolha **Exportar pasta** para baixar um ZIP com as subpastas e todas as notas em Markdown.
- **Uso offline** — notas, modelos e preferências ficam disponíveis localmente. Mídias vinculadas a sites externos dependem de conexão.
- **Sobre** — ao lado das Configurações, abra a apresentação de Felipe Silva Aguiar e os links para LinkedIn, GitHub e Instagram.

---

## Referências dos modelos

As specs do markdown-live-editor adaptam para português estruturas do Spec Coding.

| Modelo | Referência |
| --- | --- |
| Contexto de projeto | [Software Spec Template](https://spec-coding.dev/resources/software-spec-template-google-docs) |
| Spec de funcionalidade | [Feature Spec](https://spec-coding.dev/templates/feature-spec) |
| Spec de API | [API Spec](https://spec-coding.dev/templates/api-spec) |
| Spec de banco de dados | [DB Spec](https://spec-coding.dev/templates/db-spec) |
| Design técnico | [SDD Design Doc](https://spec-coding.dev/templates/sdd-design-doc) |
| Plano de implementação | [SDD Tasks Plan](https://spec-coding.dev/templates/sdd-tasks-plan) |
| Critérios de aceite | [Acceptance Criteria](https://spec-coding.dev/guides/acceptance-criteria-examples) |
| Registro de evidências | [SDD Evidence Log](https://spec-coding.dev/templates/sdd-evidence-log) |
| Revisão de código com IA | [AI Coding Review](https://spec-coding.dev/templates/ai-coding-review) |

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
.store/        ícones, capas, capturas e vídeo de divulgação
```
