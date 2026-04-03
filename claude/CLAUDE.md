# Project: Email to Calendar Assistant

## Purpose
A python CLI tool that reads unread Gmail emails, uses Claude to identify meetings, deadlines, and tasks, and automatically creates Google Calendar events or displays to-do items.

## Tech Stack
- python 3.14+ - main language
- Claude API (claude-sonnet) - email analysis and intent extraction
- Gmail MCP - read emails
- Google Calendar MCP - create calendar events
- python-dotenv - environment variable management

## Architecture
1. Fetch unread emails from Gmail
2. Send email content to Claude for analysis
3. Claude identifies: meeting/deadline/task/irrelevant
4. If meeting -> create Google Calendar event via MCP
5. If task -> print to console as to-do item

## Coding conventions
- All functions have type hints
- Each function does one thing
- Comments in english
- Error handling for every MCP call

## What Claude AI should NOT do without asking
- Add new dependencies to requirements.txt
- Change the data flow architecture
- Delete or overwrite existing calendar events
- Make API calls that cost money without confirmation