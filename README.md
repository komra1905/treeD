# treeStruct

**treeD** is a Python script that displays the folder structure in a tree-like format. It recursively traverses a specified directory and prints out the folder and file hierarchy using Unicode characters. The script omits common directories (like `.git` and `node_modules`) by default, and you can also specify additional directories to omit using the `-o` flag. Additionally, if you use the `-c` flag, the generated tree structure is copied to your system clipboard.

## Features

- **Recursive Directory Listing:** Recursively lists directories and files in a tree-like structure.
- **Default Omission:** Automatically omits directories like `.git` and `node_modules`.
- **Customizable Omissions:** Use the `-o` flag to omit additional directories.
- **Clipboard Copying:** Use the `-c` flag to copy the output to the system clipboard.
- **Cross-Platform:** Works on Windows, Linux, and macOS.

## Usage

### Basic Usage

Display the tree for the current directory:

```bash
python treed.py
```

Display the tree for a specific directory:

```bash
python treed.py C:\path\to\folder
```

### Omitting Directories

By default, `.git` and `node_modules` are omitted. To omit additional directories (e.g., `src` and `migrations`), use the `-o` flag:

```bash
python treed.py -o src migrations
```

### Copying Output to Clipboard

To copy the folder structure to the clipboard in addition to printing it, use the `-c` flag:

```bash
python treed.py -c
```

## Making the Script Available from Anywhere on Windows

Follow these steps to run `treeD` from any location on your Windows system:

### 1. Save Your Script in a Dedicated Folder

For example, create a folder (e.g., `C:\Scripts`) and place `treed.py` inside that folder.

### 2. Add the Folder to Your PATH Environment Variable

1. **Open System Environment Settings:**
   - Press **Win + S** (or click the search bar) and type **"Edit the system environment variables"**. Click the result to open it.

2. **Access Environment Variables:**
   - In the **System Properties** window, click on the **"Environment Variables..."** button.

3. **Edit the PATH Variable:**
   - Under **User variables** (or **System variables** if you want it available for all users), select the variable named `Path` and click **Edit**.
   - Click **New** and add the path to your script folder (e.g., `C:\Scripts`).
   - Click **OK** to close the dialogs.

4. **Restart Your Terminal:**
   - Close and reopen your Command Prompt or PowerShell window for the changes to take effect.

### 3. Run the Script from Anywhere

Now, open a new Command Prompt or PowerShell window and run:

```bash
python treed.py
```

If your system is configured to run `.py` files directly (via file associations), you can also simply type:

```bash
treed.py
```

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
