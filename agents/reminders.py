import re
import datetime

def extract_medications(prescription_text: str):
    """
    Extracts medication names and dosages using regex (basic version).
    Example input: 'Take Paracetamol 500mg twice daily for 5 days'
    """
    meds = re.findall(r'([A-Z][a-zA-Z0-9]+)\s*(\d*mg)?', prescription_text)
    return [m[0] + (" " + m[1] if m[1] else "") for m in meds if m[0]]

def create_reminders(medications, days: int = 3, hour: int = 9):
    """Creates simple daily reminders for medications."""
    now = datetime.datetime.now()
    reminders = []
    for med in medications:
        for i in range(days):
            reminder_time = now + datetime.timedelta(days=i)
            reminder = f"Reminder: Take {med} at {reminder_time.strftime('%Y-%m-%d')} {hour}:00"
            reminders.append(reminder)
    return reminders
