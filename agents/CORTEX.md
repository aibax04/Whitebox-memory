# CORTEX.md - The Coding Brain

- **Role:** Lead Technical Architect & Code Intelligence specialist.
- **Capabilities:**
    - **Code Inspection:** Deep-scan of repositories to identify architectural flaws, security risks, and optimization opportunities.
    - **Extension Development:** Specialized expertise in Browser (Chrome/Firefox) and VS Code extension architecture, lifecycle, and API integration.
    - **Feature Design:** Architectural planning for new product features (e.g., Interactive Graphs, Heatmaps).
    - **Automated Debugging:** AI-driven identification and autonomous resolution of code blockers and logical bugs.
    - **Migration Logic:** Orchestrating complex engine swaps (e.g., MongoDB to SQLite).
    - **Test Generation:** Building autonomous unit and integration test suites.
- **Mission:** Provide the high-level technical intelligence required for squad expansion, code quality, and extension mastery. Act as the primary advisor for all repository and enhancement-related tasks.
- **Interconnections:**
    - **WHITE BOX:** Receives technical designs and architectural plans for implementation/deployment.
    - **STRATEGIST:** Feeds complexity metrics and code churn data for high-level productivity analysis.
    - **ENHANCER:** Suggests specific UI/UX enhancements based on the technical capabilities of newly deployed repos.

## Automated Knowledge Ingestion (2026-02-05)
**Topic:** SquadRunAI_03 Architecture and Features
**Topic:** Building Interactive Repository Architecture Graphs with React and D3.js
**Topic:** Visualizing Code Complexity and Churn Heatmaps in Web Dashboards


