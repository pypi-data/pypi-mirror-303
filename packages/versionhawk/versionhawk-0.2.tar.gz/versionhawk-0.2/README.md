# 🦅 VersionHawk

VersionHawk is a tool for managing the versions of Python packages based on semantic versioning and the current date. It automatically suggests a new version tag if previous ones are already taken and allows you to fetch a list of all existing versions of a package.

## ✨ Features

	•	Generate a new version: Suggests a unique version tag based on the current date and time.
	•	View all versions: Optionally fetches a list of all existing versions of a package on PyPI.
	•	User-friendly command-line interface: Easily run it from the terminal.

## 🔧 Installation

You can install VersionHawk using pip:


pip install versionhawk

## 🚀 Usage

Once installed, you can run VersionHawk through the versionhawk command in your terminal.

## 🆕 Generate a New Version

To generate a new version for a package on PyPI, use the following command:


versionhawk <package_name>

Example:

versionhawk requests

## 📄 View All Versions

To fetch a list of all existing versions of a package on PyPI, use the --versions flag:

versionhawk <package_name> --versions

Example:

versionhawk requests --versions

## ⚙️ How It Works

VersionHawk uses the current date and time to suggest a new version. It checks the following patterns in order:

	•	Year.Month (e.g., 2024.10)
	•	Year.Month.Week Number in Month (e.g., 2024.10.3)
	•	Year.Month.Day (e.g., 2024.10.22)
	•	Year.Month.Day.Hour (e.g., 2024.10.22.20)
	•	Year.Month.Day.Hour.Minutes (e.g., 2024.10.22.20.01)
	•	Year.Month.Day.Hour.Minutes.Seconds (e.g., 2024.10.22.20.01.30)

VersionHawk checks these patterns against existing versions and suggests the first available unique tag.

## 💡 Example Usage

Let’s say the current date is 2024-10-22 20:01, and the requests package already has versions up to 2024.10.22.20.01. VersionHawk will suggest the next available version, such as 2024.10.22.20.01.30, if earlier versions are taken.

## 📦 Dependencies

VersionHawk requires the following dependencies to work:

	•	requests — to fetch version information from PyPI.
	•	packaging — to correctly sort versions.

These dependencies are automatically installed when you install VersionHawk.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.
