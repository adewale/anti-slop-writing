// Tool-free, resource-free subscription call. No AgentSession or repo discovery.
// Usage: node subscription_model.mjs /path/to/pi-coding-agent/dist/index.js
// One JSON request on stdin; one JSON response on stdout. Never emit credentials.
import { pathToFileURL } from "node:url";

export async function readRequest(input = process.stdin) {
  // Python's subprocess pipe may be nonblocking. readFileSync(0) can fail with
  // EAGAIN on a package-sized prompt before any provider request is made.
  let text = "";
  input.setEncoding("utf8");
  for await (const chunk of input) text += chunk;
  return JSON.parse(text);
}

async function main() {
  const request = await readRequest();
  const { ModelRuntime } = await import(pathToFileURL(process.argv[2]).href);
  const runtime = await ModelRuntime.create();
  if (!runtime.isUsingSubscription("openai")) {
    throw new Error("OpenAI subscription authentication is required; API billing is not authorized");
  }
  const model = runtime.getModel("openai", request.model);
  if (!model) throw new Error(`Unknown model: ${request.model}`);
  const result = await runtime.completeSimple(
    model,
    {
      systemPrompt: "You are a helpful assistant.",
      messages: [{ role: "user", content: request.prompt, timestamp: Date.now() }],
      tools: [],
    },
    {
      reasoning: request.effort,
      maxTokens: 10000,
      signal: AbortSignal.timeout(180000),
    },
  );
  console.log(JSON.stringify({ requestedModel: request.model, tools: [], result }));
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  await main();
}
