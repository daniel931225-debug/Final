# Development

---

## 📦 Prerequisites

Before you start, make sure you have the following tools installed:

* [Python 3.12+](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/) – Python environment and dependency manager
* [Node.js LTS](https://nodejs.org/)
* [pnpm](https://pnpm.io/) – Node.js package manager

---

## 🐍 Using uv (Backend Section)

### 1️⃣ Install or Update Dependencies

```bash
uv sync
```

### 2️⃣ Run the Application

```bash
uv run main.py
```

---

## 🌐 Using pnpm (Frontend Section)

### 1️⃣ Install Project Dependencies

```bash
pnpm install
```

### 2️⃣ Start the Development Server

```bash
pnpm dev
```

### 3️⃣ Build the Project

```bash
pnpm build
```

The build output will be generated in `/dist` or `/build`.

---

## ✨ Code Quality (Format & Lint)

To keep the codebase clean and consistent, use the following commands.

### 🔧 Lint

```bash
uv run ruff check
```

```bash
pnpm lint
```

### 🎨 Format

```bash
uv run ruff format
```

```bash
pnpm format
```

---

## 🧰 Additional Notes

* If you’re using **VS Code**, install the **Ruff**, **ESLint**, and **Prettier** extensions for a better development experience.
* Use a `.env` file to manage environment variables, and make sure it’s listed in `.gitignore` to avoid committing secrets.
