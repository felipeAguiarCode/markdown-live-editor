# Criar a skill `store-assets`

Crie uma skill reutilizável para preparar a mídia de divulgação de um projeto a partir dos assets existentes e do app em execução. Use o `SKILL.md` abaixo como entrada da skill e copie a seção **Produção e verificação** para `references/production.md`. O caso do markdown-live-editor documenta uma execução completa.

## Conteúdo de `store-assets/SKILL.md`

````markdown
---
name: store-assets
description: Prepare materiais de divulgação de um app em .store. Use ao criar ou atualizar ícones, capas, capturas reais e vídeos de demonstração para uma loja ou portfólio.
---

# Assets de loja

1. **Inventarie.** Na raiz do projeto, identifique o nome público, o idioma, a identidade visual, a forma de rodar o app e os materiais que já existem. Procure também ícones embutidos no HTML e referências a arquivos no código, nos manifestos e na documentação. Termine com uma fonte e uma decisão por categoria pedida.
2. **Reaproveite.** Use o material existente quando representa a versão atual do app e atende ao formato do destino. Copie arquivos que o app ou outro consumidor usa no caminho original. Ao mover um arquivo, atualize as referências e confira os destinos.
3. **Produza o que falta.** Para exportar ícones, compor capas, capturar o app ou gravar a demonstração, leia [Produção e verificação](references/production.md). Planeje cenas que mostrem recursos distintos. Use os tamanhos do destino quando informados.
4. **Entregue.** Organize os arquivos finais nas cinco categorias abaixo. Confirme que cada categoria pedida tem material utilizável. Liste a estrutura, as fontes reaproveitadas, os arquivos gerados e as verificações realizadas. Se uma categoria ficar pendente, indique o motivo concreto.

```text
.store/
  icons/
  squares/
  banners/
  screenshots/
  videos/
```

Use nomes de arquivo consistentes, com o nome do app nas peças de divulgação. Guarde rascunhos, scripts temporários, gravação bruta e folhas de contato fora de `.store`. A entrega termina com os arquivos validados no projeto. Sincronização de portfólio, commit e publicação seguem o escopo pedido.
````

## Produção e verificação

### 1. Ícones

1. Localize o símbolo oficial no favicon, manifesto, pacote de marca ou código do app. Se for um SVG embutido, leia o `href` do `link[rel="icon"]` e use a imagem do próprio app como fonte. Preserve o desenho e a margem ótica de origem. Quando faltar um ícone oficial, desenhe uma marca simples que represente a função do app e teste a silhueta no menor tamanho.
2. Rasterize o vetor diretamente em cada dimensão. No navegador, use uma página vazia, a imagem ocupando todo o quadro, `deviceScaleFactor: 1` e captura PNG com `omitBackground: true` quando a fonte tiver transparência. Confirme que a imagem carregou antes de capturar. Se a fonte for raster, use a maior versão oficial e preserve a proporção.
3. Exporte os tamanhos pedidos pelo destino. Na ausência de uma lista, gere `icon-16.png`, `icon-32.png`, `icon-48.png`, `icon-64.png`, `icon-96.png`, `icon-128.png`, `icon-180.png`, `icon-192.png`, `icon-256.png`, `icon-512.png` e `icon-1024.png`. Confira se cada PNG é quadrado, se os cantos têm a transparência esperada e se a marca continua legível em 16 e 32 px.

### 2. Capturas reais

1. Abra o app no caminho de execução que o projeto oferece. Use um contexto de navegador isolado, com dados fictícios coerentes com o idioma e o propósito do produto. Carregue os dados antes da inicialização quando houver uma fixture ou um formato de importação utilizável. Exercite os recursos pela interface.
2. Escolha de quatro a seis cenas. Use uma cena geral para explicar a navegação e distribua as outras entre operações que se distinguem visualmente. Inclua celular quando o app oferecer um layout móvel. Anote a intenção de cada captura e escolha nomes como `01-organizacao.png` e `02-modelos-de-projeto.png`.
3. Espere pela tela esperada, pelas fontes e pelo fim de transições que alterem o layout. Use a largura e a altura do destino. Em automação com Playwright, capture com `animations: "disabled"` e `caret: "hide"` para imagens estáticas. Revise o resultado em tamanho de galeria e no tamanho integral. Confira texto legível, menus dentro do quadro, seleção visível e ausência de dados pessoais.

### 3. Capas

