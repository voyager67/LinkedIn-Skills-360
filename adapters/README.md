# AI host adapters

The core is provider-neutral: a `SKILL.md` is Markdown instructions plus YAML metadata. Any model that can interpret these instructions can use a skill when the file is in its context. Automatic skill discovery, persistent loading, filesystem access, tools and multi-agent delegation are host-specific capabilities—not guarantees of the skill format.

| Host / model environment | Practical use | Caveat |
|---|---|---|
| Claude / Claude Code | Copy selected skill folders into a supported skills directory, or attach/paste a skill for a single task. | Check current host conventions and directory rules. |
| OpenAI Codex | Add selected folders to a currently supported skills location or include the `SKILL.md` in context. | Verify the installed Codex version's discovery behaviour. |
| ChatGPT | Paste or attach a skill in a conversation, or use a supported project/custom-instruction surface. | Do not assume a public GitHub URL is automatically installed or persistently loaded. |
| Google Gemini | Paste/attach the skill or use a supported instruction surface. | Host features and file handling vary by product and account. |
| Open-weight / local LLMs | Provide the skill as context through the local UI or runtime. | Quality depends on the model, context window, inference parameters and system prompt. |
| Other agent hosts | Adapt the Markdown folder to the host's documented discovery and delegation rules. | Do not alter the skill's safety boundaries to fit a tool integration. |

## Portable single-skill method

1. Open `skills/<skill-name>/SKILL.md`.
2. Paste or attach the complete file in the AI chat.
3. State the task and provide the minimum relevant inputs.
4. Ask the model to follow the workflow and output contract.
5. Review assumptions, facts and actions before using the result.

## Orchestrated method

Provide `agents/orchestrator.md` plus the relevant specialist file and skill. If the host supports delegation, separate work into specialists using the handoff contract. Otherwise, follow the route sequentially in one conversation. Do not claim that separate agents ran when they did not.

See the host-specific notes: [Claude Code](claude-code.md), [Codex](codex.md), [ChatGPT](chatgpt.md), and [Gemini and other hosts](gemini-and-other-hosts.md).
