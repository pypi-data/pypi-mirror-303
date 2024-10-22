import * as fs from "fs";
import * as path from "path";
import * as vscode from "vscode";
import { saveTestProfile } from "./shared/specification";
import { collectPromptFiles, Node, RunnableNode } from "./validation/discovery";
import { generateTestProfile, mergeNodeTree } from "./validation/session";

let discoveredTests = new Map<string, RunnableNode>();

export function activate(context: vscode.ExtensionContext) {
  const testController = vscode.tests.createTestController(
    "promptarchitect.testController",
    "Prompt Architect"
  );

  testController.createRunProfile(
    "Run tests",
    vscode.TestRunProfileKind.Run,
    async (request) => {
      let nodes: RunnableNode[];

      if (request.include) {
        nodes = request.include.map((node) => {
          if (!discoveredTests.has(node.id)) {
            throw new Error(`Node ${node.id} not found in discovered tests`);
          }

          return discoveredTests.get(node.id)!;
        });
      } else {
        nodes = Array.from(discoveredTests.values());
      }

      const workspaceDirectory =
        vscode.workspace.workspaceFolders![0].uri.fsPath;
      const testProfile = generateTestProfile(nodes, discoveredTests);
      await saveTestProfile(testProfile, ".promptarchitect/testprofile.json");

      // Create a directory .promptarchitect/output when it doesn't exist in the workspace folder.
      // This is used to store the generated output of the prompts.
      const outputDirectory = path.join(
        workspaceDirectory,
        ".promptarchitect/output"
      );
      if (!fs.existsSync(outputDirectory)) {
        fs.mkdirSync(outputDirectory);
      }

      // Use the well-known promptarchitect location to store the report JSON file.
      const reportDirectory = path.join(workspaceDirectory, ".promptarchitect");

      // Run promptarchitect with the generated test profile.
      const terminal = vscode.window.createTerminal("PromptArchitect");

      terminal.sendText(
        `promptarchitect test run --prompts ${workspaceDirectory} --output ${outputDirectory} --test-profile .promptarchitect/testprofile.json --report-path ${reportDirectory} --report-format json`
      );

      terminal.show();
    }
  );

  testController.refreshHandler = async () => {
    const nodeTree = await collectPromptFiles();
    mergeNodeTree(testController, nodeTree);
    cacheDiscoveredTests(nodeTree);
  };

  testController.resolveHandler = async (item) => {
    let nodeTree: Node[];

    if (item) {
      const workspaceFolder = vscode.workspace.workspaceFolders![0].uri.fsPath;
      const relativePath = path.relative(workspaceFolder, item.uri!.fsPath);

      nodeTree = await collectPromptFiles(relativePath);
    } else {
      nodeTree = await collectPromptFiles();
    }

    mergeNodeTree(testController, nodeTree);
    cacheDiscoveredTests(nodeTree);
  };

  context.subscriptions.push(testController);
}

function cacheDiscoveredTests(nodeTree: Node[], clearCache = true) {
  if (clearCache) {
    discoveredTests = new Map();
  }

  for (const node of nodeTree) {
    if (node.type !== "directory") {
      discoveredTests.set(node.id, node);
    }

    if (node.type !== "promptInput") {
      cacheDiscoveredTests(node.children, false);
    }
  }
}

export function deactivate() {}
