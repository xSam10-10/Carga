# GitHub, Pages e entrega

## Situação atual (17/10/2026)

- **Repositório:** https://github.com/xSam10-10/Carga (conta do usuário: **xSam10-10**; o `xsam2025-boop` era um nome antigo errado). Público, branch `main`, com o histórico completo do projeto enviado.
- **Conectar numa sessão:** `add_repo` com owner `xSam10-10`, repo `Carga`, acesso `push`. Se falhar, use `list_repos` para ver o nome exato que a conexão enxerga.
- **Pages:** o workflow `.github/workflows/pages.yml` publica `dist/` a cada push na `main`. Na primeira vez, a ação `configure-pages` falha com "Resource not accessible by integration", porque o token do workflow não pode **criar** o site do Pages. O dono precisa ativar uma única vez: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Depois disso, rode o workflow de novo (Actions → "Publicar no GitHub Pages" → Re-run, ou faça um push).
- **Endereço do site:** https://xsam10-10.github.io/Carga/

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
