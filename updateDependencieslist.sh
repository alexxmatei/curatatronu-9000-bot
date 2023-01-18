FILE_NAME="Dependencies.md"

# sed is used to add "  " to the string to describe newline in markdown
pip list | grep -e "^pytz\s" | sed 's/$/  /' > $FILE_NAME
pip list | grep supabase | sed 's/$/  /'  >> $FILE_NAME
pip list | grep python-dotenv | sed 's/$/  /'  >> $FILE_NAME
pip list | grep python-telegram-bot | sed 's/$/  /'  >> $FILE_NAME