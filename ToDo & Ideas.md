# ToDo
### Commands to implement
 - Request bot to print a table (Markdown?) with:
   - the current user and the tasks they still have
   - the current month with all the users and tasks that need to be done
 - Ability to check off commands
   - print the table with updated tasks afterwards
 - Request bot to print current resposible for the week (no table)
 - Add reporting command (with or without photo) and start a timer for user to solve spotaneous task (1 day)
   - User has to report task being completed
   - User can delay task with justification (and nr of days)
   - User (user1) can move task to another user (user2)
     - If user2 completes task, they receive bonus points, user1 loses points
   - Issue 4 warnings before penalizing (immediate, 2 hours, 12 hours, 22 hours)
 - Add a schedule report command to print all the queued jobs and the messages that will be printed in the current week (maybe next week too)
### Schedule to implement
 - Reminder 2 days before week ends (8AM)
 - Reminders the last day before week ends
   - morning (8 AM)
   - evening (8 PM)
 - Print table when a person's duty ends (Maybe calculate a score) (12AM)
 - Start the week by mentioning the new person's shift and print their table (8AM)
### Others
 - Add formatter to repo
 - Replace @user with telegramId when available
 - Add versioning
 - Add bi-weekly, monthly and asynchronous tasks
 - Add documentation & examples about libraries used
   - Example: Bot.send_message(text='some-text', chat_id=CHAT_ID)
 - Investigate Supabase / Postgres database naming convention (snake_case vs camelCase)

<br></br>
# Ideas
 - Implement a system to estimate each task duration and their importance
   - could be done using emojiis here or other symbols
 - Detect when scheduler gets a message to shut down (Ctrl + C) and send a message, "Bot shutting down..." for example.
 - Create an MVP
