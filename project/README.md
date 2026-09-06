# Harvest Bot Launcher (13)

Create a desktop-style compact launcher UI for a game automation app named "CLASH FARM". Window style: - Frameless, dark theme (pure black / slate-950 background, #111318 cards) with rounded corners. - Custom window title bar at top: custom logo "H", title "HARVEST BOT", minimize (-) and close (X) buttons. - Sub-navigation tabs underneath header: "Home" (home icon), "Settings" (gear icon), "Profile" (user icon), "Log" (chat bubble icon). Make active tab highlighted with a rounded background. Screen 1: Home Tab - Select dropdowns: "Select Mode" (default: "Home Village") and "Select Army" (default: "Electric Dragon"). - Range sliders: * "Minimum Loot Threshold" with live dynamic value label on right (e.g. 500k). * "Max Storage Capacity" with live label (e.g. 27.0M). - A large, prominent primary button: "STOP" (red bg) / "START" (green/cyan bg) toggle. - "CURRENT SESSION" card at bottom listing key-value stats: * GOLD (yellow value: 0) * ELIXIR (magenta/pink value: 0) * ATTACK (cyan value: 0) * WALL (cyan value: 0) * TIME ELAPSED (white value: 0m) Screen 2: Settings Tab - Device selection row: Dropdown labeled "Select Device" showing "emulator-5554", next to a small "Refresh" button. - Two action buttons: "Restart ADB Server" and "Capture Event Troop". - List of clean toggle switches with cyan-blue active state: * "Deploy Heroes Automatically" (checked) * "Use Rage Spells" (checked) * "Use Siege Machines" (checked) * "Auto Upgrade Walls" (checked) * "Stop When Storage Get Full" (checked) * "Donate Troops Before Attack" (checked) * "Ask For Donation Before Attack" (checked) Screen 3: Log Tab - Top control bar: "Auto-scroll" toggle switch, "Clear" button, and line count counter (e.g. "2 lines"). - Dark embedded terminal area showing monospace green and purple log lines: * "Input backend: sendevent (fast)" * "Searching for a base to attack..." Use Tailwind CSS, Lucide-react icons, and polished modern styling.

This project was built with [Lovable](https://lovable.dev).

**Live app**: https://harvest-bot-ui.lovable.app

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/94ef1606-4da1-4b40-b115-518425f6b7b5).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
