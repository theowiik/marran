#!/bin/bash

# Ensure autoflake, isort, and black are installed
echo "🔍 Checking and installing necessary tools..."
pip install autoflake isort black --quiet

# Define the target directory
TARGET_DIR="src"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Error: Target directory $TARGET_DIR does not exist."
    exit 1
fi

# Run autoflake, isort, and black on all Python files in the target directory
echo "🛠️ Processing Python files in $TARGET_DIR..."
find "$TARGET_DIR" -type f -name "*.py" -print0 | while IFS= read -r -d '' file; do
    autoflake --remove-all-unused-imports --in-place --remove-unused-variables "$file"
    isort "$file"
    black "$file"
    echo "✅ Processed $file"
done

echo "🎉 All Python files in the $TARGET_DIR directory have been processed by autoflake, isort, and black."
