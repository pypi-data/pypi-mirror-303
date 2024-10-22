import * as assert from "assert";
import * as vscode from "vscode";
import { TestProfile } from "../../shared/specification";
import { collectPromptFiles, RunnableNode } from "../../validation/discovery";
import { generateTestProfile, mergeNodeTree } from "../../validation/session";
import { getTestData } from "./testData";

suite("session suite", () => {
  test("merge node tree", async () => {
    const controller = vscode.tests.createTestController(
      "promptarchitect.testController",
      "Test Controller"
    );
    const nodeTree = await collectPromptFiles();

    mergeNodeTree(controller, nodeTree);

    // We're not testing all the nodes, but these ones should be present.

    assert.notEqual(
      controller.items.get("mixed-files-dir"),
      undefined,
      "directory not found"
    );
    assert.notEqual(
      controller.items
        .get("mixed-files-dir")
        ?.children.get("mixed-files-dir/file1.prompt"),
      undefined,
      "prompt file not found"
    );
  });
});

suite("generateTestProfile", () => {
  test("should generate a test profile from a selected prompt file", () => {
    const { selectedPromptFile, availableItems } = getTestData();

    const selectedItems: RunnableNode[] = [selectedPromptFile];

    const expectedProfile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.prompt",
          tests: [
            {
              id: "test-prompt.prompt/test1",
              samples: ["sample1.txt", "sample2.txt"],
            },
            {
              id: "test-prompt.prompt/test2",
              samples: ["sample1.txt", "sample2.txt"],
            },
          ],
        },
      ],
    };

    const result: TestProfile = generateTestProfile(
      selectedItems,
      availableItems
    );

    assert.deepStrictEqual(result, expectedProfile);
  });

  test("should generate a test profile from a selected test specification", () => {
    const { testSpecification, availableItems } = getTestData();

    const selectedItems: RunnableNode[] = [testSpecification];

    const expectedProfile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.prompt",
          tests: [
            {
              id: "test-prompt.prompt/test1",
              samples: ["sample1.txt", "sample2.txt"],
            },
          ],
        },
      ],
    };

    const result: TestProfile = generateTestProfile(
      selectedItems,
      availableItems
    );

    assert.deepStrictEqual(result, expectedProfile);
  });

  test("should generate a test profile from a selected test sample", () => {
    const { firstTestSample, availableItems } = getTestData();

    const selectedItems: RunnableNode[] = [firstTestSample];

    const expectedProfile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.prompt",
          tests: [
            { id: "test-prompt.prompt/test1", samples: ["sample1.txt"] },
            { id: "test-prompt.prompt/test2", samples: ["sample1.txt"] },
          ],
        },
      ],
    };

    const result: TestProfile = generateTestProfile(
      selectedItems,
      availableItems
    );

    assert.deepStrictEqual(result, expectedProfile);
  });

  test("should generate a test profile from a selected test sample and prompt file", () => {
    const { firstTestSample, selectedPromptFile, availableItems } =
      getTestData();

    const selectedItems: RunnableNode[] = [selectedPromptFile, firstTestSample];

    const expectedProfile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.prompt",
          tests: [
            {
              id: "test-prompt.prompt/test1",
              samples: ["sample1.txt", "sample2.txt"],
            },
            {
              id: "test-prompt.prompt/test2",
              samples: ["sample1.txt", "sample2.txt"],
            },
          ],
        },
      ],
    };

    const result: TestProfile = generateTestProfile(
      selectedItems,
      availableItems
    );

    assert.deepStrictEqual(result, expectedProfile);
  });
});
