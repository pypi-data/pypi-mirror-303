import * as path from "path";
import * as vscode from "vscode";
import {
  TestProfile,
  TestProfileInclude,
  TestSpecificationInclude,
} from "../shared/specification";
import {
  Node,
  PromptFileNode,
  PromptInputNode,
  RunnableNode,
  TestSpecificationNode,
} from "./discovery";

export function mergeNodeTree(
  controller: vscode.TestController,
  nodes: Node[]
) {
  const workspacePath = vscode.workspace.workspaceFolders![0].uri.fsPath;

  function mergeNodes(parent: vscode.TestItem, node: Node) {
    if (node.type === "promptInput") {
      return;
    }

    for (const childItem of node.children) {
      let childTestItem = parent.children.get(childItem.name);

      if (!childTestItem) {
        childTestItem = controller.createTestItem(
          childItem.id,
          childItem.name,
          vscode.Uri.file(path.join(workspacePath, childItem.path))
        );

        parent.children.add(childTestItem);
      }

      parent.children.forEach((child) => {
        if (!node.children.some((n) => n.id === child.id)) {
          parent.children.delete(child.id);
        }
      });

      mergeNodes(childTestItem, childItem);
    }
  }

  for (const node of nodes) {
    let testItem = controller.items.get(node.path);

    if (!testItem) {
      testItem = controller.createTestItem(
        node.id,
        node.name,
        vscode.Uri.file(path.join(workspacePath, node.path))
      );

      controller.items.add(testItem);
    }

    mergeNodes(testItem, node);

    controller.items.forEach((child) => {
      if (!nodes.some((n) => n.id === child.id)) {
        testItem.children.delete(child.id);
      }
    });
  }
}

/**
 * Generate a test profile from selected items.
 * @param selectedItems The selected items to generate the test profile from
 * @returns The generated test profile
 */
export function generateTestProfile(
  selectedItems: RunnableNode[],
  availableItems: Map<string, RunnableNode>
): TestProfile {
  const include: TestProfileInclude[] = [];

  // This iterates over the selected items. This list can contain prompt files, test specifications, and prompt inputs.
  // The goal is to generate a test profile that includes all of the selected items.
  selectedItems.forEach((item) => {
    // First, we process prompt files, if they aren't included yet, we include them in the test.
    // When you select a prompt file, we should include all tests, and all samples for the prompt file.
    if (
      item.type === "promptFile" &&
      !promptFileIncludedInProfile(include, item.path)
    ) {
      const testIncludes: TestSpecificationInclude[] = item.children.map(
        (test) => ({
          id: test.id,
          samples: test.children.map((c) => c.path),
        })
      );

      include.push({ filename: item.path, tests: testIncludes });
    }

    // Next we look at test specifications. If a test specification is selected, we should include it in the test profile.
    // We should include the samples associated with the test specification.
    if (
      item.type === "testSpecification" &&
      !testSpecificationIncludedInProfile(include, item)
    ) {
      if (!promptFileIncludedInProfile(include, item.promptFile)) {
        include.push({
          filename: item.promptFile,
          tests: [
            {
              id: item.id,
              samples: item.children.map((c) => c.path),
            },
          ],
        });
      } else {
        // When the prompt file is already included, we need to find the prompt file and add the test to it.
        // Again, we need to include all the samples in the test profile for the test specification.

        const promptFile = include.find((i) => i.filename === item.promptFile)!;
        promptFile.tests!.push({
          id: item.id,
          samples: item.children.map((c) => c.path),
        });
      }
    }

    // Finally, we look at samples. If a sample is selected, we should include it in the test profile.
    // This time, when we don't have a prompt file for this item yet, we should include the profile
    // but only include the selected sample and test.
    if (
      item.type === "promptInput" &&
      !promptInputIncludedInProfile(include, item)
    ) {
      if (!promptFileIncludedInProfile(include, item.promptFile)) {
        const promptFile = availableItems.get(
          item.promptFile
        )! as PromptFileNode;

        const testIncludes: TestSpecificationInclude[] =
          promptFile.children.map((test) => ({
            id: test.id,
            samples: [item.path],
          }));

        include.push({
          filename: item.promptFile,
          tests: testIncludes,
        });
      } else {
        // When we do have a prompt file but not a test specification we need to add the
        // sample to the test specification. This should only include the sample we selected.

        const testSpecification = availableItems.get(
          item.id
        ) as TestSpecificationNode;

        if (!testSpecificationIncludedInProfile(include, testSpecification)) {
          const promptFile = include.find(
            (i) => i.filename === item.promptFile
          )!;

          promptFile.tests!.push({
            id: item.id,
            samples: [item.path],
          });
        } else {
          // When we have a test specification but not the sample, we need to add the sample to the test specification.

          const promptFile = include.find(
            (i) => i.filename === item.promptFile
          )!;

          const testSpecification = promptFile.tests!.find(
            (t) => t.id === item.id
          )!;

          testSpecification.samples.push(item.path);
        }
      }
    }
  });

  return {
    version: "0.0.1",
    include,
  };
}

function promptFileIncludedInProfile(
  include: TestProfileInclude[],
  promptFilePath: string
): boolean {
  return include.some((i) => i.filename === promptFilePath);
}

function testSpecificationIncludedInProfile(
  include: TestProfileInclude[],
  item: TestSpecificationNode
): boolean {
  return include.some(
    (i) =>
      i.filename == item.promptFile && i.tests?.some((t) => t.id === item.id)
  );
}

function promptInputIncludedInProfile(
  include: TestProfileInclude[],
  item: PromptInputNode
) {
  return include.some(
    (i) =>
      i.filename === i.filename &&
      i.tests?.some((t) => t.samples?.some((s) => s === item.path))
  );
}