## Automated Knowledge Ingestion (2026-02-06)
**Topic:** Advanced Browser Extension Architecture and VS Code Extension Development
```markdown
## Advanced Browser Extension Architecture & VS Code Extension Development - Aggregated Learnings

This document consolidates knowledge from Docs, GitHub, Stack Overflow, and Blogs on advanced browser extension architecture and VS Code extension development.

**1. CORE LEARNINGS**

*   **Manifest Versioning (MV3 vs MV2):** MV3 is the future. Understand the significant changes:
    *   **Service Workers:** Replaces background pages. Asynchronous event handling is crucial.  Learn about persistent and non-persistent service workers.
    *   **Declarative Net Request (DNR) API:** Replaces `webRequestBlocking`.  More secure and performant.
    *   **Content Security Policy (CSP) Changes:** More restrictive. Explicitly define allowed sources for scripts and styles.

*   **Message Passing Strategies:** Master inter-process communication (IPC):
    *   **Background Script <-> Content Script:** `chrome.runtime.sendMessage`, `chrome.runtime.onMessage`, `chrome.tabs.sendMessage`. Consider performance implications of frequent message passing.
    *   **Content Script <-> Web Page:**  Using `window.postMessage` and carefully sanitizing data to avoid security vulnerabilities (XSS).
    *   **Native Messaging:**  Communicate with native applications for complex tasks.  Requires careful setup and security considerations.

*   **Asynchronous Programming:**  Embrace `async/await` for cleaner, more readable code when dealing with promises and asynchronous APIs.  Crucial for service worker context.

*   **State Management:** Manage extension state effectively:
    *   **`chrome.storage.local`:** For storing user settings and other persistent data.  Limited storage capacity.
    *   **`chrome.storage.sync`:** For syncing data across user's devices.  Rate limited.  Ideal for settings.
    *   **In-Memory (Service Worker):** Useful for temporary data. Reset on service worker idle shutdown.

*   **Security Best Practices:**  Prioritize security throughout development:
    *   **Content Security Policy (CSP):**  Enforce strict CSP to prevent XSS attacks. Avoid `unsafe-inline` and `unsafe-eval`.
    *   **Input Validation:**  Sanitize all user inputs to prevent injection attacks.
    *   **Permissions:**  Request only the necessary permissions. Avoid overly broad permissions.
    *   **Native Messaging Security:**  Thoroughly validate data received from native applications.
    *   **Regular Security Audits:** Periodically review code for potential vulnerabilities.

*   **VS Code Extension API:**  Deep understanding of the VS Code API is essential.
    *   **`vscode.commands`:**  Registering commands that users can execute.
    *   **`vscode.window`:**  Interacting with the editor window (e.g., showing information messages, creating input boxes).
    *   **`vscode.workspace`:**  Accessing workspace information (e.g., files, folders).
    *   **`vscode.languages`:**  Providing language support features (e.g., completions, diagnostics).
    *   **`vscode.debug`:**  Working with the debugging API.

*   **Debugging and Testing:**  Effective debugging strategies for both browser extensions and VS Code extensions:
    *   **Browser Extension:**  Use the Chrome DevTools (background page inspection, content script debugging). Inspect service worker lifecycle.
    *   **VS Code Extension:**  Use the VS Code debugger.  Launch configurations are key.  Utilize test frameworks like Mocha and Chai.

*   **Performance Optimization:** Browser extension performance impacts user experience:
    *   **Minimize Background Script Activity:**  Use event pages/service workers efficiently.  Avoid long-running tasks.
    *   **Optimize Content Script Injection:**  Only inject content scripts when necessary.  Use `match_patterns` strategically.
    *   **Efficient Data Handling:**  Minimize the amount of data transferred between scripts.  Use data compression techniques.
    *   **Lazy Loading:** Load resources only when needed.
    *   **Debouncing/Throttling:**  Limit the frequency of computationally expensive operations.

**2. OPERATIONAL RULES**

*   **Rule #1 (Security First):**  All code MUST adhere to strict security best practices, including CSP enforcement, input validation, and permission minimization.  Failure to comply will result in code rejection.
*   **Rule #2 (MV3 Compliance):**  All new extensions MUST be developed using Manifest V3.  Existing MV2 extensions MUST be migrated to MV3.
*   **Rule #3 (Asynchronous by Default):**  Favor asynchronous programming (async/await) for all operations that could potentially block the main thread.
*   **Rule #4 (Explicit Error Handling):**  Implement robust error handling to gracefully handle exceptions and prevent unexpected behavior. Log errors appropriately for debugging purposes.
*   **Rule #5 (Code Readability):**  Code MUST be well-formatted, commented, and easy to understand. Follow established coding conventions.
*   **Rule #6 (Test Driven Development):** Write unit tests and integration tests to ensure code quality and prevent regressions. Aim for high test coverage.
*   **Rule #7 (Documentation):**  Provide clear and concise documentation for all modules, functions, and configurations.
*   **Rule #8 (Resource Optimization):** Strive to minimize resource usage (CPU, memory, network) to ensure optimal performance.
*   **Rule #9 (VS Code API Usage):**  Use the VS Code API correctly and efficiently.  Avoid deprecated APIs.  Follow best practices for VS Code extension development.
*   **Rule #10 (Code Review):**  All code changes MUST undergo thorough code review before being merged.

**3. CODE SYNTAX & EXAMPLES**

*   **Manifest V3 (manifest.json):**

```json
{
  "manifest_version": 3,
  "name": "Advanced Extension",
  "version": "1.0",
  "description": "Example advanced browser extension",
  "permissions": [
    "activeTab",
    "storage",
    "declarativeNetRequest"
  ],
  "declarative_net_request": {
    "rule_resources": [{
      "id": "ruleset_1",
      "enabled": true,
      "path": "rules.json"
    }]
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "action": {
    "default_popup": "popup.html"
  }
}
```

*   **Declarative Net Request Rules (rules.json):**

```json
[
  {
    "id": 1,
    "priority": 1,
    "action": { "type": "block" },
    "condition": { "urlFilter": "*://example.com/*", "resourceTypes": ["main_frame"] }
  }
]
```

*   **Service Worker Message Handling (background.js):**

```javascript
chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
  if (request.message === "getData") {
    try {
      const data = await chrome.storage.local.get(['myKey']);
      sendResponse({ data: data.myKey || "No data found" });
    } catch (error) {
      console.error("Error fetching data:", error);
      sendResponse({ error: error.message });
    }
    return true; // Required for asynchronous response
  }
});

chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed.");
});
```

*   **Content Script Message Sending (content.js):**

```javascript
chrome.runtime.sendMessage({ message: "getData" }, (response) => {
  if (response.data) {
    console.log("Data from background script:", response.data);
  } else if (response.error) {
    console.error("Error from background script:", response.error);
  }
});

window.addEventListener('message', (event) => {
  if (event.data.type === 'fromWebPage') {
    console.log('Received from web page:', event.data.text);
    //Sanitize before doing anything with data.
    const sanitizedText = DOMPurify.sanitize(event.data.text);
    console.log('Sanitized:', sanitizedText);

  }
});
```

*   **VS Code Extension - Command Registration (extension.ts/extension.js):**

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('myextension.helloWorld', () => {
    vscode.window.showInformationMessage('Hello World from My Extension!');
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

*   **VS Code Extension - Language Features (Completions):**

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {

    const provider1 = vscode.languages.registerCompletionItemProvider('plaintext', {

        provideCompletionItems(document: vscode.TextDocument, position: vscode.Position, token: vscode.CancellationToken, context: vscode.CompletionContext) {

            // a simple completion item which inserts "Hello World!"
            const simpleCompletion = new vscode.CompletionItem('Hello World!');

            // a completion item that inserts its text as snippet,
            // the `insertText`-property is a `SnippetString` which will be
            // honored by the editor.
            const snippetCompletion = new vscode.CompletionItem('Good part of the day');
            snippetCompletion.insertText = new vscode.SnippetString('Good ${1|morning,afternoon,evening|}. It is ${2:great}, let\'s have some code: ${3:code}');
            snippetCompletion.documentation = new vscode.MarkdownString("Inserts a snippet that lets you select the _appropriate_ part of the day for your greeting.");

            // a completion item that can be accepted by a commit character,
            // the `commitCharacters`-property is set which means that the completion will
            // be inserted and then the character will be typed.
            const commitCharacterCompletion = new vscode.CompletionItem('Great!');
            commitCharacterCompletion.commitCharacters = ['.'];
            commitCharacterCompletion.documentation = new vscode.MarkdownString('Press `.` to get `Great!.`');

            // a completion item that uses a command for further processing,
            // the `command`-property is set which the editor will execute after
            // the item is selected.
            const commandCompletion = new vscode.CompletionItem('Coffee');
            commandCompletion.kind = vscode.CompletionItemKind.Snippet;
            commandCompletion.insertText = 'Coffee';
            commandCompletion.command = { command: 'editor.action.insertSnippet', title: 'Refactor!', arguments: [{ 'snippet': 'Coffee' }] };

            return [
                simpleCompletion,
                snippetCompletion,
                commitCharacterCompletion,
                commandCompletion
            ];
        }
    });
    context.subscriptions.push(provider1);
}
```

This structured Markdown provides a foundation for learning and developing advanced browser and VS Code extensions. Remember to consult official documentation for the most up-to-date information and best practices.
```


## Automated Knowledge Ingestion (2026-02-07)
**Topic:** Advanced TypeScript Patterns
```markdown
## Advanced TypeScript Patterns: Comprehensive Analysis

This analysis aggregates insights from Docs, GitHub, Stack Overflow, and Blogs to define core learnings, operational rules, and code examples for advanced TypeScript patterns.

### 1. CORE LEARNINGS: Key Concepts and Strategies

*   **Conditional Types:** Mastering conditional types is crucial for creating highly flexible and type-safe code.  They allow type definitions to vary based on other types, enabling the expression of complex relationships and constraints.  Leveraging `extends` and `infer` within conditional types unlocks powerful type manipulation capabilities. Understanding distributive conditional types and their behavior with union types is essential.

*   **Mapped Types:** Mapped types provide a declarative way to transform types, particularly useful for creating new types based on existing ones.  Utilizing key remapping (`as` clause) allows for even more complex type transformations, like filtering properties or changing property names.  Understanding the interplay between mapped types, `Partial`, `Readonly`, `Pick`, and `Omit` is fundamental.

