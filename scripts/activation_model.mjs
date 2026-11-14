// Controlled live Pi AgentSession: native skill metadata + guarded read tool.
// Host authentication uses the existing SDK subscription store, never artifact copies.
import { readFile, realpath } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { readRequest } from "./subscription_model.mjs";

export async function confinedPath(root, requested) {
  const resolved = await realpath(requested);
  const canonicalRoot = await realpath(root);
  if (resolved !== canonicalRoot && !resolved.startsWith(canonicalRoot + path.sep)) {
    throw new Error("Read outside the isolated skill tree is not permitted");
  }
  return resolved;
}

async function main() {
  const request = await readRequest();
  const sdk = await import(pathToFileURL(process.argv[2]).href);
  const runtime = await sdk.ModelRuntime.create();
  if (!runtime.isUsingSubscription("openai")) {
    throw new Error("OpenAI subscription authentication is required; API billing is not authorized");
  }
  const model = runtime.getModel("openai", request.model);
  if (!model) throw new Error(`Unknown model: ${request.model}`);
  const found = sdk.loadSkillsFromDir({ dir: request.skillRoot, source: "isolated-study" });
  if (found.skills.length !== 1 || found.skills[0].name !== "anti-slop-writing" || found.diagnostics.length) {
    throw new Error("Unexpected skill inventory or diagnostics");
  }
  const extensions = { extensions: [], errors: [], runtime: sdk.createExtensionRuntime() };
  const resourceLoader = {
    getExtensions: () => extensions,
    getSkills: () => found,
    getPrompts: () => ({ prompts: [], diagnostics: [] }),
    getThemes: () => ({ themes: [], diagnostics: [] }),
    getAgentsFiles: () => ({ agentsFiles: [] }),
    getSystemPrompt: () => undefined,
    getSystemPromptSource: () => undefined,
    getAppendSystemPrompt: () => [],
    getAppendSystemPromptSources: () => [],
    extendResources: () => {},
    reload: async () => {},
  };
  const operations = {
    readFile: async (file) => readFile(await confinedPath(request.skillRoot, file)),
    access: async (file) => { await confinedPath(request.skillRoot, file); },
    detectImageMimeType: async () => undefined,
  };
  const readTool = sdk.createReadToolDefinition(request.cwd, { operations });
  const { session } = await sdk.createAgentSession({
    cwd: request.cwd,
    agentDir: request.agentDir,
    modelRuntime: runtime,
    model,
    thinkingLevel: "low",
    resourceLoader,
    tools: [],
    customTools: [readTool],
    sessionManager: sdk.SessionManager.inMemory(request.cwd),
    settingsManager: sdk.SettingsManager.inMemory({
      compaction: { enabled: false }, retry: { enabled: false },
    }),
  });
  try {
    const tools = session.getActiveToolNames();
    if (tools.length !== 1 || tools[0] !== "read") throw new Error("Unexpected active tools");
    console.log(JSON.stringify({ type: "init", client: "pi-sdk", model: request.model,
      cwd: request.cwd, skillRoot: request.skillRoot,
      skills: found.skills.map(({ name, description, filePath }) => ({ name, description, filePath })),
      tools, systemPrompt: session.systemPrompt,
    }));
    let assistantTurns = 0;
    session.subscribe((event) => {
      if (["message_end", "tool_execution_start", "tool_execution_end", "agent_settled"].includes(event.type)) {
        console.log(JSON.stringify(event));
      }
      if (event.type === "message_end" && event.message?.role === "assistant" && ++assistantTurns > 8) {
        void session.abort();
      }
    });
    await session.prompt(request.query);
    const messages = session.messages;
    const assistants = messages.filter((m) => m.role === "assistant");
    if (!assistants.length || assistants.some((m) => m.model !== request.model || m.stopReason === "error")) {
      throw new Error("Incomplete response or unexpected model");
    }
    if (assistants.at(-1).stopReason !== "stop") throw new Error("Incomplete agent run");
    console.log(JSON.stringify({ type: "result", success: true, messages,
      finalText: session.getLastAssistantText(), model: request.model }));
  } finally {
    session.dispose();
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) await main();
