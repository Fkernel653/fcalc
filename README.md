# fcalc is a simple, colorful offline calculator based on the CustomTkinter library

[![Python](https://img.shields.io/badge/python-3.14+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey)]()
[![CustomTkinter](https://img.shields.io/badge/UI-customtkinter-1a6eae)](https://github.com/TomSchimansky/CustomTkinter)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-261230?logo=ruff&logoColor=white)](https://docs.astral.sh/ruff/)

A modern desktop calculator application built with Python and CustomTkinter. Features a clean, intuitive interface with both mouse and keyboard support, styled with a Dracula theme.

![Calculator Screenshot](screenshot.png)

## ✨ Features

- **Basic arithmetic operations** — addition (+), subtraction (-), multiplication (*), division (/)
- **Decimal numbers support**
- **Keyboard input** — full control without touching the mouse
- **Error handling** — clear messages for syntax errors and division by zero
- **Modern UI** — Dracula theme with system appearance mode
- **Responsive design** — grid-based button layout that scales cleanly
- **Offline** — no internet required, works entirely locally

Вижу, вы собираете README-секцию Quick Start. Вот структурированный вариант с вашими правками:

---

## 🚀 Quick Start

### Prerequisites
- Python 3.14+ & CustomTkinter library

### Installation

#### 1. Clone Repository

```bash
git clone -b customtk https://github.com/Fkernel653/fcalc.git && cd fcalc
```

#### 2. Install Dependencies

**uv** (recommended)
```bash
uv sync
```

**pip**
```bash
pip install .
```

**Poetry**
```bash
poetry install
```

**PDM**
```bash
pdm install
```

### Usage

```bash
python main.py
```

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Input numbers |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `.` | Decimal point |
| `=` or `Enter` | Calculate result |
| `Backspace` | Delete last character |
| `Escape` | Clear all (AC) |

## 📁 Project Structure

```
fcalc/
├── main.py           # Main calculator application
├── style.py          # Main style (Dracula colors)
├── pyproject.toml    # Project metadata and dependencies
├── README.md         # Project documentation
└── screenshot.png    # Application screenshot
```

## 🔧 Requirements

| Package | Purpose |
|---------|---------|
| `customtkinter` | Modern themed Tkinter widgets |
| `tkinter` | Built-in GUI framework (ships with Python) |

## 📘 Code Overview

The calculator is built using object-oriented programming principles:

- **Calc class** — Main application class inheriting from `customtkinter.CTk`
- **UI Components** — Buttons, display entry, and frame layout
- **Event Handlers** — Keyboard and mouse input processing
- **Calculation Engine** — Uses Python's `eval()` with error handling

## ⚠️ Error Messages

The calculator displays user-friendly error messages:

| Error | Message |
|-------|---------|
| Invalid syntax | `Error: The syntax is incorrect` |
| Division by zero | `Error: Division by zero` |

## 🎨 Customization

You can easily customize the calculator by modifying:

- **Window size** — Change `self.geometry("500x600")` in `main.py`
- **Theme** — Modify the Dracula color palette in `style.py`
- **Font** — Adjust the `Button` class font settings
- **Background** — Change `self.configure()` in the main window

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — Modern Tkinter widget library

---

**Author:** [Fkernel653](https://github.com/Fkernel653)  
**Repository:** [github.com/Fkernel653/fcalc](https://github.com/Fkernel653/fcalc)
