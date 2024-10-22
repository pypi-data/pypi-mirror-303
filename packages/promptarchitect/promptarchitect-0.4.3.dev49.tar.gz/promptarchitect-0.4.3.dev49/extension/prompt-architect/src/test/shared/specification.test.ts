import * as assert from "assert";
import * as fs from "fs";
import * as path from "path";
import * as vscode from "vscode";
import {
  EngineeredPromptSpecification,
  parsePromptFile,
  parsePromptFileContent,
  saveTestProfile,
  TestProfile,
} from "../../shared/specification";

suite("parsePromptFileContent", () => {
  test("should parse content with metadata correctly", () => {
    const content = `---
title: Test Title
author: John Doe
date_created: 2023-10-01
description: This is a test description.
---
This is the input content.`;

    const result: EngineeredPromptSpecification =
      parsePromptFileContent(content);

    assert.deepStrictEqual(result.metadata, {
      title: "Test Title",
      author: "John Doe",
      date_created: "2023-10-01",
      description: "This is a test description.",
    });
    assert.strictEqual(result.input, "This is the input content.");
  });

  test("should parse content without metadata correctly", () => {
    const content = `This is the input content without metadata.`;

    const result: EngineeredPromptSpecification =
      parsePromptFileContent(content);

    assert.deepStrictEqual(result.metadata, {});
    assert.strictEqual(
      result.input,
      "This is the input content without metadata."
    );
  });
});

suite("parsePromptFile", () => {
  const workspacePath = vscode.workspace.workspaceFolders![0]!.uri.fsPath;

  const validFilePath = path.join(workspacePath, "test01.prompt");
  const invalidFilePath = path.join(workspacePath, "non-existent-file.prompt");
  test("should parse a valid file correctly", async () => {
    const result: EngineeredPromptSpecification = await parsePromptFile(
      validFilePath
    );

    assert.notEqual(result, undefined);
    assert.notEqual(result, null);
    assert.strictEqual(result.metadata.author, "John Doe");
    assert.strictEqual(result.metadata.date_created, "2023-10-01");
    assert.strictEqual(
      result.metadata.description,
      "This is a test description."
    );
  });

  test("should reject with an error for a non-existent file", async () => {
    await assert.rejects(async () => {
      await parsePromptFile(invalidFilePath);
    });
  });
});

suite("saveTestProfile", () => {
  const validFilePath = path.join(__dirname, "test-profile.json");
  const invalidFilePath = path.join(__dirname, "invalid-dir/test-profile.json");

  test("should save a valid profile correctly", async () => {
    const profile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.md",
          tests: [
            {
              id: "test1",
              samples: ["sample1.txt", "sample2.txt"],
            },
            {
              id: "test2",
              samples: ["sample3.txt"],
            },
          ],
        },
      ],
    };

    await saveTestProfile(profile, validFilePath);

    const savedProfile = JSON.parse(fs.readFileSync(validFilePath, "utf8"));
    assert.deepStrictEqual(savedProfile, profile);
  });

  test("should reject with an error for an invalid file path", async () => {
    const profile: TestProfile = {
      version: "0.0.1",
      include: [
        {
          filename: "test-prompt.md",
          tests: [
            {
              id: "test1",
              samples: ["sample1.txt", "sample2.txt"],
            },
            {
              id: "test2",
              samples: ["sample3.txt"],
            },
          ],
        },
      ],
    };

    await assert.rejects(async () => {
      await saveTestProfile(profile, invalidFilePath);
    });
  });
});