1. Use como fontes o ícone oficial, uma captura real e a paleta do projeto. Faça a composição depois de aprovar as capturas. Dê espaço ao nome público, preserve a proporção da interface e use texto de apoio apenas se ele explicar o que o app faz.
2. Na capa quadrada de referência, use uma tela de **1080 × 1080 px**. Ponha marca, nome e uma frase curta na parte superior e enquadre a captura na metade inferior. No banner de **1920 × 640 px**, distribua marca e texto de um lado e a captura do outro. Ajuste a composição à proporção exigida pelo destino.
3. Para montar a arte com Pillow, crie o fundo com a paleta do app, recorte a margem transparente do ícone apenas na composição e redimensione a captura com LANCZOS. Use uma máscara arredondada e uma borda discreta para enquadrar a interface. Inspecione as duas peças em miniatura e confirme os tamanhos dos PNGs.

### 4. Vídeo de demonstração

1. Monte um roteiro com uma tela inicial reconhecível e interações que tenham resultado visível. Reserve tempo para ler menus e observar mudanças. Use legendas curtas no idioma do projeto quando forem úteis. Mantenha legendas e ponteiro temporários na gravação.
2. Grave o app funcionando em um quadro de **1280 × 720** ou **1920 × 1080**. Com Playwright, use `recordVideo` com o mesmo tamanho do viewport em um contexto dedicado. Reproduza as interações com cliques e digitação. Encerre o contexto antes de guardar a gravação bruta. Inspecione a abertura e retire apenas a espera de carregamento que aparecer no vídeo.
3. Exporte para MP4 com H.264 em `.store/videos/`. Este comando prepara uma prévia sem áudio a 30 fps a partir da gravação bruta. Ajuste o nome de saída ao projeto.

```sh
ffmpeg -i preview.webm -map 0:v:0 -an -vf "fps=30,format=yuv420p" \
  -c:v libx264 -preset fast -crf 17 -movflags +faststart \
  .store/videos/app-demonstracao.mp4
```

4. Confira a duração, a resolução e o codec com `ffprobe`. Decodifique o vídeo inteiro e reproduza a abertura e um trecho perto do fim no navegador. Se o servidor local não oferecer busca por intervalo, abra o MP4 como uma URL de Blob para checar o avanço no arquivo completo.

```sh
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,avg_frame_rate:format=duration \
  -of json .store/videos/app-demonstracao.mp4
ffmpeg -v error -xerror -err_detect explode \
  -i .store/videos/app-demonstracao.mp4 -f null -
```

### 5. Conferência final

Abra cada PNG e compare as dimensões ao destino. Confira a quantidade de arquivos, as cinco subpastas diretas e os nomes finais. Valide a integridade das imagens. Com Pillow, faça `verify()` logo após abrir o arquivo e reabra para carregar pixels ou inspecionar o canal alfa. Revise as capturas juntas para detectar cenas repetidas e confira as referências a arquivos que foram movidos.

## Caso real do markdown-live-editor

1. Exporte o [favicon SVG embutido em `index.html`](index.html) em 11 tamanhos. O desenho combina um bloco de notas com uma janela de navegador.
2. Abra a nota fictícia **Projeto Aurora** em um contexto isolado. Capture organização, modelos de projeto, menu do editor, tabela editável, escrita imersiva e editor móvel. As cenas desktop usam 1440 × 900 px. A captura móvel usa viewport de 390 × 844 com densidade 2, resultando em 780 × 1688 px. [Capturas de referência](.store/screenshots/)
3. Monte a capa quadrada com a captura de organização e o banner com a captura de escrita imersiva. Use um fundo derivado da paleta escura, o ícone no topo ou à esquerda e a imagem real do editor com borda arredondada. [Capa quadrada](.store/squares/markdown-live-editor-capa-quadrada.png) · [Banner](.store/banners/markdown-live-editor-banner.png)
4. Grave a navegação por pastas e modelos, a transformação de blocos, a edição de tabela, a troca de tema e o modo imersivo com papel pautado. Confira a reprodução da prévia em 720p e 30 fps. [Demonstração](.store/videos/markdown-live-editor-demonstracao.mp4)

## Validar a skill criada

Valide o frontmatter e os links do pacote. Rode a skill em um checkout isolado com um favicon já referenciado pelo app e sem material de divulgação. A execução deve preservar o favicon, entregar as cinco categorias e permitir inspecionar todos os resultados. Rode novamente com as saídas já presentes para verificar o reaproveitamento e a ausência de duplicatas.

## Referências de escrita

Use a descrição para disparar a skill nos pedidos certos. Deixe o fluxo comum no arquivo principal e a produção por tipo de peça na referência acessada sob demanda. Formule os passos com verbos de ação e critérios que possam ser conferidos. [Writing for Agents, de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) · [Skill Mechanics](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)
