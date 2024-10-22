import * as fs from "fs";
import * as path from "path";
import * as vscode from "vscode";

import { parsePromptFile } from "../shared/specification";

/**
 * Defines the structure for a directory node for test discovery.
 */
export interface DirectoryNode {
  id: string;
  path: string;
  type: "directory";
  name: string;
  children: (DirectoryNode | PromptFileNode)[];
}

/**
 * Defines the structure for a prompt file node for test discovery.
 */
export interface PromptFileNode {
  id: string;
  path: string;
  type: "promptFile";
  name: string;
  children: TestSpecificationNode[];
}

/**
 * Defines the structure for a test specification node for test discovery.
 */
export interface TestSpecificationNode {
  id: string;
  path: string;
  type: "testSpecification";
  name: string;
  promptFile: string;
  children: PromptInputNode[];
}

export interface PromptInputNode {
  id: string;
  type: "promptInput";
  path: string;
  name: string;
  promptFile: string;
}

export type Node =
  | DirectoryNode
  | PromptFileNode
  | TestSpecificationNode
  | PromptInputNode;

/**
 * Collect all prompt files in the given directory and its child directories.
 * @param dirPath The base path to start collecting prompt files.
 * @returns The list of child nodes for the scanned root directory.
 */
export async function collectPromptFiles(
  dirPath?: string
): Promise<(DirectoryNode | PromptFileNode)[]> {
  const workspaceFolder = vscode.workspace.workspaceFolders![0].uri.fsPath;
  const fullDirPath =
    (dirPath && path.join(workspaceFolder, dirPath)) || workspaceFolder;
  const children: (DirectoryNode | PromptFileNode)[] = [];
  const items = fs.readdirSync(fullDirPath);

  for (const item of items) {
    const itemPath = path.join(fullDirPath, item);
    const stats = fs.statSync(itemPath);

    if (stats.isDirectory()) {
      const childItems = await collectPromptFiles(
        path.relative(workspaceFolder, itemPath)
      );

      const candidate: DirectoryNode = {
        id: path.relative(workspaceFolder, itemPath).replace(/\\/g, "/"),
        path: path.relative(workspaceFolder, itemPath).replace(/\\/g, "/"),
        type: "directory",
        name: item,
        children: childItems,
      };

      if (containsPromptFiles(candidate)) {
        children.push(candidate);
      }
    } else if (stats.isFile() && item.endsWith(".prompt")) {
      const testSpecificationNodes = await collectTestSpecifications(
        path.relative(workspaceFolder, itemPath)
      );

      const promptFile: PromptFileNode = {
        id: path.relative(workspaceFolder, itemPath).replace(/\\/g, "/"),
        path: path.relative(workspaceFolder, itemPath).replace(/\\/g, "/"),
        type: "promptFile",
        name: item,
        children: testSpecificationNodes,
      };

      children.push(promptFile);
    }
  }

  return children;
}

/**
 * Check if the directory node contains prompt files at any level.
 * @param item Directory node to check
 * @returns Returns true if the directory node contains prompt files.
 */
export function containsPromptFiles(item: DirectoryNode): boolean {
  for (const child of item.children) {
    if (child.type === "promptFile") {
      return true;
    } else if (child.type === "directory") {
      const childContainsPromptFiles = containsPromptFiles(
        child as DirectoryNode
      );

      if (childContainsPromptFiles) {
        return true;
      }
    }
  }

  return false;
}

/**
 * Collect test specifications from the given prompt file.
 * @param itemPath Path to the prompt file
 * @returns The list of test specifications in the prompt file.
 */
async function collectTestSpecifications(
  itemPath: string
): Promise<TestSpecificationNode[]> {
  const workspaceFolder = vscode.workspace.workspaceFolders![0].uri.fsPath;
  const fullItemPath = path.join(workspaceFolder, itemPath);

  const specification = await parsePromptFile(fullItemPath);
  const results: TestSpecificationNode[] = [];

  for (const key in specification.metadata.tests) {
    const testSpecificationId = `${itemPath}/${key}`.replace(/\\/g, "/");

    const promptInputs = collectPromptInputs(
      testSpecificationId,
      fullItemPath,
      specification.metadata.test_path
    );

    results.push({
      id: testSpecificationId,
      path: `${itemPath}`.replace(/\\/g, "/"),
      type: "testSpecification",
      name: key,
      promptFile: itemPath,
      children: promptInputs,
    });
  }

  return results;
}

function collectPromptInputs(
  promptFileId: string,
  promptFilePath: string,
  inputFilePath: string | undefined
): PromptInputNode[] {
  if (!inputFilePath) {
    return [];
  }

  const fullPromptInputDirectoryPath = path.join(
    path.dirname(promptFilePath),
    inputFilePath
  );

  if (fs.existsSync(fullPromptInputDirectoryPath) === false) {
    return [];
  }

  const results: PromptInputNode[] = [];
  const workspaceFolderPath = vscode.workspace.workspaceFolders![0].uri.fsPath;
  const promptInputFiles = fs.readdirSync(fullPromptInputDirectoryPath);

  for (const promptInputFile of promptInputFiles) {
    const promptInputPath = path.join(
      fullPromptInputDirectoryPath,
      promptInputFile
    );

    const promptInputNode: PromptInputNode = {
      id: `${promptFileId}/${promptInputFile}`.replace(/\\/g, "/"),
      type: "promptInput",
      path: path.relative(workspaceFolderPath, promptInputPath),
      name: promptInputFile,
      promptFile: path.relative(workspaceFolderPath, promptFilePath),
    };

    results.push(promptInputNode);
  }

  return results;
}

export type RunnableNode =
  | PromptFileNode
  | TestSpecificationNode
  | PromptInputNode;
