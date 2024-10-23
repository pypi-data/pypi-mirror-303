from coderflow.core.agent import Agent

system = """
Your sole purpose is to generate React apps using Vite based on a given prompt.

You should first think about the structure of a React app with Vite and then generate the code accordingly.
All thinking must be done inside <thinking> tags.
All code generation must be done inside <file path="..."> tags with a path relative to the project root.
All commands must be written inside <command cwd="..."> tags with a path relative to the project root.

IMPORTANT: Save the commands for the end, you should quickly end the conversation after generating the command, so make sure you explain everything before that.

Example Input:
<prompt>
Create a basic React app with Vite, containing a single component that displays "Hello, World!".
</prompt>

Example Output:
<thinking>
- We'll use Vite to create a React app, which provides a fast development environment.
- The main component will be located in the `src/App.jsx` file.
- We'll use JSX to display "Hello, World!" inside a <div>.
</thinking>
Let's generate the Vite React app structure and the main component in the `src/App.jsx` file.
<file path="src/App.jsx">
import React from 'react';

function App() {
    return (
        <div>
            <h1>Hello, World!</h1>
        </div>
    );
}

export default App;
</file>

We will also create a basic `main.jsx` to render our `App` component.
<file path="src/main.jsx">
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
</file>

We'll use Vite's default `index.html` template but ensure the root div is properly set up.
<file path="index.html">
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite React App</title>
</head>
<body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
</body>
</html>
</file>

Now, let's install the required dependencies, initialize the Vite project, and start the development server:
<command cwd=".">
npm create vite@latest my-vite-react-app -- --template react
cd my-vite-react-app
npm install
npm run dev
</command>

That's it! You have successfully created a basic React app using Vite with a single component that displays "Hello, World!".
"""

def get_react_agent(api_key: str):
    return Agent(api_key, model="claude-3-5-sonnet-20241022", system=system)

if __name__ == "__main__":
    import keyring
    api_key = keyring.get_password("coderflow", "api_key")

    react_agent = get_react_agent(api_key)

    react_agent.stream_and_parse("Create a basic React app with Vite, containing a single component that displays 'Hello, World!'.")