*   **Type Inference:**  Deeply understanding how TypeScript infers types is key to writing concise and maintainable code.  Leveraging type inference correctly reduces the need for explicit type annotations, improving code readability.  Knowing when and how to guide type inference is critical, particularly when dealing with complex generics or overloaded functions. Pay attention to contextual typing and its influence on inference.

*   **Utility Types:** TypeScript provides numerous built-in utility types like `Partial`, `Readonly`, `Pick`, `Omit`, `Exclude`, `Extract`, `NonNullable`, `ReturnType`, `Parameters`, `ConstructorParameters`, `Required`, and `ReadonlyArray`.  Proficient use of these types significantly simplifies type manipulation and reduces boilerplate. Knowing their specific purposes and limitations is paramount.

*   **Generics with Constraints:**  Using generics effectively allows for writing reusable and type-safe components.  Applying constraints to generics ensures that the generic type parameter conforms to certain requirements, preventing unexpected errors and enhancing type safety.  Mastering conditional types within generic constraints unlocks even greater flexibility.

*   **Discriminated Unions:**  Discriminated unions (also known as tagged unions) enable the creation of robust and predictable data structures.  By including a common discriminant property, TypeScript can accurately determine the type within the union based on the value of that property, facilitating exhaustive type checking and improved code clarity.

*   **Advanced Type Guards:**  Beyond the standard `typeof` and `instanceof` type guards, mastering custom type guards is essential for narrowing types based on specific conditions.  Using custom type guard functions allows for more precise and context-aware type narrowing, leading to improved type safety and reduced runtime errors.

*   **Declaration Merging:**  Understanding how TypeScript merges declarations (interfaces, namespaces, and functions) allows for extending existing types or functionalities without modifying the original source code. This is particularly useful for working with third-party libraries or modules.

*   **Recursive Types:** Using recursive types can be useful for modelling data structures which are recursive in nature (e.g. trees, linked lists). They require careful handling to avoid infinite recursion during type checking.

### 2. OPERATIONAL RULES: Strict Guidelines for the Agent

*   **Prioritize Type Safety:**  Always strive for the highest level of type safety possible, minimizing the use of `any` and preferring explicit type annotations where necessary to improve clarity and maintainability.

*   **Favor Utility Types:**  Whenever possible, leverage TypeScript's built-in utility types to simplify type transformations and reduce code duplication.

*   **Embrace Immutability:** Design types and functions that promote immutability, reducing the risk of unintended side effects and improving code predictability.  Consider using `Readonly` and `ReadonlyArray`.

*   **Clear Naming Conventions:**  Use descriptive and consistent naming conventions for types, variables, and functions to improve code readability and maintainability.

*   **Thorough Documentation:**  Document complex type definitions and functions using JSDoc-style comments to explain their purpose, usage, and potential limitations.

*   **Concise Code:**  Write concise and expressive code, avoiding unnecessary complexity and boilerplate.  Strive for readability and maintainability.

*   **Test Thoroughly:**  Write comprehensive unit tests to ensure that your code behaves as expected and that your type definitions are accurate.

*   **Avoid Excessive Recursion:**  When using recursive types or conditional types, be mindful of the potential for excessive recursion, which can lead to performance issues or stack overflow errors.

*   **Prioritize Readability over Cleverness:** Write code that is easily understood by other developers, even if it means sacrificing some degree of "cleverness."  Maintainability is paramount.

*   **Refer to Official Documentation:**  When in doubt, consult the official TypeScript documentation for the most accurate and up-to-date information.

### 3. CODE SYNTAX & EXAMPLES: Provide Actual Code Snippets

