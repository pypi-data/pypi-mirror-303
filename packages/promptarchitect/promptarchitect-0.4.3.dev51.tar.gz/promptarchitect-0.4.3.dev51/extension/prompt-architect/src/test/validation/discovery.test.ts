import * as assert from "assert";
import {
  collectPromptFiles,
  containsPromptFiles,
  DirectoryNode,
} from "../../validation/discovery";

suite("containsPromptFiles", () => {
  test("one level", () => {
    const node: DirectoryNode = {
      id: "level-1",
      path: "level-1",
      type: "directory",
      name: "level-1",
      children: [
        {
          id: "level-1/file1.prompt",
          path: "level1/file1.prompt",
          type: "promptFile",
          name: "file1.prompt",
          children: [],
        },
      ],
    };

    const result = containsPromptFiles(node);

    assert.equal(result, true);
  });

  test("two levels", () => {
    const node: DirectoryNode = {
      id: "level-1",
      path: "level-1",
      type: "directory",
      name: "level-1",
      children: [
        {
          id: "level-1/level-2",
          path: "level-1/level-2",
          type: "directory",
          name: "level-2",
          children: [
            {
              id: "level-1/level-2/file1.prompt",
              type: "promptFile",
              path: "level-1/level-2/file1.prompt",
              name: "file1.prompt",
              children: [],
            },
          ],
        },
      ],
    };

    const result = containsPromptFiles(node);

    assert.equal(result, true);
  });

  test("two levels with empty dir", () => {
    const node: DirectoryNode = {
      id: "level-1",
      path: "level-1",
      type: "directory",
      name: "level-1",
      children: [
        {
          id: "level-1/level-2",
          path: "level-1/level-2",
          type: "directory",
          name: "level-2",
          children: [],
        },
        {
          id: "level-1/level-2/file1.prompt",
          type: "promptFile",
          path: "level-1/level-2/file1.prompt",
          name: "file1.prompt",
          children: [],
        },
      ],
    };

    const result = containsPromptFiles(node);

    assert.equal(result, true);
  });

  test("no prompt files", () => {
    const node: DirectoryNode = {
      id: "level-1",
      path: "level-1",
      type: "directory",
      name: "level-1",
      children: [],
    };

    const result = containsPromptFiles(node);

    assert.equal(result, false);
  });
});

suite("collectPromptFiles", () => {
  test("should return an empty array for an empty directory", async () => {
    const result = await collectPromptFiles("empty-dir");
    assert.deepStrictEqual(result, []);
  });

  test("should return prompt files for a directory with prompt files only", async () => {
    const result = await collectPromptFiles("multiple-files-dir");

    assert.deepStrictEqual(result, [
      {
        id: "multiple-files-dir/file1.prompt",
        type: "promptFile",
        name: "file1.prompt",
        path: "multiple-files-dir/file1.prompt",
        children: [
          {
            id: "multiple-files-dir/file1.prompt/test01",
            type: "testSpecification",
            name: "test01",
            promptFile: "multiple-files-dir/file1.prompt",
            children: [],
          },
        ],
      },
      {
        id: "multiple-files-dir/file2.prompt",
        type: "promptFile",
        name: "file2.prompt",
        path: "multiple-files-dir/file2.prompt",
        children: [
          {
            id: "multiple-files-dir/file2.prompt/test01",
            type: "testSpecification",
            name: "test01",
            promptFile: "multiple-files-dir/file2.prompt",
            children: [],
          },
        ],
      },
    ]);
  });

  test("should return nested prompt files for a directory with nested directories", async () => {
    const result = await collectPromptFiles("nested-dir");

    assert.deepStrictEqual(result, [
      {
        id: "nested-dir/file1.prompt",
        type: "promptFile",
        name: "file1.prompt",
        path: "nested-dir/file1.prompt",
        children: [
          {
            id: "nested-dir/file1.prompt/test01",
            type: "testSpecification",
            name: "test01",
            promptFile: "nested-dir/file1.prompt",
            children: [],
          },
        ],
      },
      {
        id: "nested-dir/subdir",
        type: "directory",
        name: "subdir",
        children: [
          {
            id: "nested-dir/subdir/file2.prompt",
            type: "promptFile",
            name: "file2.prompt",
            path: "nested-dir/subdir/file2.prompt",
            children: [
              {
                id: "nested-dir/subdir/file2.prompt/test01",
                type: "testSpecification",
                name: "test01",
                promptFile: "nested-dir/subdir/file2.prompt",
                children: [],
              },
            ],
          },
        ],
      },
    ]);
  });

  test("should ignore non-prompt files", async () => {
    const result = await collectPromptFiles("mixed-files-dir");

    assert.deepStrictEqual(result, [
      {
        id: "mixed-files-dir/file1.prompt",
        type: "promptFile",
        name: "file1.prompt",
        path: "mixed-files-dir/file1.prompt",
        children: [
          {
            id: "mixed-files-dir/file1.prompt/test01",
            type: "testSpecification",
            name: "test01",
            promptFile: "mixed-files-dir/file1.prompt",
            children: [],
          },
        ],
      },
    ]);
  });
});
