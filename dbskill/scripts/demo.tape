# dbskill plugin marketplace demo
# Self-bootstrapped: cleans previous state, creates filter wrapper, records clean demo
# MARKETPLACE_REPO placeholder is patched by record-demo.sh before recording

Output demo.gif
Set Theme "Catppuccin Latte"
Set FontSize 24
Set Width 1400
Set Height 600
Set Padding 20
Set TypingSpeed 10ms
Set Shell zsh

# Bootstrap (hidden): clean previous state, install output filter, clear screen
Hide
Type "claude plugin uninstall dbs-diagnosis@dontbesilent-skills 2>/dev/null; claude plugin uninstall dbs@dontbesilent-skills 2>/dev/null; claude plugin marketplace remove dontbesilent-skills 2>/dev/null"
Enter
Sleep 4s
# Base64 wrapper: claude() { command claude "$@" 2>&1 | grep -v -E "SSH|cache|Clon|Refresh|timeout"; }
# Filters noisy git-clone progress lines. Base64 needed because VHS cannot parse $ and \" in Type.
Type "echo Y2xhdWRlKCkgeyBjb21tYW5kIGNsYXVkZSAiJEAiIDI+JjEgfCBncmVwIC12IC1FICJTU0h8Y2FjaGV8Q2xvbnxSZWZyZXNofHRpbWVvdXQiOyB9Cg== | base64 -d > /tmp/cw.sh && source /tmp/cw.sh"
Enter
Sleep 500ms
Type "clear"
Enter
Sleep 500ms
Show

# Add marketplace
Type "claude plugin marketplace add MARKETPLACE_REPO"
Enter
Sleep 12s
Enter
Sleep 300ms

# Install skills
Type "claude plugin install dbs-diagnosis@dontbesilent-skills"
Enter
Sleep 3s
Enter
Sleep 300ms

Type "claude plugin install dbs@dontbesilent-skills"
Enter
Sleep 3s
Enter
Sleep 300ms

# Verify
Type "claude plugin list | grep -A2 dbs"
Enter
Sleep 2s

Sleep 1s
