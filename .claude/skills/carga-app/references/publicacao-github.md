# GitHub, Pages e entrega

## Situação atual (17/10/2026)

- **Repositório:** https://github.com/xSam10-10/Carga (conta do usuário: **xSam10-10**; o `xsam2025-boop` era um nome antigo errado). Público, branch `main`, com o histórico completo do projeto enviado.
- **Conectar numa sessão:** `add_repo` com owner `xSam10-10`, repo `Carga`, acesso `push`. Se falhar, use `list_repos` para ver o nome exato que a conexão enxerga.
- **Pages:** o workflow `.github/workflows/pages.yml` publica `dist/` a cada push na `main`. Na primeira vez, a ação `configure-pages` falha com "Resource not accessible by integration", porque o token do workflow não pode **criar** o site do Pages. O dono precisa ativar uma única vez: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Depois disso, rode o workflow de novo (Actions → "Publicar no GitHub Pages" → Re-run, ou faça um push).
- **Pages ativado** em 17/10/2026; a primeira publicação deu certo. Cada push na `main` atualiza o site sozinho (lembre de aumentar o `CACHE` em `sw.js`).
- **Endereço do site:** https://xsam10-10.github.io/Carga/ (o contêiner da sessão não acessa github.io; confira pelo status do workflow com `gh run list -R xSam10-10/Carga`).

## Se a conexão não aparecer
1. A conta precisa estar vinculada em https://claude.ai/connect-github.
2. O app do Claude precisa estar instalado no repositório: github.com/settings/installations → Claude → Configure → Repository access.
3. As permissões são definidas quando a sessão começa. Se mesmo assim não aparecer, abra uma sessão nova com o repositório selecionado.

**Plano B sem conector:** subir o conteúdo do `carga-projeto.zip` pela interface web do GitHub (Add file → Upload files).

## Pacotes entregues ao usuário a cada versão

| Arquivo | Conteúdo |
|---|---|
| `carga-projeto.zip` | Projeto inteiro, sem `.git` e sem `tools/.cache` |
| `carga-site.zip` | Só o conteúdo de `dist/`; é o site pronto para o Pages |
| `carga.bundle` | Histórico git completo (`git clone carga.bundle carga`) |

## Commits

- Autor: `Samuel Costa <samuel.costa@unilever.com>`.
- Mensagens em português, com título curto e corpo explicando o que mudou para o usuário.
- Siga as linhas de atribuição que a sessão indicar.
- Nunca coloque identificador de modelo em commits ou em arquivos do repositório.

## Atualizações no celular

- Aumente o `CACHE` em `sw.js` a cada entrega; o service worker antigo é trocado na próxima abertura.
- Ícones e nome só mudam no celular depois de **reinstalar** o app (remover e adicionar de novo à tela inicial).

## Atualização automática no celular (v36, 18/10/2026)
- `sw.js` busca os arquivos com `fetch(req,{cache:'no-cache'})` (rede primeiro, sem o cache HTTP de 10 min do Pages; cache só offline).
- O app registra o service worker com `updateViaCache:'none'`, chama `reg.update()` sempre que volta para a tela e a cada 30 min; no `controllerchange` recarrega sozinho (ou avisa, se houver treino em andamento, folha aberta ou formulário).
- A versão aparece no rodapé de Configurações ("Carga v36"): `build.py` troca `__CARGA_V__` pelo `CACHE` do `sw.js`. Para conferir se o celular está atualizado, compare com o `CACHE` atual.
- Versões até a v35 não tinham isso: o app instalado podia ficar parado na memória com a versão antiga até ser fechado de vez.