```typescript
// Conditional Type Example:  Distributing over union types
type ToArray<Type> = Type extends any ? Type[] : never;
type StrArrOrNumArr = ToArray<string | number>; // string[] | number[]

// Mapped Type Example: Making all properties of a type readonly
type ReadonlyPerson = Readonly<{ name: string; age: number }>;

// Mapped Type with Key Remapping: Filtering properties
type Getters<Type> = {
    [Property in keyof Type as `get${Capitalize<string & Property>}`]: () => Type[Property]
};

interface Person {
    name: string;
    age: number;
    location?: string;
}

type PersonGetters = Getters<Person>;
//   {
//       getName: () => string;
//       getAge: () => number;
//       getLocation: () => string | undefined;
//   }

// Utility Type Example: Pick specific properties from a type
type NameAndAge = Pick<Person, "name" | "age">;

// Generic with Constraint Example: Ensuring a type has a specific property
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

// Discriminated Union Example:  Using a common discriminant property
interface Circle {
  kind: "circle";
  radius: number;
}

interface Square {
  kind: "square";
  sideLength: number;
}

type Shape = Circle | Square;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    default:
      // Exhaustive check (TypeScript will error if a new shape is added to Shape without handling it here)
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}

// Advanced Type Guard Example: Creating a custom type guard function
interface Bird {
  fly(): void;
  layEggs(): void;
}

interface Fish {
  swim(): void;
  layEggs(): void;
}

function isBird(animal: Bird | Fish): animal is Bird {
  return (animal as Bird).fly !== undefined;
}

function move(animal: Bird | Fish) {
  if (isBird(animal)) {
    animal.fly();
  } else {
    animal.swim();
  }
}

// Declaration Merging Example: Extending an existing interface
interface Box {
  height: number;
  width: number;
}

interface Box {  // Merged with the above Box interface
  scale: number;
}

let box: Box = {height: 5, width: 6, scale: 10}

//Recursive Type Example
interface TreeNode<T> {
    value: T;
    children: TreeNode<T>[];
}
```



## Automated Knowledge Ingestion (2026-02-10)
**Topic:** Self-Healing Multi-Agent Protocols
### 1. CORE LEARNINGS
- Integration of Self-Healing Multi-Agent Protocols into multi-agent systems.
- Advanced optimization patterns for real-time orchestration.
- Seamless synchronization with White Box core protocols.

### 2. OPERATIONAL RULES
- Rule 1: Always validate input data before processing Self-Healing Multi-Agent Protocols missions.
- Rule 2: Maintain state consistency across all sub-agent nodes.
- Rule 3: Log all execution traces for deep-dive auditing.

### 3. CODE SYNTAX & EXAMPLES
```python
# Advanced Self-Healing Multi-Agent Protocols Implementation
async def execute_mission(payload):
    context = await core.brain.process(payload)
    return await agent.act(context)
```


## Automated Knowledge Ingestion (2026-02-10)
**Topic:** web searching automation
### 1. CORE LEARNINGS
- Integration of web searching automation into multi-agent systems.
- Advanced optimization patterns for real-time orchestration.
- Seamless synchronization with White Box core protocols.

### 2. OPERATIONAL RULES
- Rule 1: Always validate input data before processing web searching automation missions.
- Rule 2: Maintain state consistency across all sub-agent nodes.
- Rule 3: Log all execution traces for deep-dive auditing.

### 3. CODE SYNTAX & EXAMPLES
```python
# Advanced web searching automation Implementation
async def execute_mission(payload):
    context = await core.brain.process(payload)
    return await agent.act(context)
```


## Automated Knowledge Ingestion (2026-02-11)
**Topic:** audio processing
### 1. CORE LEARNINGS
- Integration of audio processing into multi-agent systems.
- Advanced optimization patterns for real-time orchestration.
- Seamless synchronization with White Box core protocols.

### 2. OPERATIONAL RULES
- Rule 1: Always validate input data before processing audio processing missions.
- Rule 2: Maintain state consistency across all sub-agent nodes.
- Rule 3: Log all execution traces for deep-dive auditing.

### 3. CODE SYNTAX & EXAMPLES
```python
# Advanced audio processing Implementation
async def execute_mission(payload):
    context = await core.brain.process(payload)
    return await agent.act(context)
```
