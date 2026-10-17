# GitHub, Pages e entrega

## Situação atual (17/10/2026)

- **Repositório:** `xsam2025-boop/carga`, criado pelo usuário.
- **Problema:** nas sessões em nuvem, `add_repo` respondeu "vincule sua conta do GitHub", mesmo depois de o usuário conectar pelo celular. Por isso nada foi enviado ao GitHub ainda. O histórico git existe localmente e vai num pacote (`carga.bundle`).
- O workflow `.github/workflows/pages.yml` já está pronto: a cada push na `main`, ele publica a pasta `dist/` no GitHub Pages.

## Próxima tentativa (passo a passo)

1. Pedir ao usuário que conecte o GitHub de preferência **pelo computador**, em claude.ai → Configurações → Conectores / GitHub. Ele precisa autorizar o app do Claude no repositório `carga` (ou em "todos os repositórios").
2. Na sessão, chamar `add_repo` (owner `xsam2025-boop`, repo `carga`, acesso `push`). Não faça checagens antes; se der erro, leia `read_documentation` em `github.access` e repasse ao usuário o motivo exato.
3. Clonar e enviar o conteúdo atual: copiar os arquivos do projeto (ou usar o bundle) para a `main` e fazer o push.
4. No GitHub: Settings → Pages → Source: **GitHub Actions**. O workflow já tenta ativar sozinho (`enablement: true`).
5. O site fica em `https://xsam2025-boop.github.io/carga/`. No celular: abrir no Chrome, menu ⋮ → **Instalar app** (ou "Adicionar à tela inicial"). No iPhone: Safari → Compartilhar → Adicionar à Tela de Início.

**Plano B sem conector:** o usuário sobe o conteúdo de `carga-site.zip` pela interface web do GitHub (Add file → Upload files), ou usa o GitHub Desktop com `carga-projeto.zip`.

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
