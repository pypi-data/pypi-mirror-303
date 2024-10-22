// @ts-check

import eslint from "@eslint/js";
import typescriptEslint from "typescript-eslint";

export default typescriptEslint.config(
    eslint.configs.recommended,
    ...typescriptEslint.configs.recommended,
)

// export default [{
//     ignores: ["**/out", "**/dist", "**/*.d.ts"],
// }, {
//     plugins: {
//         "typescript-eslint": typescriptEslint,
//     },

//     languageOptions: {
//         parser: tsParser,
//         ecmaVersion: 6,
//         sourceType: "module",
//     },

//     rules: {
//         "typescript-eslint/naming-convention": ["warn", {
//             selector: "import",
//             format: ["camelCase", "PascalCase"],
//         }],

//         "typescript-eslint/semi": "warn",
//         curly: "warn",
//         eqeqeq: "warn",
//         "no-throw-literal": "warn",
//         semi: "off",
//     },
// }];