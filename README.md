# Flow Launcher Repeater Plugin

A simple but powerful plugin for **Flow Launcher** to repeat a string a specified number of times.

---

## 🚀 Usage

The plugin is triggered by the `repeat` keyword.

1. Open **Flow Launcher** (usually with `Alt + Space`).
2. Type `repeat` followed by your query.
3. The query format is:

   ```
   <number>::<string to repeat>
   ```

### Example

To repeat the text `"hello "` three times, type:

```
repeat 3::hello
```

The plugin will show you the result:

```
hello hello hello
```

Selecting this result will automatically copy it to your clipboard.

---

## 🤖 Installation

### 1. Python Requirement

Make sure you have **Python** installed and it's added to your system's `PATH`.

### 2. FlowLauncher Library

The plugin requires the `flowlauncher` Python library.
Install it by running:

```bash
pip install flowlauncher
```

### 3. Plugin Folder

Place the entire **Repeater** folder into your **Flow Launcher user plugins** directory.

To easily find this directory:

1. Type `fd` in Flow Launcher.
2. Select **"Open Flow's user data folder"**.
3. Navigate to the `Plugins` subdirectory.

### 4. Restart

Restart **Flow Launcher** to load the new plugin.

