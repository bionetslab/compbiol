# Practical Skills in Computational Biology

## Structure of the course

- Part 1 (April 13 - 27): Python intro. Material/instructions in `python-intro` folder.
- Part 2 (April 28 – June 1): Analysis of high-throughput sequencing data. Material/instructions in `htseq` folder.
- Part 3 (June 2 – July 7): Analysis of bioimaging data. Material/instructions in `bioimaging` folder. 

## Install Git (one-time setup)

You need Git for this course.

Check whether Git is already installed:

```bash
git --version
```

If this prints a version number, you are ready.

### macOS

Option A (recommended): install Xcode Command Line Tools:

```bash
xcode-select --install
```

Option B: install with Homebrew (if you already use Homebrew):

```bash
brew install git
```

### Windows

Install Git for Windows:
- https://git-scm.com/download/win

Then open a new **Git Bash** or **PowerShell** window and run:

```bash
git --version
```

### Linux

Use your distribution package manager:

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install git
```

Fedora:

```bash
sudo dnf install git
```

Arch Linux:

```bash
sudo pacman -S git
```

After installation, verify again:

```bash
git --version
```

## Create a GitHub account (one-time setup)

GitHub is a website where you can store and share your code repositories online.

### Why this is useful in this course

- Keep your own work backed up online.
- Track your progress over time with commits.
- Share your code with instructors or collaborators when needed.

### How to create an account

1. Go to https://github.com/signup.
2. Enter your email address and create a password.
3. Choose a username (this will be visible to others).
4. Verify your email when GitHub sends the confirmation message.
5. Sign in at https://github.com.

Optional but recommended for students:
- Use a recognizable username (or add your real name in profile settings).
- Add a profile picture so collaborators can identify you.