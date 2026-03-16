#!/usr/bin/env bash
# PM_FRAMEWORK — First-time setup script
# Creates your first property and configures AGENT_CONTEXT.md
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/properties/property-template"

echo "============================================"
echo "  PM_FRAMEWORK — First-Time Setup"
echo "============================================"
echo ""

# --- Gather info -----------------------------------------------------------

read -rp "Your name (property owner): " OWNER_NAME
if [[ -z "$OWNER_NAME" ]]; then
  echo "Error: Owner name is required." >&2
  exit 1
fi

read -rp "Number of properties to set up [1]: " PROP_COUNT
PROP_COUNT="${PROP_COUNT:-1}"

declare -a PROP_SLUGS
declare -a PROP_ADDRESSES

for ((i = 1; i <= PROP_COUNT; i++)); do
  echo ""
  echo "--- Property $i ---"
  read -rp "  Short name / slug (e.g. 'maple-st'): " SLUG
  read -rp "  Full address: " ADDRESS
  PROP_SLUGS+=("$SLUG")
  PROP_ADDRESSES+=("$ADDRESS")
done

echo ""
read -rp "Your state (e.g. Oregon, Texas, California): " STATE

echo ""
echo "Which AI tool will you use primarily?"
echo "  1) Claude Code (Anthropic)"
echo "  2) ChatGPT / GPT-4"
echo "  3) Cursor"
echo "  4) Other / Not sure"
read -rp "Choice [1]: " AI_CHOICE
AI_CHOICE="${AI_CHOICE:-1}"

case "$AI_CHOICE" in
  1) AI_TOOL="Claude Code" ;;
  2) AI_TOOL="ChatGPT / GPT-4" ;;
  3) AI_TOOL="Cursor" ;;
  *) AI_TOOL="AI Assistant" ;;
esac

# --- Create properties from template ----------------------------------------

echo ""
echo "Creating properties..."

for ((i = 0; i < PROP_COUNT; i++)); do
  SLUG="${PROP_SLUGS[$i]}"
  ADDRESS="${PROP_ADDRESSES[$i]}"
  DEST="$SCRIPT_DIR/properties/$SLUG"

  if [[ -d "$DEST" ]]; then
    echo "  Skipping '$SLUG' — already exists."
    continue
  fi

  cp -r "$TEMPLATE_DIR" "$DEST"

  # Replace placeholders in README.md
  if [[ -f "$DEST/README.md" ]]; then
    sed -i '' "s/\[PROPERTY_ADDRESS\]/$ADDRESS/g" "$DEST/README.md" 2>/dev/null || \
    sed -i "s/\[PROPERTY_ADDRESS\]/$ADDRESS/g" "$DEST/README.md"

    sed -i '' "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$DEST/README.md" 2>/dev/null || \
    sed -i "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$DEST/README.md"
  fi

  echo "  Created: properties/$SLUG/"
done

# --- Update AGENT_CONTEXT.md -----------------------------------------------

CONTEXT_FILE="$SCRIPT_DIR/AGENT_CONTEXT.md"

if [[ -f "$CONTEXT_FILE" ]]; then
  echo ""
  echo "Updating AGENT_CONTEXT.md..."

  # Build property list for context file
  PROP_LIST=""
  for ((i = 0; i < PROP_COUNT; i++)); do
    PROP_LIST+="- **${PROP_ADDRESSES[$i]}** → \`properties/${PROP_SLUGS[$i]}/\`\n"
  done

  # Update owner name
  sed -i '' "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$CONTEXT_FILE" 2>/dev/null || \
  sed -i "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$CONTEXT_FILE"

  # Update state
  sed -i '' "s/\[YOUR_STATE\]/$STATE/g" "$CONTEXT_FILE" 2>/dev/null || \
  sed -i "s/\[YOUR_STATE\]/$STATE/g" "$CONTEXT_FILE"

  # Update AI tool
  sed -i '' "s/\[AI_TOOL\]/$AI_TOOL/g" "$CONTEXT_FILE" 2>/dev/null || \
  sed -i "s/\[AI_TOOL\]/$AI_TOOL/g" "$CONTEXT_FILE"

  # Update last-updated date
  TODAY=$(date +%Y-%m-%d)
  sed -i '' "s/\[LAST_UPDATED\]/$TODAY/g" "$CONTEXT_FILE" 2>/dev/null || \
  sed -i "s/\[LAST_UPDATED\]/$TODAY/g" "$CONTEXT_FILE"

  echo "  Done."
fi

# --- Update continuity files -----------------------------------------------

echo "Updating continuity placeholders..."
for f in "$SCRIPT_DIR"/continuity/*.md; do
  if [[ -f "$f" ]]; then
    sed -i '' "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$f" 2>/dev/null || \
    sed -i "s/\[OWNER_NAME\]/$OWNER_NAME/g" "$f"
  fi
done

# --- Summary ----------------------------------------------------------------

echo ""
echo "============================================"
echo "  Setup Complete!"
echo "============================================"
echo ""
echo "Owner:      $OWNER_NAME"
echo "State:      $STATE"
echo "AI Tool:    $AI_TOOL"
echo "Properties: $PROP_COUNT"
for ((i = 0; i < PROP_COUNT; i++)); do
  echo "  - ${PROP_ADDRESSES[$i]} (properties/${PROP_SLUGS[$i]}/)"
done
echo ""
echo "Next steps:"
echo "  1. Fill in property details:  properties/<slug>/README.md"
echo "  2. Add state compliance docs: compliance/ or copy from examples/"
echo "  3. Launch the dashboard:      cd webapp && ./startup.sh"
echo "  4. Start your AI assistant and point it at AGENT_CONTEXT.md"
echo ""
echo "See docs/getting-started.md for the full walkthrough."
