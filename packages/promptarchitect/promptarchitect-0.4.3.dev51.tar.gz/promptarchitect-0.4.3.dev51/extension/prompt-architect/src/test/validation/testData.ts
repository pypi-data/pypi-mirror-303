import { RunnableNode } from "../../validation/discovery";

export function getTestData() {
  const firstTestSample: RunnableNode = {
    id: "test-prompt.prompt/test1/sample1.txt",
    type: "promptInput",
    path: "sample1.txt",
    name: "sample1.txt",
    promptFile: "test-prompt.prompt",
  };

  const secondTestSample: RunnableNode = {
    id: "test-prompt.prompt/test1/sample2.txt",
    type: "promptInput",
    path: "sample2.txt",
    name: "sample2.txt",
    promptFile: "test-prompt.prompt",
  };

  const testSpecification: RunnableNode = {
    id: "test-prompt.prompt/test1",
    type: "testSpecification",
    path: "test-prompt.prompt",
    name: "test1",
    promptFile: "test-prompt.prompt",
    children: [firstTestSample, secondTestSample],
  };

  const extraTestSpecification: RunnableNode = {
    id: "test-prompt.prompt/test2",
    type: "testSpecification",
    path: "test-prompt.prompt",
    name: "test2",
    promptFile: "test-prompt.prompt",
    children: [firstTestSample, secondTestSample],
  };

  const selectedPromptFile: RunnableNode = {
    id: "test-prompt.prompt",
    type: "promptFile",
    path: "test-prompt.prompt",
    name: "test-prompt.prompt",
    children: [testSpecification, extraTestSpecification],
  };

  const availableItems = new Map<string, RunnableNode>();
  availableItems.set(firstTestSample.id, firstTestSample);
  availableItems.set(secondTestSample.id, secondTestSample);
  availableItems.set(testSpecification.id, testSpecification);
  availableItems.set(selectedPromptFile.id, selectedPromptFile);

  return {
    firstTestSample,
    secondTestSample,
    testSpecification,
    selectedPromptFile,
    availableItems,
  };
}
